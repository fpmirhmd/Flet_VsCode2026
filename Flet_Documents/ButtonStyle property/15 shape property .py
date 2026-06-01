import flet as ft

def main(page: ft.Page):
    page.add(
        ft.FilledButton(
            "Rounded",
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),
                bgcolor=ft.Colors.BLUE,
                color=ft.Colors.WHITE,
            ),
        ),
        ft.FilledButton(
            "Stadium",
            style=ft.ButtonStyle(
                shape=ft.StadiumBorder(),
                bgcolor=ft.Colors.GREEN,
                color=ft.Colors.WHITE,
            ),
        ),
        ft.FilledButton(
            "Circle",
            style=ft.ButtonStyle(
                shape=ft.CircleBorder(),
                bgcolor=ft.Colors.RED,
                color=ft.Colors.WHITE,
            ),
        ),
    )

ft.app(target=main)
