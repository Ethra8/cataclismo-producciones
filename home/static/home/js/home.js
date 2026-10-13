const serviceCheckboxes = document.querySelectorAll('input[name="services"]');
const messageField = document.getElementById("message");

function updateMessageRequired() {
    const serviceSelected = [...serviceCheckboxes].some((checkbox) => checkbox.checked);
    messageField.required = !serviceSelected;
}

serviceCheckboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", updateMessageRequired);
});

messageField.addEventListener("input", updateMessageRequired);

updateMessageRequired();



(function () {
    const word = document.querySelector(".digital-glitch");

    if (!word) return;

    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

    function triggerGlitch() {
        word.classList.add("is-glitching");

        setTimeout(function () {
            word.classList.remove("is-glitching");
        }, 120);

        setTimeout(triggerGlitch, 500 + Math.random() * 900);
    }

    triggerGlitch();
})();