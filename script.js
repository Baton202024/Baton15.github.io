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
  