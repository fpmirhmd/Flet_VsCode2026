import flet as ft

def main(page: ft.Page):
    # Apply theme with semi-transparent red as primary
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.with_opacity(0.5, ft.Colors.RED),
            error=ft.Colors.RED,
        ),
    )

    page.title = "Flet Colors with Opacity Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # TextField for input
    txt_input = ft.TextField(label="Type something", width=300)

    # ElevatedButton now uses 'content' instead of 'text'
    btn_show = ft.ElevatedButton(
        content=ft.Text("Show Text", color=ft.Colors.WHITE),
        bgcolor=page.theme.color_scheme.primary,
        on_click=lambda e: page.add(
            ft.Text(f"You typed: {txt_input.value}", color=page.theme.color_scheme.primary)
        )
    )

    # Add controls to page
    page.add(txt_input, btn_show)

# Run the app
ft.app(target=main)
