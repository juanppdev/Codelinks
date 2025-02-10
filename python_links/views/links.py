import reflex as rx
from python_links.components.link_button import link_button
from python_links.components.title import title
import python_links.constants as const
from python_links.routes import Route

def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        # link_button("Twitch", 
        #             "Directos de Lunes a viernes",
        #             "/icons/twitch.svg",
        #             const.TWITCH_URL,
        #             True
        #             ),
        link_button("Youtube", 
                    "Videos Semanales",
                    "/icons/youtube.svg",
                    const.YOUTUBE_URL,
                    True
                    ),
        link_button("Github",
                    "Mi perfil de Github",
                    "/icons/github.svg",
                    const.GITHUB_URL,
                    True
                    ),
        link_button("Discord",
                    "El chat de la comunidad",
                    "/icons/discord.svg",
                    const.DISCORD_URL,
                    True
                    ),
        title("Recursos y más"), # Recursos y más
        link_button("Dragon Ball Api", 
                    "Api de Dradon Ball",
                    "/icons/api.svg",
                    const.DRAGON_API,
                    True
                    ),
        link_button("Blog MundoCode", 
                    "Noticias y más",
                    "/icons/blog.svg",
                    const.BLOG,
                    True
                    ),
        link_button("Mis proyectos",
                    "Mis proyectos en Github",
                    "/icons/github.svg",
                    Route.PROJECTS.value,
                    False
                    ),
        title("Contacto"),
        link_button("Email", 
                    "juanppdev@mundocode.dev",
                    "/icons/email.svg",
                    "mailto:juanppdev@mundocode.dev",
                    False
                    ),
        link_button("Portafolio", 
                    "Aqui encontrás más información sobre mi",
                    "/icons/portfolio.svg",
                    const.PORTFOLIO,
                    True
                    ),
        width="100%",
        spacing="2"
    )