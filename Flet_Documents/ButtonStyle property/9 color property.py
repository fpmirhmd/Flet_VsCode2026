import flet as ft

def main(page: ft.Page):
    page.add(
        ft.FilledButton(
            "Styled Text",
            style=ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.YELLOW},
                color={
                    ft.ControlState.DEFAULT: ft.Colors.BLACK,
                    ft.ControlState.HOVERED: ft.Colors.WHITE,
                    ft.ControlState.FOCUSED: ft.Colors.BLUE,
                    ft.ControlState.PRESSED: ft.Colors.RED,
                },
                animation_duration=300
            ),
        )
    )

ft.app(target=main)
