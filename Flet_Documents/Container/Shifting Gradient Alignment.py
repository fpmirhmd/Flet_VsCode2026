import flet as ft
import asyncio

def main(page: ft.Page):
    container = ft.Container(
        width=300,
        height=150,
        content=ft.Text("Shifting Gradient"),
        gradient=ft.LinearGradient(
            begin=ft.Alignment.TOP_LEFT,
            end=ft.Alignment.BOTTOM_RIGHT,
            colors=["#ff9a9e", "#fad0c4"]
        ),
        border_radius=20,
        alignment=ft.Alignment.CENTER
    )

    page.add(container)

    async def animate_alignment():  # <-- removed 'e'
        positions = [
            (ft.Alignment.TOP_LEFT, ft.Alignment.BOTTOM_RIGHT),
            (ft.Alignment.TOP_RIGHT, ft.Alignment.BOTTOM_LEFT),
            (ft.Alignment.BOTTOM_LEFT, ft.Alignment.TOP_RIGHT)
        ]
        i = 0
        while True:
            container.gradient.begin, container.gradient.end = positions[i % len(positions)]
            container.update()
            i += 1
            await asyncio.sleep(1)

    page.run_task(animate_alignment)

ft.run(main)  # <-- changed from ft.app() to ft.run()