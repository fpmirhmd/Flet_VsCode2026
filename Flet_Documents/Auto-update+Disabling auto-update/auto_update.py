import flet as ft


def main(page: ft.Page):
    page.title = "Auto Update Example"
    
    def button_click(e):
        page.controls.append(ft.Text("Button clicked!"))
        # no need to call page.update() — it happens automatically
        
    page.controls.append(ft.Button("Click me", on_click=button_click))
    # no need to call page.update() here either
      
    
if __name__ == "__main__":
    ft.app(main)
    