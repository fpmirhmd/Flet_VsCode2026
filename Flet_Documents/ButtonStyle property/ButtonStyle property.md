**In Flet, the `ButtonStyle` property lets you fully customize the look and behavior of buttons — including background color, text/icon color, shape, padding, borders, shadows, and even state-specific styles (hovered, focused, disabled, etc.).** It provides granular control over how a button appears and reacts to user interaction.  [Flet](https://flet.dev/docs/types/buttonstyle/)  [Github](https://github.com/flet-dev/flet/blob/main/website/docs/types/buttonstyle.md)  

---

## 🔑 Key Properties of `ButtonStyle`
- **alignment** – Controls content alignment inside the button.  
- **animation_duration** – Duration (ms) for animated changes in shape/elevation.  
- **bgcolor** – Background fill color (can vary by state).  
- **color** – Text and icon color.  
- **elevation** – Material elevation (shadow depth).  
- **icon_color** & **icon_size** – Customize icon appearance.  
- **overlay_color** – Highlight color when hovered, focused, or pressed.  
- **padding** – Space between button boundary and content.  
- **shadow_color** – Shadow color of the button.  
- **shape** – Defines button shape (rounded, stadium, circle, beveled, etc.).  
- **side** – Border outline style.  
- **text_style** – Font style for text inside the button.  
- **visual_density** – Controls how compact the button layout is.  [Flet](https://flet.dev/docs/types/buttonstyle/)  

---

## 🎨 Example Usage
```python
import flet as ft

def main(page: ft.Page):
    page.add(
        ft.FilledButton(
            "Styled Button",
            style=ft.ButtonStyle(
                color={
                    ft.ControlState.HOVERED: ft.Colors.WHITE,
                    ft.ControlState.FOCUSED: ft.Colors.BLUE,
                    ft.ControlState.DEFAULT: ft.Colors.BLACK,
                },
                bgcolor={
                    ft.ControlState.FOCUSED: ft.Colors.PINK_200,
                    "": ft.Colors.YELLOW,
                },
                padding={ft.ControlState.HOVERED: 20},
                overlay_color=ft.Colors.TRANSPARENT,
                elevation={"pressed": 0, "": 1},
                animation_duration=500,
                side={
                    ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.BLUE),
                    ft.ControlState.HOVERED: ft.BorderSide(2, ft.Colors.BLUE),
                },
                shape={
                    ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                    ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=2),
                },
            ),
        )
    )

ft.app(target=main)
```
This example shows **different colors, padding, borders, and shapes depending on button state**.  [Github](https://github.com/flet-dev/flet/blob/main/website/docs/types/buttonstyle.md)  

---

## ⚠️ Notes & Limitations
- Some properties (like `animation_duration`) may behave differently depending on button type (e.g., `TextButton` vs `IconButton`).  [Stack Overflow](https://stackoverflow.com/questions/76912507/python-flet-buttonstyle-animation-duration-dont-affect-iconbuttons-color)  
- You can set **global styles** (applied to all states) or **state-specific styles** using dictionaries keyed by `ControlState`.

---

Would you like me to show a **visual comparison of button shapes** (stadium, rounded rectangle, circle, etc.) using Flet’s `ButtonStyle`? That could make the customization options clearer.