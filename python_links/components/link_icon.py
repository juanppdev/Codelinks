import reflex as rx
from python_links.styles.styles import Size as Size

def link_icon(image: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.DEFAULT.value
        ),
        href= url,
        is_external=True
    )