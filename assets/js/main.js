const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const id = urlParams.get('id');

console.log(id)

var modal = document.getElementById("CashlessModal");
var span = document.getElementsByClassName("close")[0];

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

if ('scrollRestoration' in history) {
    history.scrollRestoration = 'manual';
}

window.addEventListener("load", () => {
    if (!sessionStorage.getItem("hasScrolled")) {
        document.getElementById("FirstPage").scrollIntoView({ behavior: "smooth" });
        sessionStorage.setItem("hasScrolled", "true");

        const Path = `assets/python/GenerateFiles/guests/${id}.json`
        console.log(Path)

        fetch(Path)
        .then(response => response.json())
        .then(data => {
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
        })
        .catch(error => console.error('Error loading JSON:', error));
    }
});

document.getElementById('ScrollButton').addEventListener('click', function() {
    const music = document.getElementById("music")
    music.volume = 0.4
    music.play();
    document.body.style.overflowY = "scroll"
    document.getElementsByClassName("wrapper")[0].setAttribute("scroll-snap-type", "y mandatory")

    setTimeout(() => {
        document.getElementById("SecondPage").scrollIntoView({ behavior: "smooth" });
    }, 100);
});

document.getElementById('BtnCashless').addEventListener('click', function() {
    modal.style.display = "block"
});

document.getElementById('BtnSubmit').addEventListener('click', function() {

});

function CopyToClipboard(Button) {
    const ButtonValue = Button.value;

    navigator.clipboard.writeText(ButtonValue)
    .then(() => alert("Copied!"))
    .catch(err => alert("Failed: " + err));
}