import flet as ft

def main(page: ft.Page):
    page.title = "Column Alignment Comparison"

    # START (left aligned)
    start_column = ft.Column(
        width=220,
        height=200,
        spacing=12,
        controls=[
            ft.Text("START", size=20, weight=ft.FontWeight.W_600),
            ft.Text("Review pull requests"),
            ft.Text("Ship release"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.START
    )

    # CENTER (horizontally centered)
    center_column = ft.Column(
        width=220,
        height=200,
        spacing=12,
        controls=[
            ft.Text("CENTER", size=20, weight=ft.FontWeight.W_600),
            ft.Text("Review pull requests"),
            ft.Text("Ship release"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    # END (right aligned)
    end_column = ft.Column(
        width=220,
        height=200,
        spacing=12,
        controls=[
            ft.Text("END", size=20, weight=ft.FontWeight.W_600),
            ft.Text("Review pull requests"),
            ft.Text("Ship release"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.END
    )

    # STRETCH (fill width)
    stretch_column = ft.Column(
        width=220,
        height=200,
        spacing=12,
        controls=[
            ft.Text("STRETCH", size=20, weight=ft.FontWeight.W_600),
            ft.Text("Review pull requests"),
            ft.Text("Ship release"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH
    )

    # Place all columns in a row
    page.add(
        ft.Row(
            controls=[start_column, center_column, end_column, stretch_column],
            spacing=20
        )
    )

ft.app(target=main)
