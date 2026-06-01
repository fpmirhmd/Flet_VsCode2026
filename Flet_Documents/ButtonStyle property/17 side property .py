import flet as ft

def main(page: ft.Page):
    page.add(
        ft.OutlinedButton(
            "Border Demo",
            style=ft.ButtonStyle(
                side={
                    ft.ControlState.DEFAULT: ft.BorderSide(2, ft.Colors.BLUE),
                    ft.ControlState.HOVERED: ft.BorderSide(3, ft.Colors.GREEN),
                    ft.ControlState.PRESSED: ft.BorderSide(4, ft.Colors.RED),
                },
                bgcolor=ft.Colors.WHITE,
                color=ft.Colors.BLACK,
                animation_duration=300
            ),
        )
    )

ft.run(main)
