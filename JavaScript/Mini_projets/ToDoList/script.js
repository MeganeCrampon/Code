const input = document.getElementById('taskInput');
const addBtn = document.getElementById('addBtn');
const taskList = document.getElementById('taskList');

addBtn.addEventListener('click', () => {
    if (input.value !== "") {
        const list = document.createElement('list');
        const conteneurTexte = document.createElement('div'); // Le bloc de 150px
        conteneurTexte.className = "conteneur-texte";

        const texteTache = document.createElement('span');
        texteTache.textContent = input.value;

        // BARRER
        texteTache.addEventListener('click', () => {
        texteTache.classList.toggle('termine');
        });

        const btnSupp = document.createElement('button');
        btnSupp.textContent = "Supprimer";
        btnSupp.className = "btnSupp";
        
        btnSupp.addEventListener('click', () => {
            list.remove();
        });

        list.appendChild(texteTache);
        list.appendChild(conteneurTexte);
        list.appendChild(btnSupp);
        taskList.appendChild(list);

        input.value = "";
    }
});

input.addEventListener('keydown', (event) => {
    if (event.key === "Enter") {
        addBtn.click(); // Cela simule un clic !
    }
});