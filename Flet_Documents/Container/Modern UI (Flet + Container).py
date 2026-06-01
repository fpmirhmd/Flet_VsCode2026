import flet as ft

def main(page: ft.Page):
    page.title = "Modern Dashboard UI"
    page.bgcolor = "#f5f7fb"
    page.padding = 0

    # ---------- Sidebar ----------
    sidebar = ft.Container(
        width=220,
        bgcolor="#1e293b",
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text("My App", size=22, weight="bold", color="white"),
                ft.Divider(color="white24"),

                ft.Text("Dashboard", color="white"),
                ft.Text("Customers", color="white54"),
                ft.Text("Reports", color="white54"),
                ft.Text("Settings", color="white54"),
            ],
            spacing=15
        )
    )

    # ---------- Header ----------
    header = ft.Container(
        height=60,
        bgcolor="white",
        padding=ft.Padding.symmetric(horizontal=20),
        content=ft.Row(
            alignment="spaceBetween",
            vertical_alignment="center",
            controls=[
                ft.Text("Dashboard", size=20, weight="bold"),
                ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.NOTIFICATIONS),  # <-- FIXED: ft.Icons (capital I)
                        ft.CircleAvatar(content=ft.Text("M"))
                    ]
                )
            ]
        )
    )

    # ---------- Card Component ----------
    def dashboard_card(title, value, color):
        return ft.Container(
            width=200,
            height=120,
            bgcolor=color,
            border_radius=15,
            padding=15,
            content=ft.Column(
                alignment="spaceBetween",
                controls=[
                    ft.Text(title, color="white"),
                    ft.Text(value, size=24, weight="bold", color="white"),
                ]
            )
        )

    # ---------- Cards Row ----------
    cards = ft.Row(
        spacing=20,
        controls=[
            dashboard_card("Total Sales", "$12,500", "#3b82f6"),
            dashboard_card("Customers", "1,240", "#10b981"),
            dashboard_card("Orders", "320", "#f59e0b"),
            dashboard_card("Revenue", "$8,430", "#ef4444"),
        ]
    )

    # ---------- Main Content ----------
    content = ft.Container(
        expand=True,
        padding=20,
        content=ft.Column(
            controls=[
                header,
                ft.Container(height=20),  # spacer
                cards,
            ]
        )
    )

    # ---------- Layout ----------
    layout = ft.Row(
        expand=True,
        controls=[
            sidebar,
            content
        ]
    )

    page.add(layout)

ft.app(target=main)