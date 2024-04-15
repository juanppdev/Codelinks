import reflex as rx
import python_links.styles.styles as styles

def title(title: str) -> rx.Component:
    return rx.heading(
        title,
        size= "7",
        style=styles.title_style
    )