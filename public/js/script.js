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