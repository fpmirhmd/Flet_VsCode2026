import flet as ft

def main(page: ft.Page):
    page.add(
        ft.FilledButton(
            "Padded Button",
            style=ft.ButtonStyle(
                padding={
                    ft.ControlState.DEFAULT: 10,   # uniform padding
                    ft.ControlState.HOVERED: 20,   # more space when hovered
                    ft.ControlState.PRESSED: (5, 2, 5, 2),  # custom sides
                },
                bgcolor=ft.Colors.YELLOW,
                color=ft.Colors.BLACK,
                animation_duration=300
            ),
        )
    )

ft.run(main)
