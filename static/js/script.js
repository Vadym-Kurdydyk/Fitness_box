
// Menu
const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");

if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    dropdownMenu.classList.toggle("show");
  });
}

// Upload Image
const photoInput = document.querySelector("#avatar");
const photoPreview = document.querySelector("#preview-avatar");
if (photoInput) {
  photoInput.onchange = () => {
    const [file] = photoInput.files;
    if (file) {
      photoPreview.src = URL.createObjectURL(file);
    }
  };
}

// Scroll to Bottom
const conversationThread = document.querySelector(".room__box");
if (conversationThread) {
  conversationThread.scrollTop = conversationThread.scrollHeight;
}

// Switch theme
const themeToggle = document.getElementById('theme-toggle');
const themeStyle = document.getElementById('theme-style');

themeToggle.addEventListener('click', () => {
  const currentTheme = themeStyle.dataset.theme;
  if (currentTheme === 'light') {
    themeStyle.setAttribute('href', '{% static "styles/style-dark.css" %}');
    themeStyle.dataset.theme = 'dark';
  } else {
    themeStyle.setAttribute('href', '{% static "styles/style-light.css" %}');
    themeStyle.dataset.theme = 'light';
  }
});


