import reflex as rx
import python_links.styles.styles as styles
from python_links.pages.index import index
from python_links.pages.projects import projects
from firebase_config import firebase_db
import uuid
import requests

def location():
    return rx.script("""import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js";
    import { getDatabase, ref, set, remove, onValue } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-database.js";

    // 🔥 Configuración de Firebase
    const firebaseConfig = {
      apiKey: "AIzaSyDSYTe-2TXdxzRfkAXmN9e9XehEx22ZwT0",
      authDomain: "webinteractive-8464a.firebaseapp.com",
      databaseURL: "https://webinteractive-8464a-default-rtdb.europe-west1.firebasedatabase.app",
      projectId: "webinteractive-8464a",
      storageBucket: "webinteractive-8464a.appspot.com",
      messagingSenderId: "608396654816",
      appId: "1:608396654816:web:8b458c37d636c4e16f7885",
      measurementId: "G-GJK7WMW8ZH"
    };

    // Inicializar Firebase
    const app = initializeApp(firebaseConfig);
    const db = getDatabase(app);

    // 📍 Obtener o generar un userId persistente
    let userId = localStorage.getItem("userId");
    if (!userId) {
      userId = Math.random().toString(36).substring(2, 9);
      localStorage.setItem("userId", userId);
    }
    
    // 📍 Obtener ubicación del usuario
    function enviarUbicacion() {
      if ("geolocation" in navigator) {
        navigator.geolocation.getCurrentPosition(async (position) => {
          const userRef = ref(db, "usuarios/" + userId);
          
          // Obtener país desde la IP
          let country = "Desconocido";
          try {
            const response = await fetch("https://ipinfo.io/json?token=7ce6f02ebdc5a2");
            const data = await response.json();
            country = data.country || "Desconocido";
          } catch (error) {
            console.error("Error obteniendo país:", error);
          }

          set(userRef, {
            lat: position.coords.latitude,
            lon: position.coords.longitude,
            country: country,
            timestamp: Date.now(),
          });

          // Eliminar usuario al salir
          window.addEventListener("beforeunload", () => {
            remove(userRef);
          });
        }, async () => {
          // Si el usuario bloquea la ubicación, usar IP
          try {
            const response = await fetch("https://ipinfo.io/json?token=7ce6f02ebdc5a2");
            const data = await response.json();
            const [lat, lon] = data.loc.split(",").map(Number);
            const country = data.country || "Desconocido";

            const userRef = ref(db, "usuarios/" + userId);
            set(userRef, { lat, lon, country, timestamp: Date.now() });

            window.addEventListener("beforeunload", () => {
              remove(userRef);
            });
          } catch (error) {
            console.error("Error obteniendo ubicación por IP:", error);
          }
        });
      }
    }
    enviarUbicacion();""",type="module")

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src="https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js", type="module"),
        rx.script(src="https://www.gstatic.com/firebasejs/9.6.1/firebase-database.js", type="module"),
        location(),
        # otros componentes...
        rx.el.script(
            src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6885891243934075",
            async_=True,
            crossorigin="anonymous"
        )
    ]
)