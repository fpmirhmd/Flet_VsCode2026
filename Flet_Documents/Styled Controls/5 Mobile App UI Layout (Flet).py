import flet as ft

def main(page: ft.Page):
    page.title = "Mobile App UI"
    page.bgcolor = "#121212"
    page.padding = 0
    page.window_width = 360
    page.window_height = 640

    # Result text
    result = ft.Text("", color="white")

    # Click handler
    def on_click(e):
        # result.value = f"{e.control.text} clicked!"
        result.value = f"You clicked: {e.control.content.value}"
        page.update()

    # 🔷 Top App Bar
    appbar = ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(ft.Icons.MENU, color="white"),
                ft.Text("My App", size=20, weight="bold", color="white"),
                ft.Icon(ft.Icons.NOTIFICATIONS, color="white"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        padding=15,
        bgcolor="#1E1E2E"
    )

    # 🔷 Gradient Header
    header = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Welcome Back 👋", size=22, weight="bold", color="white"),
                ft.Text("Explore your dashboard", color="white70"),
            ]
        ),
        padding=20,
        gradient=ft.LinearGradient(
            colors=["#6C63FF", "#48C6EF"]
        ),
        border_radius=ft.BorderRadius.only(
            bottom_left=20,
            bottom_right=20
        )
    )

    # 🔷 Card Function
    def card(title, subtitle):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(title, size=18, weight="bold", color="white"),
                    ft.Text(subtitle, color="white70"),
                ]
            ),
            padding=15,
            bgcolor="#1E1E2E",
            border_radius=15,
            shadow=ft.BoxShadow(blur_radius=10, color="black54"),
            width=300
        )

    # 🔷 Buttons
    btn1 = ft.ElevatedButton(
        content=ft.Text("Start", color="white"),
        on_click=on_click,
        style=ft.ButtonStyle(
            bgcolor="#6C63FF",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=10)
        )
    )

    btn2 = ft.ElevatedButton(
        content=ft.Text("Settings", color="white"),
        on_click=on_click,
        style=ft.ButtonStyle(
            bgcolor="#03DAC6",
            color="black",
            shape=ft.RoundedRectangleBorder(radius=10)
        )
    )

    # 🔷 Bottom Navigation
    bottom_nav = ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(ft.Icons.HOME, color="white"),
                ft.Icon(ft.Icons.SEARCH, color="white54"),
                ft.Icon(ft.Icons.PERSON, color="white54"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        ),
        padding=15,
        bgcolor="#1E1E2E"
    )

    # 🔷 Main Layout
    page.add(
        ft.Column(
            controls=[
                appbar,
                header,

                ft.Container(height=10),

                ft.Column(
                    controls=[
                        card("Profile", "View your profile"),
                        card("Analytics", "Check your data"),
                        card("Messages", "Read messages"),
                    ],
                    spacing=15,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),

                ft.Container(height=10),

                ft.Row(
                    controls=[btn1, btn2],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                ),

                result,

                ft.Container(expand=True),  # push bottom nav down

                bottom_nav
            ],
            expand=True
        )
    )

ft.run(main)