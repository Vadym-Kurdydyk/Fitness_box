
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
const themeToggleCheckbox = document.getElementById('theme-toggle');


const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
  document.documentElement.classList.add(savedTheme);
  if (savedTheme === 'light') {
    themeToggleCheckbox.checked = true;
  }
}


function toggleTheme() {
  const currentTheme = themeToggleCheckbox.checked ? 'light' : 'dark';
  localStorage.setItem('theme', currentTheme);
  document.documentElement.classList.toggle('light', currentTheme === 'light');
}


themeToggle.addEventListener('click', toggleTheme);


