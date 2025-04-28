import reflex as rx
import python_links.utils as utils
from python_links.components.navbar import navbar
from python_links.components.footer import footer
from python_links.routes import Route
from python_links.views.header import header
from python_links.views.links import links
import python_links.styles.styles as styles
from python_links.styles.styles import Size as Size

@rx.page(
        route= Route.INDEX.value,
        title=utils.index_title,
        description=utils.index_description,
        meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        rx.el.noscript(
            rx.el.iframe(
                src="https://www.googletagmanager.com/ns.html?id=GTM-M3WH6QJX",
                height="0",
                width="0",
                style={"display": "none", "visibility": "hidden"}
            )
        ),
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(True),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer(),
    )