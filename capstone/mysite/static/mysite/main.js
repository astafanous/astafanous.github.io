//Hover on an image to enlarge it, Click to rotate it and tab to navigate
document.addEventListener("DOMContentLoaded", function () {
  const galleryImages = document.querySelectorAll(".imageGallery img");

  galleryImages.forEach(img => {
    // Initial default state
    img.style.width = "23%";

    img.style.height = "15vh"; // 15% of viewport height


    img.style.transform = "scale(1)";
    img.style.boxShadow = "none";
    img.style.transition = "all 0.3s ease, transform 0.5s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.3s ease";
    img.style.transformOrigin = "center center";
    img.style.zIndex = "1";
  });

  // Then add your hover, click, and focus listeners here...

  galleryImages.forEach(img => {
    // Hover to enlarge
    img.addEventListener("mouseenter", () => {
      img.style.transform = "scale(2)";
      img.style.boxShadow = "6px 6px 20px rgba(0, 0, 0, 0.7)";
      img.style.zIndex = "10";
    });

    img.addEventListener("mouseleave", () => {
      img.style.transform = "scale(1)";
      img.style.boxShadow = "none";
      img.style.zIndex = "1";
    });

    // Click to rotate
    img.addEventListener("click", () => {
      if (img.style.transform.includes("rotate")) {
        img.style.transform = "scale(1)";
      } else {
        img.style.transform = "rotate(30deg)";
        img.style.boxShadow = "12px 12px 25px rgba(0, 0, 0, 0.7)";
        img.style.width = "44%";
      }
    });

    // Tab key focus (optional: reset rotation on blur)
    img.addEventListener("focus", () => {
      img.style.transform = "rotate(30deg)";
      img.style.boxShadow = "12px 12px 25px rgba(0, 0, 0, 0.7)";
      img.style.width = "44%";
    });

    img.addEventListener("blur", () => {
      img.style.transform = "scale(1)";
      img.style.boxShadow = "none";
      img.style.width = "23%";
    });
  });
});


// function loads content without refreshing
function showPage(pageId) {
  // Hide only the page sections
  document.querySelectorAll('.page-section').forEach(div => {
    div.style.display = 'none';
  });

  // Show the selected page
  const target = document.getElementById(pageId);
  if (target) {
    target.style.display = 'block';
  }
}

document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('button[data-page]').forEach(button => {
    button.onclick = function() {
      showPage(this.dataset.page);
    };
  });
});


// Initialize Summernote for Posts
$(document).ready(function() {
    $('#id_body').summernote({
        height: 300
    });
});


// Initialize Summernote for Pages

  $(document).ready(function() {
    $('#id_content').summernote({ height: 300 });
  });
