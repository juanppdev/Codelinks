import reflex as rx
import python_links.styles.styles as styles
from python_links.pages.index import index
from python_links.pages.projects import projects
from firebase_config import firebase_db
import uuid
import requests

class State(rx.State):
    user_id: str = str(uuid.uuid4())

    def guardar_ubicacion(self, lat, lon, country):
        """Guarda la ubicación del usuario en Firebase."""
        firebase_db.child(self.user_id).set({
            "lat": lat,
            "lon": lon,
            "country": country,
            "timestamp": rx.utils.time.now()
        })

    def eliminar_ubicacion(self):
        """Elimina la ubicación del usuario al salir de la web."""
        firebase_db.child(self.user_id).delete()


def obtener_ubicacion():
    return rx.script("""
        async function getLocation() {
            let lat = null, lon = null, country = "Desconocido";

            function guardarUbicacion() {
                fetch("/guardar_ubicacion", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ lat, lon, country })
                });

                window.addEventListener("beforeunload", () => {
                    fetch("/eliminar_ubicacion", { method: "POST" });
                });
            }

            // Intentar obtener la ubicación por GPS
            if ("geolocation" in navigator) {
                navigator.geolocation.getCurrentPosition(
                    async (position) => {
                        lat = position.coords.latitude;
                        lon = position.coords.longitude;

                        // Obtener país desde la IP
                        try {
                            const response = await fetch("https://ipinfo.io/json?token=TU_TOKEN");
                            const data = await response.json();
                            country = data.country || "Desconocido";
                        } catch (error) {
                            console.error("Error al obtener el país:", error);
                        }

                        guardarUbicacion();
                    },
                    async () => {
                        // Si el usuario deniega la geolocalización, usar IP
                        try {
                            const response = await fetch("https://ipinfo.io/json?token=TU_TOKEN");
                            const data = await response.json();
                            [lat, lon] = data.loc.split(",").map(Number);
                            country = data.country || "Desconocido";
                        } catch (error) {
                            console.error("Error al obtener ubicación por IP:", error);
                        }

                        guardarUbicacion();
                    }
                );
            }
        }

        getLocation();
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