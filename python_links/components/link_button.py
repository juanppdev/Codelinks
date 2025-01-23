import reflex as rx
import python_links.styles.styles as styles
from python_links.styles.styles import Size as Size

def link_button(title: str, body: str, image: str, url: str, external: bool) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.LARGE.value,
                    height=Size.LARGE.value,
                    margin=Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(
                        title,
                        style = styles.button_title_style
                    ),
                    rx.text(
                        body,
                        style = styles.button_body_style
                    ),
                    align_items="start",
                    spacing="0",
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value
                ),
                width="100%"
            )
        ),
        href=url,
        is_external=external,
        width="100%"
    )