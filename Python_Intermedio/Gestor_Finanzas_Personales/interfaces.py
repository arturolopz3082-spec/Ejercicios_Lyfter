"""
interfaces.py — Toda la lógica de interfaz gráfica con FreeSimpleGUI.
Importa la lógica de logica.py y la persistencia de persistencia.py,
pero no contiene reglas de negocio propias.
"""

import FreeSimpleGUI as sg
from datetime import datetime

from logic import FinanceManager, Movement, validate_date

# ─────────────────────────── Tema visual ────────────────────────────

MAIN_FONT = ("Helvetica", 11)
TITLE_FONT    = ("Helvetica", 13, "bold")
MONO_FONT      = ("Courier", 10)

BACKGROUND_COLOR      = "#1C1C2E"   # índigo oscuro
PANEL_COLOR      = "#2A2A3E"   # panel ligeramente más claro
ACCENT_COLOR     = "#7C6AF7"   # violeta
ACCENT_COLOR2 = "#4CAF7D"   # verde menta (ingresos)
DANGER_COLOR    = "#E05C6B"   # rojo suave (gastos/errores)
TEXT_COLOR      = "#E8E8F0"
SEC_TEXT_COLOR = "#8888A8"
FIELD_COLOR      = "#12121E"

sg.theme("DarkGrey13")
sg.set_options(font=MAIN_FONT)


# ─────────────────────────── Helpers visuales ────────────────────────────

def _btn(text: str, key: str, color: str = ACCENT_COLOR,
         width: int = 18) -> sg.Button:
    return sg.Button(
        text, key=key, size=(width, 1),
        button_color=(TEXT_COLOR, color),
        border_width=0,
    )


def _field(label: str, key: str, default: str = "",
           ancho: int = 30) -> list:
    return [
        sg.Text(label, size=(14, 1), text_color=SEC_TEXT_COLOR,
                background_color=PANEL_COLOR),
        sg.Input(default_text=default, key=key, size=(ancho, 1),
                 background_color=FIELD_COLOR, text_color=TEXT_COLOR,
                 border_width=1),
    ]


def _combo(label: str, key: str, options: list,
           default: str = "") -> list:
    return [
        sg.Text(label, size=(14, 1), text_color=SEC_TEXT_COLOR,
                background_color=PANEL_COLOR),
        sg.Combo(options, default_value=default or (options[0] if options else ""),
                 key=key, size=(28, 1),
                 background_color=FIELD_COLOR, text_color=TEXT_COLOR,
                 button_background_color=ACCENT_COLOR,
                 readonly=True),
    ]


def _divider() -> sg.HSeparator:
    return (sg.HSeparator(color=ACCENT_COLOR))


def _show_error(message: str) -> None:
    sg.popup_error(message, title="Error", background_color=BACKGROUND_COLOR,
                   text_color=DANGER_COLOR, font=MAIN_FONT,
                   button_color=(TEXT_COLOR, DANGER_COLOR))


def _show_ok(message: str) -> None:
    sg.popup(message, title="Listo", background_color=BACKGROUND_COLOR,
             text_color=ACCENT_COLOR2, font=MAIN_FONT,
             button_color=(TEXT_COLOR, ACCENT_COLOR2))


# ─────────────────────────── Ventanas secundarias ────────────────────────────

