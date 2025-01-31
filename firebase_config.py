import firebase_admin
from firebase_admin import credentials, db

# Cargar credenciales de Firebase
cred = credentials.Certificate("firebase_credentials.json")  # Usa tu archivo JSON
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://webinteractive-8464a-default-rtdb.europe-west1.firebasedatabase.app"
})

# Obtener referencia a la base de datos
firebase_db = db.reference("usuarios")
