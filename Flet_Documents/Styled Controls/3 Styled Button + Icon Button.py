import flet as ft

def main(page: ft.Page):
    page.title = "Styled Buttons with Icon"
    page.bgcolor = "#121212"
    page.padding = 50

    def on_click(e):
        result.value = "Regular Button Clicked! 🚀"
        page.update()

    def on_icon_click(e):
        result.value = "Icon Button Clicked! ⭐"
        page.update()

    # Styled Elevated Button
    btn = ft.ElevatedButton(
        content=ft.Text("Click Me", color="white"),
        on_click=on_click,
        style=ft.ButtonStyle(
            color="white",
            bgcolor="#2196F3",
            padding=20,
            elevation=8,
            shape=ft.RoundedRectangleBorder(radius=12)
        )
    )

    # Icon Button (NEW)
    icon_btn = ft.IconButton(
        icon=ft.Icons.STAR,
        icon_color="#FFD700",
        icon_size=40,
        tooltip="Star Button",
        on_click=on_icon_click
    )

    # Result text
    result = ft.Text(
        value="",
        size=18,
        color="white"
    )

    # Card UI
    card = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Styled Button + Icon Button", size=22, weight="bold", color="white"),
                ft.Text("Try both buttons below:", color="white70"),

                ft.Row(
                    controls=[
                        btn,
                        icon_btn
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30
                ),

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