def add_category_window(manager: FinanceManager) -> bool:
    """Abre el formulario para agregar una categoría. Retorna True si se agregó."""
    layout = [
        [sg.Text("Nueva Categoría", font=TITLE_FONT,
                 background_color=PANEL_COLOR, text_color=TEXT_COLOR)],
        [_divider()],
        _field("Nombre:", "-CAT-NOMBRE-"),
        [
            sg.Text("Color:", size=(14, 1), text_color=SEC_TEXT_COLOR,
                    background_color=PANEL_COLOR),
            sg.Input("#4A90D9", key="-CAT-COLOR-", size=(10, 1),
                     background_color=FIELD_COLOR, text_color=TEXT_COLOR),
            sg.ColorChooserButton("Elegir…", target="-CAT-COLOR-",
                                  button_color=(TEXT_COLOR, ACCENT_COLOR),
                                  border_width=0),
        ],
        [sg.VPush(background_color=PANEL_COLOR)],
        [_btn("Guardar categoría", "-GUARDAR-", ACCENT_COLOR2),
         _btn("Cancelar", "-CANCELAR-", SEC_TEXT_COLOR)],
    ]

    window = sg.Window("Agregar Categoría", layout,
                        background_color=PANEL_COLOR,
                        modal=True, finalize=True)
    save = False
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "-CANCELAR-"):
            break
        if event == "-GUARDAR-":
            ok, msg = manager.add_category(
                values["-CAT-NOMBRE-"], values["-CAT-COLOR-"])
            if ok:
                save = True
                _show_ok(msg)
                break
            else:
                _show_error(msg)
    window.close()
    return save

def _obtain_row_colors(manager: FinanceManager, lista=None) -> list:
    font = lista if lista is not None else manager.movements
    return [
        (i, manager.obtain_color_category(m.category))
        for i, m in enumerate(font)
    ]

def _movement_window(manager: FinanceManager, type: str) -> bool:
    """Formulario genérico para Ingreso o Gasto."""
    nombres = manager.obtain_category_name()
    hoy = datetime.today().strftime("%d/%m/%Y")
    icon = "💰" if type == Movement.TYPE_INCOME else "💸"
    color_btn = ACCENT_COLOR2 if type == Movement.TYPE_INCOME else DANGER_COLOR

    layout = [
        [sg.Text(f"{icon} Nuevo {type}", font=TITLE_FONT,
                 background_color=PANEL_COLOR, text_color=TEXT_COLOR)],
        [_divider()],
        _field("Título:", "-MOV-TITULO-"),
        _field("Monto ($):", "-MOV-MONTO-"),
        _field("Fecha (dd/mm/yyyy):", "-MOV-FECHA-", default=hoy),
        _combo("Categoría:", "-MOV-CAT-", nombres),
        [sg.VPush(background_color=PANEL_COLOR)],
        [_btn(f"Guardar {type.lower()}", "-GUARDAR-", color_btn),
         _btn("Cancelar", "-CANCELAR-", SEC_TEXT_COLOR)],
    ]

    window = sg.Window(f"Agregar {type}", layout,
                        background_color=PANEL_COLOR,
                        modal=True, finalize=True)
    save = False
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "-CANCELAR-"):
            break
        if event == "-GUARDAR-":
            ok, msg = manager.add_movement(
                title=values["-MOV-TITULO-"],
                amount_str=values["-MOV-MONTO-"],
                category=values["-MOV-CAT-"],
                kind=type,
                date_str=values["-MOV-FECHA-"],
            )
            if ok:
                save = True
                _show_ok(msg)
                break
            else:
                _show_error(msg)
    window.close()
    return save


def add_income_window(manager: FinanceManager) -> bool:
    if not manager.categories:
        _show_error("No hay categorías disponibles.\nAgrega una categoría primero.")
        return False
    return _movement_window(manager, Movement.TYPE_INCOME)


def add_expense_window(manager: FinanceManager) -> bool:
    if not manager.categories:
        _show_error("No hay categorías disponibles.\nAgrega una categoría primero.")
        return False
    return _movement_window(manager, Movement.TYPE_EXPENSE)


# ─────────────────────────── Ventana principal ────────────────────────────

TABLE_HEADER = ["Fecha", "Título", "Monto", "Categoría", "Tipo"]
COLUMN_WIDTH = [12, 28, 12, 16, 10]


