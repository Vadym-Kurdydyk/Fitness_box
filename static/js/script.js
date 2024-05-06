
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

document.addEventListener("DOMContentLoaded", function(){
  const editButtons = document.querySelectorAll(".thread__update");
  const editForms = document.querySelectorAll(".edit__message");
  const messageContents = document.querySelectorAll(".thread__message");


  editButtons.forEach((editButton, index) => {
      editButton.addEventListener("click", function() {
          console.log("Edit button clicked!");
          messageContents[index].toggleAttribute("hidden"); 
          editForms[index].toggleAttribute("hidden"); 
      });
  });

 
  editForms.forEach((editForm, index) => {
      editForm.addEventListener("submit", function(event) {
          event.preventDefault(); 

          const messageId = editForm.parentElement.dataset.messageId;
          const csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').value;
          const messageBodyTextarea = editForm.querySelector("textarea[name='body']"); 
          const messageBody = messageBodyTextarea.value; 

          const url = `/update-message/${messageId}/`;
          fetch(url, {
              method: "POST",
              body: JSON.stringify({ body: messageBody }),
              headers: {
                  "Content-Type": "application/json",
                  "X-CSRFToken": csrfToken 
              }
          })
          .then(response => response.json())
          .then(data => {
              
              messageContents[index].textContent = data.updated_message_body;
              messageContents[index].toggleAttribute("hidden", false); 
              editForm.toggleAttribute("hidden", true); 
          })
          .catch(error => {
              console.error('Error:', error);
              
          });
      });
  });
});
