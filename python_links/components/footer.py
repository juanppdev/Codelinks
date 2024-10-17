import reflex as rx
import datetime
from python_links.styles.styles import Size as Size
from python_links.styles.colors import TextColor as TextColor
from python_links.styles.colors import Color as Color
import python_links.constants as const
from python_links.components.ant_components import float_button

def footer() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.image(
                src="MundoCode.png",
                height=Size.VERY_BIG.value,
                width=Size.VERY_BIG.value
            ),
            rx.link(
                rx.box(
                    f"© 2024-{datetime.date.today().year} ",
                    rx.chakra.span("Juanppdev by MundoCode", color=Color.PRIMARY.value),
                    " v1.",
                    padding_top=Size.DEFAULT.value
                ),
                href="",
                is_external=True,
                font_size=Size.MEDIUM.value
            ),
            rx.hstack(
                rx.link(
                    rx.image(
                        src="icons/github.svg",
                        height=Size.DEFAULT.value,
                        width=Size.DEFAULT.value
                    ),
                    href=const.REPOSITORY_URL,
                    is_external=True
                ),
                rx.text(
                    "BUILDING SOFTWARE WITH ♥ FROM STADE TO THE WORLD.",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                )
            ),
            float_button(),
            align="center",
            margin_bottom=Size.BIG.value,
            padding_bottom=Size.BIG.value,
            padding_x= Size.BIG.value,
            spacing="0",
            color=TextColor.FOOTER.value
        )
    )