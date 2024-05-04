import reflex as rx
import python_links.styles.styles as styles
from python_links.pages.index import index

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
