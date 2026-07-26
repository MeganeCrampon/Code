const form = document.getElementById("compatibilityForm");
const name1Input = document.getElementById("name1");
const name2Input = document.getElementById("name2");
const result = document.getElementById("compatibilityResult");

form.addEventListener('submit', (event) => {
    event.preventDefault();
    const name1 = name1Input.value.trim().toLowerCase();
    const name2 = name2Input.value.trim().toLowerCase();
    const names = [name1, name2].sort();
    const combinaison = names[0] + names[1];
    
    let lettersSum = 0;
    for (let l = 0; l < combinaison.length; l++) {
        lettersSum += combinaison.charCodeAt(l);
    }
    
    const percentage = lettersSum % 101;

    let message;

    if (percentage === 0) {
        message = `Oublie, c'est mort. Passe à autre chose...`;
        launchFireworks("💀");
    } else if (percentage < 10) {
        message = `Euh...gênant, c'est pas gagné...`;
        launchFireworks("😬");
    } else if ( percentage < 20) {
        message = `Y'a vraiment très peu de chance mais bon, peut-être avec la force du désespoir hein...`;
        launchFireworks("🥺");
    } else if (percentage < 30) {
        message = `Peut-être que ça peut marcher mais bon, faut pas trop rêver non plus...`;
        launchFireworks("😅");
    } else if (percentage < 40) {
        message = `En vrai si tu farm quelques années ça peut passer !`;
        launchFireworks("🙃");
    } else if (percentage < 50) {
        message = `C'est pas trop mal barré, ça peut marcher avec de la patience !`;
        launchFireworks("🙂");
    } else if (percentage < 60) {
        message = `Franchement ça peut marcher, faut juste pas être trop pressé !`;
        launchFireworks("😉");
    }  else if (percentage < 70) {
        message = `Eh pas mal du tout, c'est bien parti !`;
        launchFireworks("😊");
    } else if (percentage < 80) {
        message = `Ouah c'est sur la bonne voie, y'a moyen que ça marche !`;
        launchFireworks("😇");
    } else if (percentage < 90) {
        message = `Mais carrément, prend ton courage à deux mains et va déclarer ta flamme !`;
        launchFireworks("🥰");
    } else if (percentage < 100) {
        message = `C'est la réussite assurée, fonce c'est le destin !`;
        launchFireworks("😍");
    } else {
        message =  `Vous êtes faits pour être ensemble, c'est un vrai coup de foudre assuré !`;
        launchFireworks("💖");
    }

    result.textContent = `La compatibilité entre ${capitalize(name1)} et ${capitalize(name2)} est de ${percentage}%. ${message}`;
});

function capitalize(word) {
    return word.charAt(0).toUpperCase() + word.slice(1);
}

function launchFireworks(emoji) {
    const fireworkdsDiv = document.createElement('div');
    fireworkdsDiv.classList.add('emoji-burst');
    document.body.appendChild(fireworkdsDiv);
    
    const rect1 = name1Input.getBoundingClientRect();
    const rect2 = name2Input.getBoundingClientRect();
    const centerX = (rect1.left + rect1.right + rect2.left + rect2.right) / 4;
    const centerY = Math.min(rect1.top, rect2.top) - 20; // un peu au-dessus des inputs

    for (let i = 0; i < 60; i++) {
        const emojiParticle = document.createElement('span');
        emojiParticle.textContent = emoji;
        emojiParticle.classList.add('emoji-particle');

        emojiParticle.style.left = `${centerX}px`;
        emojiParticle.style.top = `${centerY}px`;

        const angle = Math.random() * 2 * Math.PI;
        const distance = 250 + Math.random() * 300;

        const tx = Math.cos(angle) * distance;
        const ty = Math.sin(angle) * distance;

        emojiParticle.style.setProperty("--tx-end", `${tx}px`);
        emojiParticle.style.setProperty("--ty-end", `${ty}px`);
        emojiParticle.style.setProperty("--tx-start", `${tx * 0.3}px`);
        emojiParticle.style.setProperty("--ty-start", `${ty * 0.3}px`);
        emojiParticle.style.setProperty("--rot-start", `${Math.random() * 360}deg`);
        emojiParticle.style.setProperty("--rot-end", `${Math.random() * 720 - 360}deg`);

        fireworkdsDiv.appendChild(emojiParticle);
    }

    setTimeout(() => {
        fireworkdsDiv.remove();
    }, 1700);
}