const WEB_APP_URL = "https://script.google.com/macros/s/AKfycbzCWQOW4QXTCnYZmxf3BiJaCzlpMdalGxkkzwMxYairh38vkPf6CLh1g86locuoHP8MXg/exec"

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const id = urlParams.get('id');

if ('scrollRestoration' in history) {
    history.scrollRestoration = 'manual';
}

id == null || id == "" ? handleVerification() : ""
window.addEventListener('resize', handleOrientation)
window.addEventListener('orientationchange', handleOrientation)
const loadingPanel = document.getElementById('loading-panel');
loadingPanel.removeAttribute("hidden")

if (handleOrientation()) {
    disableScrolling()
    getGuestById(id);

    setTimeout(() => {
        loadingPanel.setAttribute("hidden", "");
    }, 2500);
}

document.getElementById('ScrollButton').addEventListener('click', function() {
    const music = document.getElementById("music")
    music.volume = 0.4
    music.play();
    document.body.style.overflowY = "unset"
    window.onscroll = function() {}

    setTimeout(() => {
        document.getElementById("SecondPage").scrollIntoView({ behavior: "smooth" });
    }, 100);
});

document.getElementById('BtnSubmit').addEventListener('click', function() {
    
});

function disableScrolling() {
    var x = window.scrollX;
    var y = window.scrollY;
    window.onscroll = function() {
        window.scrollTo(x, y);
    }
}

async function getGuestById(guestId) {
    const response = await fetch(`${WEB_APP_URL}?id=${guestId}`, {
        method: "GET",
        mode: "cors"
    });
    const data = await response.json();
    console.log(data);

    const GuestName = document.getElementById("GuestNameTextCover")
    GuestName.append(data.GuestName);

    const GuestInput = document.getElementById("GuestName")
    GuestInput.value = data.GuestName

    const ButtonSubmit = document.getElementById("BtnSubmit")
    data.Updated ? ButtonSubmit.setAttribute("hidden") : ""

    const MaximumGuest = data.GuestMaxAttendance
    const InputSelect = document.getElementById("GuestCounter")
    for (let i = 1; i <= MaximumGuest; i++) {
        const NewOption = new Option(i, i);
        InputSelect.add(NewOption);
    }

    if (data.error) {
        handleVerification()
    }
}

function CopyToClipboard(Button) {
    const ButtonValue = Button.value;

    navigator.clipboard.writeText(ButtonValue)
    .then(() => alert("Copied!"))
    .catch(err => alert("Failed: " + err));
}

function handleVerification() {
    document.body.innerHTML = '';

    const warning = document.createElement('div');
    warning.textContent = "⚠️ Who are you?!";
    warning.style.cssText = `
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        width: 100vw;
        text-align: center;
        font-family: sans-serif;
        font-size: 1.5rem;
        color: white;
        background: black;
        position: fixed;
        inset: 0;
        z-index: 9999;
    `;
    document.body.appendChild(warning);
}

function handleOrientation() {
    const isLandscape = window.innerWidth > window.innerHeight;
    if (isLandscape) {
        document.body.innerHTML = '';

        const warning = document.createElement('div');
        warning.textContent = "⚠️ Please rotate your device to portrait mode. Then refresh!";
        warning.style.cssText = `
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            width: 100vw;
            text-align: center;
            font-family: sans-serif;
            font-size: 1.5rem;
            color: white;
            background: black;
            position: fixed;
            inset: 0;
            z-index: 9999;
        `;
        document.body.appendChild(warning);

        return false
    }
    return true
}