import flet as ft

def main(page: ft.Page):
    page.add(
        ft.FilledButton(
            "Animated Button",
            style=ft.ButtonStyle(
                bgcolor={ft.ControlState.DEFAULT: ft.Colors.BLUE,
                         ft.ControlState.FOCUSED: ft.Colors.PINK_200},
                elevation={"": 1, ft.ControlState.PRESSED: 0},
                shape={
                    ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=4),
                    ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                },
                animation_duration=500  # half a second transition
            ),
        )
    )

ft.run(main)
