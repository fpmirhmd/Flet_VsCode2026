import flet as ft


def main(page: ft.Page):
    page.title = "Modern Dashboard"
    page.bgcolor = "#0f172a"  # dark background
    page.padding = 0

    # -------------------------------
    # Sidebar (Left)
    # -------------------------------
    sidebar = ft.Container(
        width=220,
        bgcolor="#1e293b",
        padding=20,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Text("My App", size=22, weight="bold", color="white"),

                ft.Divider(color="white24"),

                ft.Text("Dashboard", color="white"),
                ft.Text("Analytics", color="white70"),
                ft.Text("Orders", color="white70"),
                ft.Text("Customers", color="white70"),
                ft.Text("Settings", color="white70"),
            ],
        ),
    )

    # -------------------------------
    # Header (Top Bar)
    # -------------------------------
    header = ft.Container(
        height=60,
        bgcolor="#1e293b",
        padding=ft.Padding.symmetric(horizontal=20),
        alignment=ft.Alignment.CENTER,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Dashboard", size=20, color="white", weight="bold"),
                ft.Row(
                    spacing=10,
                    controls=[
                        ft.Icon(ft.Icons.NOTIFICATIONS, color="white"),
                        ft.CircleAvatar(
                            content=ft.Text("M"),
                            bgcolor="#38bdf8"
                        )
                    ]
                )
            ]
        )
    )

    # -------------------------------
    # Card Component
    # -------------------------------
    def dashboard_card(title, value, color):
        return ft.Container(
            width=220,
            height=120,
            bgcolor="#1e293b",
            border_radius=15,
            padding=15,
            alignment=ft.Alignment.CENTER,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(title, color="white70"),
                    ft.Text(value, size=22, weight="bold", color=color),
                ]
            )
        )

    # -------------------------------
    # Cards Grid (Center Area)
    # -------------------------------
    cards = ft.Row(
        spacing=20,
        run_spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            dashboard_card("Revenue", "$12,500", "#22c55e"),
            dashboard_card("Orders", "320", "#38bdf8"),
            dashboard_card("Customers", "1,200", "#facc15"),
            dashboard_card("Growth", "+15%", "#f43f5e"),
        ]
    )

    # -------------------------------
    # Main Content Area
    # -------------------------------
    content = ft.Container(
        expand=True,
        padding=20,
        content=ft.Column(
            expand=True,
            controls=[
                header,
                ft.Container(height=20),
                cards,
            ]
        )
    )

    # -------------------------------
    # Layout (Row)
    # -------------------------------
    layout = ft.Row(
        expand=True,
        controls=[
            sidebar,
            content
        ]
    )

    page.add(layout)

ft.run(main)