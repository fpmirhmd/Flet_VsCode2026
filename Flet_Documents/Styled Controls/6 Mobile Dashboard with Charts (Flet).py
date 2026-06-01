import flet as ft
import flet.canvas as cv

def main(page: ft.Page):
    page.title = "Dashboard UI"
    page.bgcolor = "#121212"
    page.padding = 0
    page.window_width = 360
    page.window_height = 640

    # 🔷 AppBar
    appbar = ft.Container(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.MENU, color="white"),
                ft.Text("Dashboard", color="white", size=20, weight="bold"),
                ft.Icon(ft.Icons.NOTIFICATIONS, color="white"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        padding=15,
        bgcolor="#1E1E2E"
    )

    # 🔷 Header
    header = ft.Container(
        content=ft.Column(
            [
                ft.Text("Welcome 👋", size=22, weight="bold", color="white"),
                ft.Text("Your performance overview", color="white70"),
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

    # 🔷 Stat Card
    def stat_card(title, value, color):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(title, color="white70"),
                    ft.Text(value, size=20, weight="bold", color="white"),
                ]
            ),
            padding=15,
            bgcolor=color,
            border_radius=15,
            width=150
        )

    stats = ft.Row(
        [
            stat_card("Sales", "$12K", "#1E1E2E"),
            stat_card("Users", "1.2K", "#1E1E2E"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    # 🔷 Custom Line Chart using Canvas
    data_points = [(0, 3), (1, 5), (2, 4), (3, 7), (4, 6)]
    chart_width = 300
    chart_height = 180
    padding = 30
    
    # Scale points to canvas
    max_y = 8
    x_step = (chart_width - 2 * padding) / (len(data_points) - 1)
    y_scale = (chart_height - 2 * padding) / max_y
    
    scaled_points = [
        (
            padding + i * x_step,
            chart_height - padding - y * y_scale
        )
        for i, (x, y) in enumerate(data_points)
    ]

    # Draw grid lines
    grid_lines = []
    for i in range(5):
        y = padding + i * (chart_height - 2 * padding) / 4
        grid_lines.append(
            cv.Line(
                x1=padding, y1=y,
                x2=chart_width - padding, y2=y,
                paint=ft.Paint(color="white12", stroke_width=1)
            )
        )

    # Build path elements list using cv.Path.MoveTo and cv.Path.LineTo
    path_elements = [
        cv.Path.MoveTo(scaled_points[0][0], scaled_points[0][1])
    ]
    for x, y in scaled_points[1:]:
        path_elements.append(cv.Path.LineTo(x, y))

    chart_canvas = cv.Canvas(
        [
            *grid_lines,
            cv.Path(
                elements=path_elements,
                paint=ft.Paint(
                    color="#6C63FF",
                    stroke_width=3,
                    style=ft.PaintingStyle.STROKE
                )
            ),
            # Draw points
            *[
                cv.Circle(
                    x, y, 4,
                    paint=ft.Paint(color="#6C63FF")
                )
                for x, y in scaled_points
            ]
        ],
        width=chart_width,
        height=chart_height
    )

    chart_card = ft.Container(
        content=ft.Column(
            [
                ft.Text("Analytics", size=18, weight="bold", color="white"),
                ft.Container(
                    content=chart_canvas,
                    alignment=ft.Alignment.CENTER
                )
            ]
        ),
        padding=15,
        bgcolor="#1E1E2E",
        border_radius=15,
        margin=10
    )

    # 🔷 Bottom Navigation
    bottom_nav = ft.Container(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.HOME, color="white"),
                ft.Icon(ft.Icons.BAR_CHART, color="white54"),
                ft.Icon(ft.Icons.SETTINGS, color="white54"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        ),
        padding=15,
        bgcolor="#1E1E2E"
    )

    # 🔷 Layout
    page.add(
        ft.Column(
            [
                appbar,
                header,
                ft.Container(height=10),
                stats,
                chart_card,
                ft.Container(expand=True),
                bottom_nav
            ],
            expand=True
        )
    )

ft.run(main)