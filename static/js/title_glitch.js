(function () {
    const word = document.querySelector(".title-glitch");

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