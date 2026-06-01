import flet as ft

def main(page: ft.Page):
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.GREEN,
            error=ft.Colors.RED,
        ),
    )
    page.title = "Flet Theme Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    txt_name = ft.TextField(label="Enter your name", width=300)
    
    btn_submit = ft.ElevatedButton(
        content=ft.Text("Submit"),
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE,
            bgcolor=page.theme.color_scheme.primary,
        ),
        on_click=lambda e: page.add(
            ft.Text(
                f"Hello, {txt_name.value}!", 
                color=page.theme.color_scheme.primary
            )
        )
    )
    
    page.add(txt_name, btn_submit)

ft.app(target=main)