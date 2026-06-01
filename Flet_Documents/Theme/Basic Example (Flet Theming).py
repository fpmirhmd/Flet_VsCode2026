import flet as ft

def main(page: ft.Page):
    page.title = "Theming Example"

    # Apply theme
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLUE,
            secondary=ft.Colors.ORANGE
        )
    )

    page.dark_theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLUE_200
        )
    )

    # page.theme_mode = ft.ThemeMode.LIGHT  # or DARK
    page.theme_mode = ft.ThemeMode.DARK  # or DARK

    page.add(
        ft.Text("Hello Theming!", size=30),
        ft.ElevatedButton("Click Me")
    )

ft.run(main)