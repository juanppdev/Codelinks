import reflex as rx
import python_links.styles.styles as styles
from python_links.styles.colors import TextColor as TextColor
from python_links.styles.colors import Color as Color

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.chakra.span(
            title, 
            font_weight="bold", 
            color=Color.PRIMARY.value
        ),
        f" {body}",
        font_size=styles.Size.MEDIUM.value,
        color=TextColor.BODY.value
    )