window.onscroll = function() {scrollEvent()};

function scrollEvent() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    document.getElementById("mainNav").className = "navbar navbar-expand-lg navbar-dark fixed-top site-header";

  } else {
    document.getElementById("mainNav").className = "navbar navbar-expand-lg navbar-dark fixed-top";

  }

}