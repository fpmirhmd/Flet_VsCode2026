import flet as ft

def main(page: ft.Page):
    page.title = "Modern Dashboard UI"
    page.window.width = 1200
    page.window.height = 700
    page.padding = 0
    page.bgcolor = ft.Colors.GREY_100   # Set page background explicitly

    # ------------------ THEME ------------------
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLUE,
            secondary=ft.Colors.CYAN,
            surface=ft.Colors.WHITE,
        )
    )
    page.dark_theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLUE_200,
            surface=ft.Colors.GREY_900,
        )
    )
    page.theme_mode = ft.ThemeMode.LIGHT

    # ------------------ SIDEBAR ------------------
    sidebar = ft.Container(
        width=220,
        bgcolor=ft.Colors.BLUE,
        padding=20,
        content=ft.Column(
            [
                ft.Text("Dashboard", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Divider(color=ft.Colors.WHITE),
                ft.Text("Home", color=ft.Colors.WHITE),
                ft.Text("Analytics", color=ft.Colors.WHITE),
                ft.Text("Reports", color=ft.Colors.WHITE),
                ft.Text("Settings", color=ft.Colors.WHITE),
            ]
        )
    )

    # ------------------ HEADER ------------------
    header = ft.Container(
        height=60,
        padding=20,
        bgcolor=ft.Colors.WHITE,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text("Welcome Back 👋", size=20, weight=ft.FontWeight.BOLD),
                ft.Row(
                    [
                        ft.Icon(ft.Icons.NOTIFICATIONS),
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
                    ft.Text(title, color=ft.Colors.WHITE),
                    ft.Text(value, size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
                ]
            )
        )

    # ------------------ CARDS ------------------
    cards = ft.Row(
        spacing=20,
        controls=[
            dashboard_card("Users", "1,245", ft.Colors.BLUE),
            dashboard_card("Revenue", "$12,340", ft.Colors.GREEN),
            dashboard_card("Orders", "320", ft.Colors.ORANGE),
            dashboard_card("Growth", "+15%", ft.Colors.PURPLE),
        ]
    )

    # ------------------ CHART PLACEHOLDER ------------------
    chart = ft.Container(
        height=250,
        bgcolor=ft.Colors.WHITE,
        border_radius=15,
        padding=20,
        content=ft.Column(
            [
                ft.Text("Analytics Overview", size=18, weight=ft.FontWeight.BOLD),
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
        scroll=ft.ScrollMode.AUTO,
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