def _build_summary(manager: FinanceManager) -> list[list[sg.Element]]:
    return [
        [
            sg.Text("Ingresos:", text_color=ACCENT_COLOR2,
                    background_color=PANEL_COLOR),
            sg.Text(f"${manager.total_income():,.2f}",
                    key="-TOTAL-ING-", text_color=ACCENT_COLOR2,
                    background_color=PANEL_COLOR, font=TITLE_FONT),
            sg.Text("   Gastos:", text_color=DANGER_COLOR,
                    background_color=PANEL_COLOR),
            sg.Text(f"${manager.total_expenses():,.2f}",
                    key="-TOTAL-GAS-", text_color=DANGER_COLOR,
                    background_color=PANEL_COLOR, font=TITLE_FONT),
            sg.Text("   Balance:", text_color=SEC_TEXT_COLOR,
                    background_color=PANEL_COLOR),
            sg.Text(f"${manager.balance():,.2f}",
                    key="-BALANCE-", text_color=TEXT_COLOR,
                    background_color=PANEL_COLOR, font=TITLE_FONT),
        ]
    ]


def _principal_layout(manager: FinanceManager) -> list:
    table_rows = manager.movement_rows()

    layout = [
        # ── Encabezado
        [
            sg.Text("Gestor de Finanzas", font=("Helvetica", 16, "bold"),
                    text_color=ACCENT_COLOR, background_color=BACKGROUND_COLOR),
            sg.Push(background_color=BACKGROUND_COLOR),
            sg.Text("", key="-FECHA-HOY-", text_color=SEC_TEXT_COLOR,
                    background_color=BACKGROUND_COLOR),
        ],
        [_divider()],

        # ── Resumen financiero
        [sg.Frame("Resumen", _build_summary(manager),
                  background_color=PANEL_COLOR,
                  title_color=ACCENT_COLOR2,
                  relief=sg.RELIEF_FLAT, expand_x=True)],

        # ── Filtro por fechas
        [sg.Frame("Filtrar por rango de fechas", [
            [
                sg.Text("Desde:", text_color=SEC_TEXT_COLOR,
                        background_color=PANEL_COLOR),
                sg.Input("", key="-FEC-INI-", size=(12, 1),
                         background_color=FIELD_COLOR, text_color=TEXT_COLOR),
                sg.CalendarButton(
                    "Fecha Inicio",
                    target="-FEC-INI-",
                    format="%d/%m/%Y",
                    button_color=(TEXT_COLOR, PANEL_COLOR),
                    border_width=0
                ),
                sg.Text("Hasta:", text_color=SEC_TEXT_COLOR,
                        background_color=PANEL_COLOR),
                sg.Input("", key="-FEC-FIN-", size=(12, 1),
                         background_color=FIELD_COLOR, text_color=TEXT_COLOR),
                sg.CalendarButton(
                    "Fecha Final",
                    target="-FEC-FIN-",
                    format="%d/%m/%Y",
                    button_color=(TEXT_COLOR, PANEL_COLOR),
                    border_width=0
                ),
                _btn("Filtrar", "-FILTRAR-", ACCENT_COLOR, width=10),
                _btn("Ver todos", "-VER-TODOS-", SEC_TEXT_COLOR, width=10),
            ]
        ], background_color=PANEL_COLOR, title_color=SEC_TEXT_COLOR,
                  relief=sg.RELIEF_FLAT, expand_x=True)],

        # ── Tabla de movimientos
        [sg.Table(
            values=table_rows,
            headings=TABLE_HEADER,
            col_widths=COLUMN_WIDTH,
            auto_size_columns=False,
            key="-TABLA-",
            display_row_numbers=False,
            justification="left",
            num_rows=14,
            background_color=FIELD_COLOR,
            text_color=TEXT_COLOR,
            header_background_color=PANEL_COLOR,
            header_text_color=ACCENT_COLOR,
            alternating_row_color="#1A1A2E",
            expand_x=True,
            enable_events=True,
            row_colors=_obtain_row_colors(manager)
        )],

        [_divider()],

        # ── Botones de acción
        [
            _btn("Categoría",  "-BTN-CAT-",     ACCENT_COLOR),
            _btn("Ingreso",    "-BTN-ING-",     SEC_TEXT_COLOR),
            _btn("Gasto",      "-BTN-GAS-", DANGER_COLOR),
            sg.Push(background_color=BACKGROUND_COLOR),
            _btn("Exportar CSV", "-BTN-CSV-", ACCENT_COLOR, width=16),
        ],
    ]
    return layout


