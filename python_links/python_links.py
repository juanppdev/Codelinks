import reflex as rx
from python_links.components.navbar import navbar
from python_links.components.footer import footer
from python_links.views.header.header import header
from python_links.views.links.links import links
import python_links.styles.styles as styles
from python_links.styles.styles import Size as Size

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )




app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Juanppdev | Aprendiendo cada dia juntos"
)