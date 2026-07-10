from datetime import date, datetime


class Category:
    def __init__(self, name, color: str = '#4A90d9'):
        self.name = name
        self.color = color

    def to_dict(self) -> dict:
        return {'name': self.name, 'color': self.color}

    @classmethod
    def from_dict(cls, data : dict) -> 'Category':
        return cls(name = data['name'], color = data['color'])

    def __repr__(self):
        return f'Category(name={self.name}, color={self.color})'

class Movement:
    TYPE_INCOME = 'Ingreso'
    TYPE_EXPENSE = 'Gasto'
    VALID_TYPES = [TYPE_INCOME, TYPE_EXPENSE]

    def __init__(self, title, amount, category, kind,
                 movement_date : str | None = None):
        self.title = title
        self.amount = amount
        self.category = category
        self.kind = kind
        self.movement_date = movement_date or date.today().strftime('%d/%m/%Y')

    def to_dict(self) -> dict:
        return { 'title': self.title,
                 'amount': self.amount,
                 'category': self.category,
                 'kind': self.kind,
                 'movement_date': str(self.movement_date)
                 }

    @classmethod
    def from_dict (cls, data : dict) -> 'Movement':
        return Movement(
            title= data['title'],
            amount= data['amount'],
            category= data['category'],
            kind= data['kind'],
            movement_date= data.get('movement_date')
        )

    def __repr__(self):
        return (f'Movement(title={self.title}, amount={self.amount}, category={self.category}, '
                f'kind={self.kind}, movement_date={self.movement_date})')


def validate_title(title) -> str | None:
    '''Devuelve mensaje de error o None si es válido'''
    title = title.strip()
    if not title:
        return "El título no puede estar vacío"
    if len(title) > 100:
        return  "El título no puede pasar de los 100 caracteres"
    return None

def validate_amount(amount_str:str) -> tuple[float | None, str | None]:
    '''Retorna (amount_float | None) si es válida'''
    try:
        amount = float(amount_str.strip().replace(',', '.'))
    except(ValueError, TypeError):
        return None, "El monto debe ser un numero (ej: 150.50)"
    if amount <= 0:
        return None, "El monto debe ser mayor que 0"
    return amount, None

def validate_date(date_str: str, enable_future: bool = False) -> str | None:
    '''retorna mensaje de error o None si la fecha es válida'''
    date_str = date_str.strip()
    try:
        valid_date = datetime.strptime(date_str, '%d/%m/%Y').date()
    except ValueError:
        return "Formato de fecha inválido (use dd/mm/yyyy)"
    if not enable_future and valid_date > date.today():
        return "La fecha no puede ser futura"
    return None

def validate_category(name) -> str | None:
    name = name.strip()
    if not name:
        return "El nombre de la categoría no puede estar vacío"
    if len(name) > 50:
        return "el nombre no puede superar los 50 caracteres"
    return None

class FinanceManager:
    '''Orquesta categorías y movimientos. No depende de la interfaz gráfica'''
    def __init__(self):
        self.categories : list[Category] = []
        self.movements : list[Movement] = []

    def add_category(self, name, color : str = "#4A90D9") -> tuple[bool, str]:
        error = validate_category(name)
        if error:
            return False, error
        clean_name = name.strip()
        if self.existing_category(clean_name):
            return False, f'La categoría {clean_name} ya existe'
        self.categories.append(Category(clean_name, color))
        return True, "Categoría agregada correctamente"

    def existing_category(self, name) -> bool:
        name_lower = name.strip().lower()
        return any(c.name.lower() == name_lower for c in self.categories)

    def obtain_category_name(self) -> list[str]:
        return [c.name for c in self.categories]

    def obtain_color_category(self, name) -> str:
        for c in self.categories:
            if c.name.lower() == name.strip().lower():
                return c.color
        return "#FFFFFF"

    def add_movement(self, title: str, amount_str: str,
                     category: str, kind: str,
                     date_str: str | None = None) -> tuple[bool, str]:
        if not self.categories:
            return False, "Primero debes agregar al menos una categoría."
        if kind not in Movement.VALID_TYPES:
            return False, f"Tipo inválido: {kind!r}."
        if not self.existing_category(category):
            return False, f"La categoría '{category}' no existe."

        error = validate_title(title)
        if error:
            return False, error

        amount, error = validate_amount(amount_str)
        if error:
            return False, error

        date_str = date_str or datetime.today().strftime("%d/%m/%Y")
        error_date = validate_date(date_str)
        if error_date:
            return False, error_date

        final_amount = amount if kind == Movement.TYPE_INCOME else -abs(amount)
        self.movements.append(Movement(title.strip(), final_amount, category, kind, date_str))
        return True, f"{kind} agregado correctamente."

    def total_income(self) -> float:
        return sum(m.amount for m in self.movements if m.amount > 0)

    def total_expenses(self) -> float:
        return abs(sum(m.amount for m in self.movements if m.amount < 0))

    def balance(self) -> float:
        return sum(m.amount for m in self.movements)

    def filter_by_range(self, init_date: str, end_date: str) -> list[Movement]:
        """Filtra movimientos entre dos fechas (dd/mm/yyyy, inclusive)."""
        try:
            begin_date = datetime.strptime(init_date.strip(), "%d/%m/%Y")
            ending_date = datetime.strptime(end_date.strip(), "%d/%m/%Y")
        except ValueError:
            return []
        result = []
        for m in self.movements:
            try:
                fecha_m = datetime.strptime(m.movement_date, "%d/%m/%Y")
                if begin_date <= fecha_m <= ending_date:
                    result.append(m)
            except ValueError:
                continue
        return result

    def movement_rows(self, movement_list: list[Movement] | None = None) -> list[list]:
        """Devuelve los movimientos en formato de tabla para la GUI."""
        source = movement_list if movement_list is not None else self.movements
        rows = []
        for m in source:
            symbol = "+" if m.amount >= 0 else ""
            rows.append([
                m.movement_date,
                m.title,
                f"{symbol}{m.amount:,.2f}",
                m.category,
                m.kind,
            ])
        return rows