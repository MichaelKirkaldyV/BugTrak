// Creates a slideshow of headers
var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("slideshow");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  // Change title every 2 seconds
  setTimeout(showSlides, 3000); 
}

//------------------JQUERY------------------------------------//

// Creates yellow hue over links in the navbar
$(document).ready(function(){
    $("a").hover(function(){
        $(this).addClass("newColor");
    }, function(){
        $(this).removeClass("newColor");
    });
});