def _update_table(window: sg.Window, manager: FinanceManager,
                  table_list=None) -> None:
    rows = manager.movement_rows(table_list)
    colors = _obtain_row_colors(manager, table_list)
    window["-TABLA-"].update(values=rows, row_colors=colors)


def _update_summary(window: sg.Window, manager: FinanceManager) -> None:
    window["-TOTAL-ING-"].update(f"${manager.total_income():,.2f}")
    window["-TOTAL-GAS-"].update(f"${manager.total_expenses():,.2f}")
    color_balance = ACCENT_COLOR2 if manager.balance() >= 0 else DANGER_COLOR
    window["-BALANCE-"].update(f"${manager.balance():,.2f}",
                               text_color=color_balance)


def deploy_app(manager: FinanceManager,
               fn_save=None, fn_export=None) -> None:
    """
    Lanza la ventana principal.
    fn_guardar(gestor) se llama tras cada cambio.
    fn_exportar(gestor) se llama al presionar Exportar CSV.
    """
    if fn_save is None:
        raise ValueError("fn_save es requerido")
    if fn_export is None:
        raise ValueError("fn_export es requerido")

    window = sg.Window(
        "Gestor de Finanzas Personales",
        _principal_layout(manager),
        background_color=BACKGROUND_COLOR,
        finalize=True,
        resizable=True,
        size=(820, 600),
    )

    # Fecha de hoy en encabezado
    window["-FECHA-HOY-"].update(
        datetime.today().strftime("%A %d/%m/%Y").capitalize())

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            fn_save(manager)
            break

        elif event == "-BTN-CAT-":
            if add_category_window(manager):
                fn_save(manager)

        elif event == "-BTN-ING-":
            if add_income_window(manager):
                fn_save(manager)
                _update_table(window, manager)
                _update_summary(window, manager)

        elif event == "-BTN-GAS-":
            if add_expense_window(manager):
                fn_save(manager)
                _update_table(window, manager)
                _update_summary(window, manager)

        elif event == "-FILTRAR-":
            begin_date = values["-FEC-INI-"].strip()
            end_date    = values["-FEC-FIN-"].strip()
            if not begin_date or not end_date:
                _show_error("Ingresa ambas fechas para filtrar.")
            else:
                error_begin = validate_date(begin_date, enable_future=True)
                error_end = validate_date(end_date, enable_future=True)
                if error_begin:
                    _show_error(f"Fecha de inicio inválida_ {error_begin}")
                elif error_end:
                    _show_error(f"Fecha de fin inválida_ {error_end}")
                elif datetime.strptime(begin_date, "%d/%m/%Y") > datetime.strptime(end_date, "%d/%m/%Y"):
                    _show_error("La fecha de inicio no puede ser posterior a la fecha fin")
                else:
                    filtered = manager.filter_by_range(begin_date, end_date)
                    _update_table(window, manager, filtered)
                    if not filtered:
                        _show_error("No hay movimientos en ese rango de fechas")

        elif event == "-VER-TODOS-":
            _update_table(window, manager)
            window["-FEC-INI-"].update("")
            window["-FEC-FIN-"].update("")

        elif event == "-BTN-CSV-":
            ruta = fn_export(manager)
            if ruta:
                _show_ok(f"CSV exportado exitosamente:\n{ruta}")
            else:
                print(f"No se pudo exportar el archivo CSV")

    window.close()