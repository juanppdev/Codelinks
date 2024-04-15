import reflex as rx
from python_links.components.link_icon import link_icon
from python_links.components.info_text import info_text
from python_links.styles.styles import Size as Size
from python_links.styles.colors import TextColor as TextColor
from python_links.styles.colors import Color as Color
from python_links.styles.fonts import Font as Font
import python_links.constants  as const

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/Perfil.jpg",
                name="Juanppdev",
                fallbac="JP", 
                size="8", 
                radius="full",
                padding="2px",
                border="4px solid",
                border_color=Color.PRIMARY.value
            ),
            rx.vstack(
                rx.heading(
                    "Juan Pablo",
                    size= "7",
                ),
                rx.text(
                    "@Juanppdev",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon(
                        "icons/x-twitter.svg",
                        const.X_URL,
                    ),
                    link_icon(
                        "icons/github.svg",
                        const.GITHUB_URL
                    ),
                    link_icon(
                        "icons/instagram.svg",
                        const.INSTAGRAM_URL
                    ),
                    link_icon(
                        "icons/tiktok.svg",
                        const.TIKTOK_URL
                    ),
                    link_icon(
                        "icons/linkedin.svg",
                        const.LINKEDIN_URL
                    ),
                    spacing="4"
                ),
                align_items="start",
            ),
            spacing="4"
        ),
        rx.flex(
            info_text("+13", "Anos de Experiencia"),
            rx.spacer(),
            info_text("+13", "Anos de Experiencia"),
            rx.spacer(),
            info_text("+13", "Anos de Experiencia"),
            width="100%",
        ),
        rx.text(
            "Soy Ingeniero de Software",
            color=TextColor.BODY.value,
            font_size=Size.DEFAULT.value,
        ),
        spacing="4",
        align_items="start",
        width="100%"
    )