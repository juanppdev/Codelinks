import reflex as rx
import python_links.styles.styles as styles
from python_links.pages.index import index
from python_links.pages.projects import projects
from firebase_config import firebase_db
import uuid

class State(rx.State):
    user_id: str = str(uuid.uuid4())

    def guardar_ubicacion(self, lat, lon):
        """Guarda la ubicación del usuario en Firebase."""
        firebase_db.child(self.user_id).set({
            "lat": lat,
            "lon": lon,
            "timestamp": rx.utils.time.now()
        })

    def eliminar_ubicacion(self):
        """Elimina la ubicación del usuario al salir de la web."""
        firebase_db.child(self.user_id).delete()

def obtener_ubicacion():
    return rx.script("""
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition((position) => {
                fetch("/guardar_ubicacion", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({
                        lat: position.coords.latitude,
                        lon: position.coords.longitude
                    })
                });

                window.addEventListener("beforeunload", () => {
                    fetch("/eliminar_ubicacion", { method: "POST" });
                });
            });
        }
    """)

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        obtener_ubicacion(),
        rx.el.script(
            src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6885891243934075",
            async_=True,
            crossorigin="anonymous"
        ),
        rx.script(src="/js/script.js")
    ]
)