import flet as ft

def main(page: ft.Page):
    page.title = "Styled Button Example"
    page.bgcolor = "#121212"
    page.padding = 50

    def on_click(e):
        result.value = "Button Clicked! 🚀"
        page.update()

    # Styled Button - use 'content' instead of 'text'
    btn = ft.ElevatedButton(
        content=ft.Text("Click Me", color="white"),  # Text goes here
        on_click=on_click,
        style=ft.ButtonStyle(
            bgcolor="#2196F3",
            padding=20,
            elevation=8,
            shape=ft.RoundedRectangleBorder(radius=12)
        )
    )

    # Result Text
    result = ft.Text(
        value="",
        size=18,
        color="white"
    )

    # Card Container
    card = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Styled Button Demo", size=22, weight="bold", color="white"),
                ft.Text("Click the button below:", color="white70"),
                btn,
                result
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=30,
        border_radius=20,
        bgcolor="#1E1E2E",
        shadow=ft.BoxShadow(
            blur_radius=20,
            color="black54",
            offset=ft.Offset(4, 4)
        )
    )

    page.add(card)

ft.run(main)