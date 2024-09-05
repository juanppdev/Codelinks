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
                src="/perfil.jpg",
                name="Juanppdev",
                fallbac="JP", 
                size="7", 
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
                    color=Color.PRIMARY.value
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
                    spacing="4",
                    padding_top=Size.SMALL.value
                ),
                padding_top=Size.ZERO.value,
                align_items="start"
            ),
            align="end",
            spacing="4"
        ),
        rx.flex(
            info_text("+2", "Anos de Experiencia"),
            rx.spacer(),
            info_text("+1", "Aplicaciones creadas"),
            rx.spacer(),
            info_text("+5", "Seguidores"),
            width="100%",
        ),
        rx.text(
            "A los 25 años, descubrí mi pasión por la programación a través de la plataforma de aprendizaje Platzi mientras navegaba por la web. Desde entonces, me he inmerso en este mundo en constante evolución, explorando nuevas tecnologías y conceptos diariamente. Aunque mi enfoque inicial fue en la creación de páginas web, he ampliado mis horizontes explorando diferentes lenguajes y disciplinas.",
            color=TextColor.BODY.value,
            font_size=Size.DEFAULT.value,
        ),
        spacing="4",
        align_items="start",
        width="100%"
    )