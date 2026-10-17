document.querySelectorAll(".mobile-nav").forEach(mobileNav => {
    const menuToggle = mobileNav.querySelector(".mobile-menu-toggle");
    const mobileMenuLinks = mobileNav.querySelectorAll(".mobile-menu a");

    menuToggle.addEventListener("click", () => {
        const isOpen = mobileNav.classList.toggle("is-open");
        menuToggle.setAttribute("aria-expanded", isOpen);
    });

    mobileMenuLinks.forEach(link => {
        link.addEventListener("click", () => {
            mobileNav.classList.remove("is-open");
            menuToggle.setAttribute("aria-expanded", "false");
        });
    });
});