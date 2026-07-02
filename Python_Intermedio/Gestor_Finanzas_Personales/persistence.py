import json
import os
import csv

from logic import FinanceManager, Category, Movement

FILE_NAME = 'finance_info.json'

def save_finance_info(manager: FinanceManager, file= FILE_NAME) -> None:
    '''Serializa categorias y movimientos en un archivo JSON'''
    data = {
        'categories' : [c.to_dict() for c in manager.categories],
        'movements' : [c.to_dict() for c in manager.movements],
    }
    try:
        with open(file, 'w', encoding = 'utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f"error al guardar los datos: {e}")

def load_finance_info( manager: FinanceManager, file = FILE_NAME ) -> None:
    '''Carga categorias y movimientos desde un archivo JSON (si existe).'''
    if not os.path.exists(file):
        return
    try:
        with open(file, 'r', encoding = 'utf-8') as f:
            data = json.load(f)
        manager.categories = [Category.from_dict(c) for c in data.get('categories', [])]
        manager.movements = [Movement.from_dict(m) for m in data.get('movements', [])]
    except (json.JSONDecodeError, KeyError):
        manager.categories = []
        manager.movements = []


def export_csv(manager: FinanceManager, file='movements.csv') -> str:
    '''
    Genera un archivo CSV con todos los movimientos y un bloque de totales.
    Retorna la ruta del archivo creado.
    '''
    try:
        with open(file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)

            # Encabezado
            writer.writerow(['Fecha', 'Título', 'Monto', 'Categoría', 'Tipo'])

            # Filas de movimientos
            for m in manager.movements:
                writer.writerow([m.movement_date, m.title, m.amount, m.category, m.kind])

            # Bloque de totales
            writer.writerow([])
            writer.writerow(['Totales:'])
            writer.writerow(['Ingresos:', manager.total_income()])
            writer.writerow(['Gastos:', manager.total_expenses()])
            writer.writerow(['Balance Neto:', manager.balance()])

        return file
    except OSError as e:
        print(f"error al guardar los datos: {e}")
        return None