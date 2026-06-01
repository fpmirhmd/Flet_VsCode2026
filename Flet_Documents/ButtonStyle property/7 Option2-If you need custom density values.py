import flet as ft

def main(page: ft.Page):
    page.add(
        ft.FilledButton(
            "Compact Button",
            style=ft.ButtonStyle(
                padding=ft.Padding.symmetric(horizontal=8, vertical=4)  # Tight padding
            ),
        ),
        ft.FilledButton(
            "Relaxed Button",
            style=ft.ButtonStyle(
                padding=ft.Padding.symmetric(horizontal=24, vertical=16)  # Loose padding
            ),
        ),
    )

ft.run(main)