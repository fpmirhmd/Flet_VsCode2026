import flet as ft

def main(page: ft.Page):
    page.add(
        ft.FilledButton(
            "Colorful Button",
            style=ft.ButtonStyle(
                bgcolor={
                    ft.ControlState.DEFAULT: ft.Colors.YELLOW,
                    ft.ControlState.HOVERED: ft.Colors.GREEN,
                    ft.ControlState.FOCUSED: ft.Colors.PINK_200,
                    ft.ControlState.PRESSED: ft.Colors.BLUE,
                },
                color=ft.Colors.BLACK,  # text color
                animation_duration=300
            ),
        )
    )

ft.app(target=main)
