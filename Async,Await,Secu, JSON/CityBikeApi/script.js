async function chargerStations() {
    const reponse = await fetch("http://localhost:5191/api/stations");
    const donnees = await reponse.json();

    // Envoyer à la fonction d'affichage
    afficherStations(donnees);
}

function afficherStations(stations) {
    const listeStations = document.getElementById("liste-stations");

    listeStations.innerHTML = ""
    stations.forEach(station => {
        const carte = document.createElement("div");
        carte.classList.add("station-card");

        carte.innerHTML = `
            <h2>${station.nom}</h2>
            <p>Vélos disponibles : ${station.velosDisponibles}</p>
            <button onclick="louer(${station.id})">Louer</button>
            <button onclick="rendre(${station.id})">Rendre</button>
        `;

        listeStations.appendChild(carte);
    });
}

async function louer(id) {
    const reponse = await fetch(`http://localhost:5191/api/stations/${id}/louer`, {
        method: "POST"
    });
    if (reponse.ok) {
        alert("Vélo loué avec succès !");
        chargerStations();
    } else {
        alert("Erreur lors de la location : Plus de vélos ou station hors service.")
    }
}

async function rendre(id) {
    const reponse = await fetch(`http://localhost:5191/api/stations/${id}/rendre`, {
        method: "POST"
    });
    if (reponse.ok) {
        alert("Vélo rendu avec succès !");
        chargerStations();
    } else {
        alert("Erreur lors du retour : Station hors service ou déjà pleine.")
    }
}

chargerStations()