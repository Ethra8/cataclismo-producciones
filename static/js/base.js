document.querySelectorAll(".message-close").forEach((button) => {
    button.addEventListener("click", () => {
        button.closest(".message").remove();
    });
});

document.querySelectorAll(".message").forEach((message) => {
    setTimeout(() => {
        message.remove();
    }, 10000);
});


const dropdown = document.querySelector(".nav-dropdown");
const toggle = document.querySelector(".nav-dropdown-toggle");

toggle?.addEventListener("click", () => {
    const isOpen = dropdown.classList.toggle("open");
    toggle.setAttribute("aria-expanded", isOpen);
});

document.addEventListener("click", (event) => {
    if (dropdown && !dropdown.contains(event.target)) {
        dropdown.classList.remove("open");
        toggle?.setAttribute("aria-expanded", "false");
    }
});