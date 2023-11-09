const themeButton = document.getElementById("themeButton");

themeButton.addEventListener("click", function() {
    const currentTheme = themeButton.textContent.trim();

    if (currentTheme === "Default theme") {
        themeButton.textContent = "Dark theme";
        updateTheme("dark");
    } else {
        themeButton.textContent = "Default theme";
        updateTheme("default");
    }
});

function updateTheme(theme) {
    const url = `/change_theme?theme=${theme}`;
    fetch(url)
        .then(response => response.json())
        .then(data => {
          location.reload();
        })
        .catch(error => {
            console.error("เกิดข้อผิดพลาด: " + error);
        });
}
