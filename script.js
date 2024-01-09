document.addEventListener("DOMContentLoaded", () => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        console.log(entry);
        if (entry.isIntersecting) {
          entry.target.classList.add('show');
        } else {
          entry.target.classList.remove('show');
        }
      });
    });
  
    const sectionsToObserve = document.querySelectorAll(".hidden");
  
    sectionsToObserve.forEach((section) => {
      observer.observe(section);
    });
  });
  

  function toggleReadMore(button) {
    const content = button.previousElementSibling;
    const section = content.parentElement;
    const maxHeight = "400px"; // Set your desired max height for the "read more" content here
    
    if (content.style.maxHeight === maxHeight) {
        content.style.maxHeight = "0";
        section.style.maxHeight = "auto";
        button.innerText = "Read More";
    } else {
        content.style.maxHeight = maxHeight;
        section.style.maxHeight = "400px"; // Adjust this value as needed
        button.innerText = "Read Less";
    }
}

