document.addEventListener("DOMContentLoaded", function() {
  var nav = document.querySelector('.nav-container-wrapper');
  var topContent = document.querySelector('.top-content');
  var stickyOffset = nav.offsetTop;

  function checkSticky() {
    if (window.pageYOffset > stickyOffset) {
      nav.classList.add('sticky');
    } else {
      nav.classList.remove('sticky');
    }
  }

  window.addEventListener('scroll', checkSticky);
});

document.addEventListener("DOMContentLoaded", function() {
  const links = document.querySelectorAll('.nav a');

  for (const link of links) {
    link.addEventListener('click', function(event) {
      event.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      const targetElement = document.getElementById(targetId);

      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop,
          behavior: 'smooth'
        });
      }
    });
  }
});