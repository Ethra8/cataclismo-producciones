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