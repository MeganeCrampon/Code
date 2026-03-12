async function chargerStations() {
    const reponse = await fetch("http://localhost:5191/api/stations");
    const donnees = await reponse.json();

    afficherStations(donnees);
}

function afficherStations(stations) {
    const listeStations = document.getElementById("liste-stations");
    listeStations.innerHTML = ""; 

    stations.forEach(station => {
        // col-md-4 = 3 colonnes par ligne
        const col = document.createElement("div");
        col.className = "col-md-4"; 

        // Structure de "Card" Bootstrap
        col.innerHTML = `
            <div class="card h-100 shadow-sm">
                <div class="card-body text-center">
                    <h5 class="card-title fw-bold">${station.nom}</h5>
                    <p class="card-text">
                        <span class="badge ${station.velosDisponibles > 0 ? 'badge-dispo' : 'badge-attention'}">
                            ${station.velosDisponibles} vélos disponibles
                        </span>
                    </p>
                    <div class="d-grid gap-2 d-md-block">
                        <button onclick="louer(${station.id})" class="btn louer">Louer</button>
                        <button onclick="rendre(${station.id})" class="btn rendre">Rendre</button>
                    </div>
                </div>
            </div>
        `;

        listeStations.appendChild(col);
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