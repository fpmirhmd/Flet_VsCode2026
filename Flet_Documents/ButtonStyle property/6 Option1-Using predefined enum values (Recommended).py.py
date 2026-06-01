import flet as ft

def main(page: ft.Page):
    page.add(
        ft.FilledButton(
            "Compact Button",
            style=ft.ButtonStyle(
                visual_density=ft.VisualDensity.COMPACT  # Predefined compact density
            ),
        ),
        ft.FilledButton(
            "Relaxed Button",
            style=ft.ButtonStyle(
                visual_density=ft.VisualDensity.COMFORTABLE  # Default/relaxed
            ),
        ),
    )

ft.app(target=main)



'''
Available ft.VisualDensity enum values:
ft.VisualDensity.STANDARD (default)
ft.VisualDensity.COMPACT (denser)
ft.VisualDensity.COMFORTABLE (more spacious)
ft.VisualDensity.ADAPTIVE_PLATFORM_DENSITY
'''