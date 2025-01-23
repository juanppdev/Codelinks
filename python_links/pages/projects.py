import reflex as rx
import python_links.utils as utils
from python_links.components.navbar import navbar
from python_links.components.footer import footer
from python_links.routes import Route
from python_links.views.header import header
from python_links.views.links import links
import python_links.styles.styles as styles
from python_links.styles.styles import Size as Size
from python_links.views.projects_links import projects_links

@rx.page(
        route= Route.PROJECTS.value,
        title=utils.projects_title,
        description=utils.projects_description,
        meta=utils.projects_meta
)
def projects() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(False),
                # links(),
                projects_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )