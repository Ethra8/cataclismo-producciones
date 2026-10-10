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