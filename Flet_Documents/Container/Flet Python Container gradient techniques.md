In **Flet Python**, `Container` supports **gradient backgrounds** that let you create smooth color transitions for stylish UI designs. These gradient techniques can be applied using `LinearGradient` or `RadialGradient`.

---

## 🔹 Gradient Techniques in Container

- **Linear Gradient**  
  - Creates a transition between colors along a straight line.  
  - You can define `begin` and `end` points (e.g., `top_left` → `bottom_right`).  
  - Supports multiple colors for multi-step blends.

- **Radial Gradient**  
  - Colors radiate outward from a center point.  
  - Great for circular or spotlight effects.  
  - You can control the radius and focal alignment.

- **Multi-Color Blends**  
  - Both gradient types support more than two colors.  
  - Example: `colors=["#ff9a9e", "#fad0c4", "#fbc2eb"]`.

- **Transparency Layers**  
  - Colors can include alpha values (e.g., `"rgba(255,0,0,0.5)"`) for semi-transparent gradients.  
  - Useful for overlays and layered effects.

---

## 🔹 Example: Linear Gradient
```python
import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            width=250,
            height=120,
            content=ft.Text("Linear Gradient"),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#ff9a9e", "#fad0c4", "#fbc2eb"]
            ),
            alignment=ft.alignment.center,
            border_radius=15
        )
    )

ft.app(target=main)
```

---

## 🔹 Example: Radial Gradient
```python
import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Container(
            width=250,
            height=120,
            content=ft.Text("Radial Gradient"),
            gradient=ft.RadialGradient(
                center=ft.Alignment.CENTER,
                radius=1.0,
                colors=["#a1c4fd", "#c2e9fb"]
            ),
            alignment=ft.Alignment.CENTER,
            border_radius=15
        )
    )

ft.app(main)

```

---

## 🔹 Visual Inspiration
Here’s how different gradient techniques might look when applied to containers:





---

Would you like me to expand on **layered gradient effects** (combining gradients with shadows and borders) or focus on **multi-color blending** for more vibrant designs?