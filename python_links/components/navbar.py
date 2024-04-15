import reflex as rx
from python_links.styles.styles import Size as Size
import python_links.styles.styles as styles
from python_links.styles.colors import Color as Color
from python_links.styles.colors import TextColor as TextColor

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.chakra.span("Juanpp", color=Color.PRIMARY.value),
            rx.chakra.span("dev", color=Color.SECONDARY.value),
            style=styles.navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )