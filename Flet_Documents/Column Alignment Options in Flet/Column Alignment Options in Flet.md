**In Flet, you control column alignment using the `alignment` and `horizontal_alignment` properties of `ft.Column`.** Vertical alignment is handled with `MainAxisAlignment` (e.g., `START`, `CENTER`, `END`), while horizontal alignment is controlled with `CrossAxisAlignment` (e.g., `START`, `CENTER`, `END`). This lets you position child controls precisely inside a column. [Flet](https://flet.dev/docs/controls/column/) [Stack Overflow](https://stackoverflow.com/questions/76656285/python-flet-vertical-alignment-for-column-of-controls)

* * *

🔑 Column Alignment Options in Flet
-----------------------------------

### Vertical Alignment (`alignment`)

* **MainAxisAlignment.START** → Aligns children at the top of the column.
* **MainAxisAlignment.CENTER** → Centers children vertically.
* **MainAxisAlignment.END** → Pushes children to the bottom.
* **MainAxisAlignment.SPACE_BETWEEN** → Evenly distributes children with space between.
* **MainAxisAlignment.SPACE_AROUND** → Equal spacing around each child.
* **MainAxisAlignment.SPACE_EVENLY** → Equal spacing between all children and edges.

### Horizontal Alignment (`horizontal_alignment`)

* **CrossAxisAlignment.START** → Aligns children to the left.
* **CrossAxisAlignment.CENTER** → Centers children horizontally.
* **CrossAxisAlignment.END** → Aligns children to the right.
* **CrossAxisAlignment.STRETCH** → Stretches children to fill the width.

* * *

📘 Example Code
---------------

```py
import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Column(
            controls=[
                ft.Text("Top aligned"),
                ft.Text("Centered horizontally"),
                ft.Text("Bottom aligned"),
            ],
            height=300,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,   # vertical alignment
            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # horizontal alignment
        )
    )

ft.app(main)
```

This example distributes text vertically with space between and centers them horizontally.

* * *

⚠️ Common Pitfalls
------------------

* **No height set** → Alignment won’t work properly unless the column has enough space (`height` or `expand=True`).
* **Confusing `alignment` vs `horizontal_alignment`** → `alignment` is vertical (main axis), `horizontal_alignment` is horizontal (cross axis).
* **Nested containers** → Sometimes you need to set alignment inside `ft.Container` as well for precise positioning. [Stack Overflow](https://stackoverflow.com/questions/76656285/python-flet-vertical-alignment-for-column-of-controls)

* * *

#### Properties

* [`alignment`](https://flet.dev/docs/controls/column/?utm_source=copilot.com#flet.Column.alignment) - How the child Controls should be placed vertically.
* [`controls`](https://flet.dev/docs/controls/column/?utm_source=copilot.com#flet.Column.controls) - A list of controls to display.
* [`horizontal_alignment`](https://flet.dev/docs/controls/column/?utm_source=copilot.com#flet.Column.horizontal_alignment) - Defines how the [`controls`](https://flet.dev/docs/controls/column#flet.Column.controls) should be placed horizontally.
* [`intrinsic_width`](https://flet.dev/docs/controls/column/?utm_source=copilot.com#flet.Column.intrinsic_width) - If `True`, the Column will be as wide as the widest child control.
* [`run_alignment`](https://flet.dev/docs/controls/column/?utm_source=copilot.com#flet.Column.run_alignment) - How the runs should be placed in the cross-axis when [`wrap`](https://flet.dev/docs/controls/column#flet.Column.wrap) is `True`.
* [`run_spacing`](https://flet.dev/docs/controls/column/?utm_source=copilot.com#flet.Column.run_spacing) - The spacing between runs when [`wrap`](https://flet.dev/docs/controls/column#flet.Column.wrap) is `True`.
* [`spacing`](https://flet.dev/docs/controls/column/?utm_source=copilot.com#flet.Column.spacing) - Spacing between the `controls`.
* [`tight`](https://flet.dev/docs/controls/column/?utm_source=copilot.com#flet.Column.tight) - Determines how vertical space is allocated.
* [`wrap`](https://flet.dev/docs/controls/column/?utm_source=copilot.com#flet.Column.wrap) - Whether the [`controls`](https://flet.dev/docs/controls/column#flet.Column.controls) should wrap into additional columns (runs) when they don't fit in a single vertical column.





Would you like me to show you a **visual diagram of column alignment options** (top, center, bottom, stretch) so you can see how they look in practice?


