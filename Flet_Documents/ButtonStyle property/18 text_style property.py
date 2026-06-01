import flet as ft

def main(page: ft.Page):
    page.add(
        ft.FilledButton(
            "Styled Text",
            style=ft.ButtonStyle(
                text_style={
                    ft.ControlState.DEFAULT: ft.TextStyle(size=16, weight=ft.FontWeight.BOLD),
                    ft.ControlState.HOVERED: ft.TextStyle(size=18, italic=True, color=ft.Colors.BLUE),
                    ft.ControlState.PRESSED: ft.TextStyle(size=16, decoration=ft.TextDecoration.UNDERLINE),
                },
                bgcolor=ft.Colors.YELLOW,
                animation_duration=300
            ),
        )
    )

ft.app(target=main)
