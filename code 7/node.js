console.log("complete");
console.log($(window).width());
console.log($(window).height());

let width = $(window).width();
let weight = $(window).height();

$(document).on("mousemove", function (event) {
  let mouseX = event.pageX;
  let mouseY = event.pageY;

  $(".bg-img").css("object-position", "$(mouseX / 10)% $(mouseY / 10)%");

  let imgWidth = $(".cat-img").width();
  let imgHeight = $(".cat-img").height();

  $(".cat-img").css("left", mouseX - imgWidth + "px");
  $(".cat-img").css("top", mouseY - imgHeight + "px");
});

console.log(width);
console.log(weight);

$(document).mousemove(function (e) {
  $("#status").html(e.pageX + "," + e.pageY);
  $(".box").css("width", e.pageX);
  $(".box").css("height", e.pageY);
});
