import flet as ft

def main(page: ft.Page):
    page.add(
        ft.FilledButton(
            "Beveled Button",
            style=ft.ButtonStyle(
                shape=ft.BeveledRectangleBorder(radius=8),
                bgcolor=ft.Colors.ORANGE,
                color=ft.Colors.WHITE,
                elevation=4,
                shadow_color=ft.Colors.BLUE_GREY,
            ),
        )
    )

ft.run(main)
