import flet as ft

def main(page: ft.Page):
    page.add(
        ft.IconButton(
            icon=ft.Icons.FAVORITE,
            style=ft.ButtonStyle(
                icon_color={
                    ft.ControlState.DEFAULT: ft.Colors.RED,
                    ft.ControlState.HOVERED: ft.Colors.PINK,
                    ft.ControlState.FOCUSED: ft.Colors.BLUE,
                    ft.ControlState.PRESSED: ft.Colors.GREEN,
                },
                icon_size=30,
                animation_duration=300
            ),
        )
    )

ft.run(main)
