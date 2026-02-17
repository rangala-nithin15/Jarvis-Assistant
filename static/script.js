let waveInterval;

function activate() {
    const consoleBox = document.getElementById("console");
    consoleBox.innerHTML += "<br>> Initializing JARVIS...";

    startWave();

    fetch('/activate', { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        consoleBox.innerHTML += "<br>> " + data.status;
        consoleBox.innerHTML += "<br>> Voice Systems Online";
    });
}

function startWave() {
    const bars = document.querySelectorAll(".waveform span");

    waveInterval = setInterval(() => {
        bars.forEach(bar => {
            const randomHeight = Math.floor(Math.random() * 40) + 10;
            bar.style.height = randomHeight + "px";
        });
    }, 200);
}

function stopWave() {
    clearInterval(waveInterval);
}

