import reflex as rx
import python_links.utils as utils
from python_links.views.header import header
from python_links.views.links import links
import python_links.styles.styles as styles
from python_links.styles.styles import Size as Size
from python_links.styles.styles import Spacing as Spacing
from python_links.components.link_button import link_button

def projects_links() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Mis proyectos",
            size=Size.BIG.value
        ),
        #link_button(),

        width="100%",
        spacing=Spacing.DEFAULT.value,
    )