const socket = io("https://mapacode.vercel.app/");

  function sendLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        socket.emit("sendLocation", {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        });
      });
    }
  }

  window.addEventListener("load", sendLocation);
  window.addEventListener("beforeunload", () => {
    socket.disconnect();
  });