import reflex as rx
from python_links.components.link_button import link_button
from python_links.components.title import title
import python_links.constants as const

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Twitch", 
                    "Directos de Lunes a viernes",
                    "/icons/twitch.svg",
                    const.TWITCH_URL,
                    ),
        link_button("Youtube", 
                    "Videos Semanales",
                    "/icons/youtube.svg",
                    const.YOUTUBE_URL),
        link_button("Github",
                    "Mi perfil de Github",
                    "/icons/github.svg",
                    const.GITHUB_URL),
        link_button("Discord",
                    "El chat de la comunidad",
                    "/icons/discord.svg",
                    const.DISCORD_URL),
        title("Recursos y más"), # Recursos y más
        link_button("Dragon Ball Api", 
                    "Api de Dradon Ball",
                    "/icons/api.svg",
                    const.DRAGON_API,
                    ),
        link_button("Blog MundoCode", 
                    "Noticias y más",
                    "/icons/blog.svg",
                    const.BLOG,
                    ),
        title("Contacto"),
        link_button("Email", 
                    "juanppdev@gmail.com",
                    "/icons/email.svg",
                    "mailto:juanppdev@gmail.com",
                    ),
        width="100%",
        spacing="2"
    )