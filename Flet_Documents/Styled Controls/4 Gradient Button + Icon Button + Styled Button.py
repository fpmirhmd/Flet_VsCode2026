import flet as ft

def main(page: ft.Page):
    page.title = "Gradient & Styled Buttons"
    page.bgcolor = "#121212"
    page.padding = 50

    # Click handlers
    def on_click(e):
        result.value = "Normal Button Clicked! 🚀"
        page.update()

    def on_icon_click(e):
        result.value = "Icon Button Clicked! ⭐"
        page.update()

    def on_gradient_click(e):
        result.value = "Gradient Button Clicked! 🔥"
        page.update()

    # Normal Styled Button
    btn = ft.ElevatedButton(
        content=ft.Text("Click Me", color="white"),
        # text="Click Me",
        on_click=on_click,
        style=ft.ButtonStyle(
            color="white",
            bgcolor="#2196F3",
            padding=20,
            elevation=8,
            shape=ft.RoundedRectangleBorder(radius=12)
        )
    )

    # Icon Button
    icon_btn = ft.IconButton(
        icon=ft.Icons.STAR,
        icon_color="#FFD700",
        icon_size=40,
        tooltip="Star Button",
        on_click=on_icon_click
    )

    # 🔥 Gradient Button (NEW)
    gradient_btn = ft.Container(
        content=ft.ElevatedButton(
            content=ft.Text("Gradient Button", color="black"),
            on_click=on_gradient_click,
            style=ft.ButtonStyle(
                color="white",
                padding=20,
                shape=ft.RoundedRectangleBorder(radius=12),
                elevation=10,
            ),
        ),
        width=200,
        height=60,
        alignment=ft.Alignment.CENTER,
        gradient=ft.LinearGradient(
            begin=ft.Alignment.TOP_LEFT,
            end=ft.Alignment.BOTTOM_RIGHT,
            colors=["#ff512f", "#dd2476"]
        ),
        border_radius=12,
        shadow=ft.BoxShadow(
            blur_radius=15,
            color="black45",
            offset=ft.Offset(4, 4)
        )
    )

    # Result text
    result = ft.Text(
        value="",
        size=18,
        color="white"
    )

    # UI Card
    card = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Modern Button UI", size=24, weight="bold", color="white"),
                ft.Text("Styled + Icon + Gradient Buttons", color="white70"),

                ft.Row(
                    controls=[btn, icon_btn],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=30
                ),

                ft.Container(height=10),

                gradient_btn,

                ft.Container(height=10),

                result
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=30,
        border_radius=20,
        bgcolor="#1E1E2E",
        shadow=ft.BoxShadow(
            blur_radius=25,
            color="black54",
            offset=ft.Offset(5, 5)
        )
    )

    page.add(card)

ft.run(main)