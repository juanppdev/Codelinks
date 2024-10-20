import reflex as rx
import datetime
from python_links.components.link_icon import link_icon
from python_links.components.info_text import info_text
from python_links.styles.styles import Size as Size
from python_links.styles.styles import Spacing as Spacing
from python_links.styles.colors import TextColor as TextColor
from python_links.styles.colors import Color as Color
from python_links.styles.fonts import Font as Font
import python_links.constants  as const

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
                rx.avatar(
                    name="Juanppdev",
                    size=Spacing.MEDIUM_BIG.value,
                    src="/perfil.jpg",
                    radius="full",
                    color=TextColor.BODY.value,
                    bg=Color.CONTENT.value,
                    padding="2px",
                    border=f"4px solid {Color.PRIMARY.value}"
                ),
            rx.vstack(
                rx.heading(
                    "Juan Pablo",
                    size=Size.BIG.value
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
                spacing=Spacing.ZERO.value,
                align_items="start"
            ),
            align="end",
            spacing=Spacing.DEFAULT.value
        ),
            rx.vstack(
                rx.flex(
                    info_text(
                        f"{experience()}+",
                        "años de experiencia"
                    ),
                    rx.spacer(),
                    info_text(
                        "1+", "aplicaciones creadas"
                    ),
                    rx.spacer(),
                    info_text(
                        "5+", "seguidores"
                    ),
                    width="100%"
                ),
                rx.text(
                    "A los 20 años, descubrí mi pasión por la programación a través de la plataforma de aprendizaje Platzi mientras navegaba por la web. Desde entonces, me he inmerso en este mundo en constante evolución, explorando nuevas tecnologías y conceptos diariamente. Aunque mi enfoque inicial fue en la creación de páginas web, he ampliado mis horizontes explorando diferentes lenguajes y disciplinas.",
                    font_size=Size.DEFAULT.value,
                    color=TextColor.BODY.value
                ),
                width="100%",
                spacing=Spacing.BIG.value
        ),
        width="100%",
        spacing=Spacing.BIG.value,
        align_items="start",
    )


def experience() -> int:
    return datetime.date.today().year - 2022