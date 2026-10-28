console.log("script loaded");

$(".giant").on("mouseenter", function () {
  $(".giant").addClass("active");
  $(".person-2").addClass("active");
});

$(".giant").on("mouseleave", function () {
  $(".giant").removeClass("active");
  $(".person-2").removeClass("active");
});

let poster_state = 1;

$(".poster-1, .poster-2").on("click", function () {
  if (poster_state == 1) {
    $(".poster-1").removeClass("showing");
    $(".poster-2").addClass("showing");

    poster_state = 2;
  } else {
    $(".poster-2").removeClass("showing");
    $(".poster-1").addClass("showing");

    poster_state = 1;
  }
});
