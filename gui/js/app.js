var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) { slideIndex = 1 }
  slides[slideIndex - 1].style.display = "block";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}



const typewriter = new Typewriter('#typewriter', {
  loop: true
});

typewriter.typeString('We provide live Twitter Sentiment Analysis On ')
  .pauseFor(2500)
  // .deleteAll()
  .typeString('Politics')
  .pauseFor(2500)
  .deleteChars(8)
  .typeString('Products')
  .pauseFor(2500)
  .deleteChars(8)
  .typeString('and Movies.')
  .pauseFor(2500)
  .deleteChars(11)
  .start();