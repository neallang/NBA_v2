document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("dark-mode-toggle");
    const darkModeCSS = document.getElementById("dark-mode-css");

    toggleButton.addEventListener("click", function() {
        if (darkModeCSS.disabled) {
            darkModeCSS.disabled = false;
            localStorage.setItem("darkMode", "enabled");
        } else {
            darkModeCSS.disabled = true;
            localStorage.setItem("darkMode", "disabled");
        }
    });

    // apply the mode on page load
    if (localStorage.getItem("darkMode") === "enabled") {
        darkModeCSS.disabled = false;
    }
});