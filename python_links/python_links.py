import reflex as rx
import python_links.styles.styles as styles
from python_links.pages.index import index
from python_links.pages.projects import projects

def location() -> rx.Component:
    return rx.script("""
    document.addEventListener('DOMContentLoaded', function() {
        // Firebase configuration 
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

        // Initialize Firebase
        firebase.initializeApp(firebaseConfig);
        const db = firebase.database();

        // Rest of your code...
        let userId = localStorage.getItem("userId");
        if (!userId) {
            userId = Math.random().toString(36).substring(2, 9);
            localStorage.setItem("userId", userId);
        }
        
        function enviarUbicacion() {
            if ("geolocation" in navigator) {
                navigator.geolocation.getCurrentPosition(async (position) => {
                    const userRef = firebase.database().ref("usuarios/" + userId);
                    
                    let country = "Desconocido";
                    try {
                        const response = await fetch("https://ipinfo.io/json?token=7ce6f02ebdc5a2");
                        const data = await response.json();
                        country = data.country || "Desconocido";
                    } catch (error) {
                        console.error("Error obteniendo país:", error);
                    }

                    userRef.set({
                        lat: position.coords.latitude,
                        lon: position.coords.longitude,
                        country: country,
                        timestamp: Date.now(),
                    });

                    window.addEventListener("beforeunload", () => {
                        userRef.remove();
                    });
                }, async () => {
                    try {
                        const response = await fetch("https://ipinfo.io/json?token=7ce6f02ebdc5a2");
                        const data = await response.json();
                        const [lat, lon] = data.loc.split(",").map(Number);
                        const country = data.country || "Desconocido";

                        const userRef = firebase.database().ref("usuarios/" + userId);
                        userRef.set({ lat, lon, country, timestamp: Date.now() });

                        window.addEventListener("beforeunload", () => {
                            userRef.remove();
                        });
                    } catch (error) {
                        console.error("Error con ubicación por IP:", error);
                    }
                });
            }
        }

        enviarUbicacion();
    });
    """)

def scripts() -> rx.Component:
    return rx.script(src="https://unpkg.com/leaflet/dist/leaflet.js")

app = rx.App(
    stylesheets=[
        "https://unpkg.com/leaflet/dist/leaflet.css"
    ],
    style=styles.BASE_STYLE,
    head_components=[
        # Load Firebase SDK first
        rx.script(src="https://www.gstatic.com/firebasejs/9.6.1/firebase-app-compat.js", strategy="beforeInteractive"),
        rx.script(src="https://www.gstatic.com/firebasejs/9.6.1/firebase-database-compat.js", strategy="beforeInteractive"),
        # Then Leaflet
        #scripts(),
        # Then your custom script
        #location(),
        # Other scripts last
        rx.el.script(
            src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6885891243934075",
            async_=True,
            crossorigin="anonymous"
        )
    ]
)