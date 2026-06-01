import flet as ft

def main(page: ft.Page):
    page.add(
        ft.FilledButton(
            "Elevated Button",
            style=ft.ButtonStyle(
                elevation={
                    ft.ControlState.DEFAULT: 2,   # normal shadow
                    ft.ControlState.HOVERED: 6,   # stronger shadow when hovered
                    ft.ControlState.PRESSED: 0,   # flat when pressed
                },
                animation_duration=300  # smooth transition
            ),
        )
    )

ft.run(main)
