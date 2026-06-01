import flet as ft

def main(page: ft.Page):
    page.title = "Color Opacity in Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30

    # Method 1: Using ft.Colors.with_opacity() (Recommended)
    # 0.0 = fully transparent, 1.0 = fully opaque
    semi_red = ft.Colors.with_opacity(0.5, ft.Colors.RED)

    # Method 2: Hex string with alpha channel (AARRGGBB)
    # 80 hex = ~50% opacity, FF0000 = pure red
    semi_blue_hex = "#800000FF"

    # Method 3: Container-level opacity (applies to the entire control)
    # This affects everything inside: background color, child controls, borders, etc.
    
    page.add(
        ft.Text("Color Opacity Examples", size=24, weight=ft.FontWeight.BOLD),
        ft.Divider(height=20),

        # Solid color (no opacity) for comparison
        ft.Container(
            content=ft.Text("Solid Red (100%)", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.RED,
            padding=20,
            border_radius=10,
            width=300,
            alignment=ft.Alignment.CENTER,
        ),
        ft.Divider(height=5, color=ft.Colors.TRANSPARENT),

        # Method 1: Built-in color with opacity
        ft.Container(
            content=ft.Text("50% Red via with_opacity()", color=ft.Colors.WHITE),
            bgcolor=semi_red,
            padding=20,
            border_radius=10,
            width=300,
            alignment=ft.Alignment.CENTER,
        ),
        ft.Divider(height=5, color=ft.Colors.TRANSPARENT),

        # Method 2: Hex string with alpha
        ft.Container(
            content=ft.Text("50% Blue via Hex Alpha", color=ft.Colors.WHITE),
            bgcolor=semi_blue_hex,
            padding=20,
            border_radius=10,
            width=300,
            alignment=ft.Alignment.CENTER,
        ),
        ft.Divider(height=5, color=ft.Colors.TRANSPARENT),

        # Method 3: Container opacity property
        # This makes the ENTIRE container (bg + text + borders) 50% opaque
        ft.Container(
            content=ft.Text("50% Container Opacity", color=ft.Colors.WHITE),
            bgcolor=ft.Colors.GREEN,
            padding=20,
            border_radius=10,
            width=300,
            opacity=0.5,  # <-- applies to the whole control
            alignment=ft.Alignment.CENTER,
        ),
        ft.Divider(height=5, color=ft.Colors.TRANSPARENT),

        # Overlay demo: Two containers on top of each other
        # Shows how semi-transparent colors blend with backgrounds
        ft.Stack(
            height=120,
            width=300,
            controls=[
                # Background image or color
                ft.Container(
                    bgcolor=ft.Colors.YELLOW,
                    border_radius=10,
                    expand=True,
                ),
                # Transparent overlay on top
                ft.Container(
                    bgcolor=ft.Colors.with_opacity(0.4, ft.Colors.PURPLE),
                    border_radius=10,
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Text(
                        "Purple 40% over Yellow",
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                ),
            ],
        ),
    )

ft.run(main)