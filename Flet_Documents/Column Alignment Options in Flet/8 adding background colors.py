import flet as ft

def main(page: ft.Page):
    page.title = "Column Alignment Comparison with Colors"

    # Vertical START
    vertical_start = ft.Container(
        bgcolor="lightblue",
        content=ft.Column(
            width=220,
            height=200,
            spacing=12,
            controls=[
                ft.Text("Vertical START", size=20, weight=ft.FontWeight.W_600),
                ft.Text("Review pull requests"),
                ft.Text("Ship release"),
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    # Vertical CENTER
    vertical_center = ft.Container(
        bgcolor="lightgreen",
        content=ft.Column(
            width=220,
            height=200,
            spacing=12,
            controls=[
                ft.Text("Vertical CENTER", size=20, weight=ft.FontWeight.W_600),
                ft.Text("Review pull requests"),
                ft.Text("Ship release"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    # Vertical END
    vertical_end = ft.Container(
        bgcolor="lightyellow",
        content=ft.Column(
            width=220,
            height=200,
            spacing=12,
            controls=[
                ft.Text("Vertical END", size=20, weight=ft.FontWeight.W_600),
                ft.Text("Review pull requests"),
                ft.Text("Ship release"),
            ],
            alignment=ft.MainAxisAlignment.END,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    # Horizontal comparison row
    horizontal_row = ft.Row(
        controls=[
            ft.Container(
                bgcolor="lightcoral",
                content=ft.Column(
                    width=220,
                    height=200,
                    spacing=12,
                    controls=[
                        ft.Text("Horizontal START", size=20, weight=ft.FontWeight.W_600),
                        ft.Text("Review pull requests"),
                        ft.Text("Ship release"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.START
                )
            ),
            ft.Container(
                bgcolor="lightpink",
                content=ft.Column(
                    width=220,
                    height=200,
                    spacing=12,
                    controls=[
                        ft.Text("Horizontal CENTER", size=20, weight=ft.FontWeight.W_600),
                        ft.Text("Review pull requests"),
                        ft.Text("Ship release"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ),
            ft.Container(
                bgcolor="lightgray",
                content=ft.Column(
                    width=220,
                    height=200,
                    spacing=12,
                    controls=[
                        ft.Text("Horizontal END", size=20, weight=ft.FontWeight.W_600),
                        ft.Text("Review pull requests"),
                        ft.Text("Ship release"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.END
                )
            ),
            ft.Container(
                bgcolor="lavender",
                content=ft.Column(
                    width=220,
                    height=200,
                    spacing=12,
                    controls=[
                        ft.Text("Horizontal STRETCH", size=20, weight=ft.FontWeight.W_600),
                        ft.Text("Review pull requests"),
                        ft.Text("Ship release"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH
                )
            ),
        ],
        spacing=20
    )

    # Place everything in one page
    page.add(
        ft.Row(
            controls=[vertical_start, vertical_center, vertical_end],
            spacing=20
        ),
        horizontal_row
    )

ft.app(target=main)
