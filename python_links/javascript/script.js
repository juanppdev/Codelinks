document.addEventListener('DOMContentLoaded', () => {
    // Obtiene la localización mediante ipinfo.io
    fetch('https://ipinfo.io/json?token=7ce6f02ebdc5a2')
        .then(response => response.json())
        .then(data => {
            const [lat, lng] = data.loc.split(',');

            // Envía la ubicación al servidor Node.js en mapacode.vercel.app
            fetch('https://mapacode.vercel.app/api/locations', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    lat: parseFloat(lat),
                    lng: parseFloat(lng),
                    country: data.country,
                    id: data.ip // Usamos la IP como identificador único
                })
            }).then(response => {
                if (response.ok) {
                    console.log('Ubicación enviada correctamente');
                } else {
                    console.error('Error al enviar la ubicación');
                }
            }).catch(error => {
                console.error('Error en la solicitud fetch:', error);
            });
        })
        .catch(error => {
            console.error('Error al obtener la localización:', error);
        });
});
