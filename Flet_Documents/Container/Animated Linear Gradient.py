import flet as ft
import asyncio

def main(page: ft.Page):
    container = ft.Container(
        width=300,
        height=150,
        content=ft.Text("Animated Gradient", color="white", weight="bold"),
        gradient=ft.LinearGradient(
            begin=ft.Alignment.TOP_LEFT,
            end=ft.Alignment.BOTTOM_RIGHT,
            colors=["#ff9a9e", "#fad0c4"]
        ),
        border_radius=20,
        alignment=ft.Alignment.CENTER
    )

    page.add(container)

    # ✅ Remove 'e' parameter - run_task() passes no arguments
    async def animate_gradient():
        colors_list = [
            ["#ff9a9e", "#fad0c4"],
            ["#a1c4fd", "#c2e9fb"],
            ["#fbc2eb", "#a6c1ee"]
        ]
        i = 0
        while True:
            container.gradient.colors = colors_list[i % len(colors_list)]
            await container.update_async()
            i += 1
            await asyncio.sleep(1)

    # ✅ Now this works - no arguments passed, none expected
    page.run_task(animate_gradient)

ft.app(main)