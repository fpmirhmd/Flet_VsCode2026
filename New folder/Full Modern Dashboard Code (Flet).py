import flet as ft

def main(page: ft.Page):
    page.title = "Modern Dashboard UI"
    page.window_width = 1200
    page.window_height = 700
    page.padding = 0

    # ------------------ THEME ------------------
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.BLUE,
            secondary=ft.colors.CYAN,
            background=ft.colors.GREY_100,
            surface=ft.colors.WHITE
        )
    )

    page.dark_theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.BLUE_200,
            background=ft.colors.BLACK,
            surface=ft.colors.GREY_900
        )
    )

    page.theme_mode = ft.ThemeMode.LIGHT

    # ------------------ SIDEBAR ------------------
    sidebar = ft.Container(
        width=220,
        bgcolor=ft.colors.BLUE,
        padding=20,
        content=ft.Column(
            [
                ft.Text("Dashboard", size=22, weight="bold", color="white"),
                ft.Divider(color="white"),
                ft.Text("Home", color="white"),
                ft.Text("Analytics", color="white"),
                ft.Text("Reports", color="white"),
                ft.Text("Settings", color="white"),
            ]
        )
    )

    # ------------------ HEADER ------------------
    header = ft.Container(
        height=60,
        padding=20,
        bgcolor=ft.colors.WHITE,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text("Welcome Back 👋", size=20, weight="bold"),
                ft.Row(
                    [
                        ft.Icon(ft.icons.NOTIFICATIONS),
                        ft.CircleAvatar(content=ft.Text("A"))
                    ]
                )
            ]
        )
    )

    # ------------------ CARD FUNCTION ------------------
    def dashboard_card(title, value, color):
        return ft.Container(
            width=250,
            height=120,
            bgcolor=color,
            border_radius=15,
            padding=15,
            content=ft.Column(
                [
                    ft.Text(title, color="white"),
                    ft.Text(value, size=28, weight="bold", color="white")
                ]
            )
        )

    # ------------------ CARDS ------------------
    cards = ft.Row(
        wrap=True,
        spacing=20,
        controls=[
            dashboard_card("Users", "1,245", ft.colors.BLUE),
            dashboard_card("Revenue", "$12,340", ft.colors.GREEN),
            dashboard_card("Orders", "320", ft.colors.ORANGE),
            dashboard_card("Growth", "+15%", ft.colors.PURPLE),
        ]
    )

    # ------------------ CHART PLACEHOLDER ------------------
    chart = ft.Container(
        height=250,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        padding=20,
        content=ft.Column(
            [
                ft.Text("Analytics Overview", size=18, weight="bold"),
                ft.Divider(),
                ft.Text("📊 Chart Placeholder (you can integrate real charts)")
            ]
        )
    )

    # ------------------ MAIN CONTENT ------------------
    content = ft.Column(
        [
            header,
            cards,
            chart
        ],
        expand=True,
        scroll="auto"
    )

    # ------------------ LAYOUT ------------------
    page.add(
        ft.Row(
            [
                sidebar,
                ft.Container(
                    expand=True,
                    padding=20,
                    content=content
                )
            ],
            expand=True
        )
    )

ft.app(target=main)