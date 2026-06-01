import flet as ft


def main(page: ft.Page):
    page.title = "Auto Update Example"
    
    def add_many_items(e):
        ft.context.disable_auto_update()  # disable auto-update to improve performance
        
        for i in range(100):
            page.controls.append(ft.Text(f"Item {i}")) 
            
        page.update()  # manually trigger a single update after adding all items
     
     
    page.controls.append(ft.Button("Add many items", on_click=add_many_items))

    
if __name__ == "__main__":
    # ft.app(main)
    ft.run(main)
    