import flet as ft

def main(page: ft.Page):
    page.title = "My APK App"
    page.add(
        ft.Text("Hello from Android!", size=24, weight=ft.FontWeight.BOLD),
        ft.ElevatedButton("Click Me", on_click=lambda e: print("Clicked!"))
    )
ft.run(main)