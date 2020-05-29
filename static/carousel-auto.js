var slideIndex = -1;

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex += 1;
  /* console.log(slideIndex); */
  if (slideIndex >= slides.length) {slideIndex = 0}
  slides[slideIndex].style.display = "block";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}

$(document).ready(showSlides);
