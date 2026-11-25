/**
 * Inicialização base do mapa Leaflet.js + OpenStreetMap.
 *
 * SPRINT 1 - PASSO 2 (Historieta 2):
 * ORIENTAÇÃO: Carregar os pinos de /api/incidents/ filtrados pelo bounding box
 * atual do mapa e exibir popups com botões de validação comunitária.
 */

document.addEventListener("DOMContentLoaded", () => {
    const mapElement = document.getElementById("map");
    if (!mapElement || typeof L === "undefined") {
        return;
    }

    // Coordenadas iniciais centradas em Brasília (UnB)
    const map = L.map("map").setView([-15.7636, -47.8703], 13);

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: "&copy; OpenStreetMap contributors",
    }).addTo(map);
});
