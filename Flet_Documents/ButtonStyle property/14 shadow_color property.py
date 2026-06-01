import flet as ft

def main(page: ft.Page):
    page.add(
        ft.FilledButton(
            "Shadow Demo",
            style=ft.ButtonStyle(
                elevation={
                    ft.ControlState.DEFAULT: 4,
                    ft.ControlState.HOVERED: 8,
                },
                shadow_color={
                    ft.ControlState.DEFAULT: ft.Colors.BLUE_GREY,
                    ft.ControlState.HOVERED: ft.Colors.PINK,
                },
                bgcolor=ft.Colors.YELLOW,
                color=ft.Colors.BLACK,
                animation_duration=300
            ),
        )
    )

ft.run(main)
