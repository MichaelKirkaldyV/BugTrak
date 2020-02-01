
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
  setTimeout(showSlides, 2000); 
}

//------------------JQUERY------------------------------------//

$(document).ready(function(){
    $("a").hover(function(){
        $(this).addClass("newColor");
    }, function(){
        $(this).removeClass("newColor");
    });
});
