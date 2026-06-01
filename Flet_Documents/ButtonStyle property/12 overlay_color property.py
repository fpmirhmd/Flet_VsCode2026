import flet as ft

def main(page: ft.Page):
    page.add(
        ft.FilledButton(
            "Overlay Demo",
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.YELLOW,
                color=ft.Colors.BLACK,
                overlay_color={
                    ft.ControlState.HOVERED: ft.Colors.GREEN_200,
                    ft.ControlState.FOCUSED: ft.Colors.PINK_100,
                    ft.ControlState.PRESSED: ft.Colors.BLUE_100,
                },
                animation_duration=300
            ),
        )
    )

ft.run(main)
