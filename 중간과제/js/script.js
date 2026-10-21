// 파일 연결 확인
console.log("script loaded");

// 거인병사에 마우스가 들어오면
$(".giant").on("mouseenter", function () {
  $(".giant").addClass("active");
  $(".person-2").addClass("active");
});

// 거인병사에서 마우스가 나가면
$(".giant").on("mouseleave", function () {
  $(".giant").removeClass("active");
  $(".person-2").removeClass("active");
});

// 처음에는 포스터1이 보이는 상태
let poster_state = 1;

// 두 포스터 중 현재 보이는 포스터를 클릭하면
$(".poster-1, .poster-2").on("click", function () {
  if (poster_state == 1) {
    // 포스터1에서 포스터2로 전환
    $(".poster-1").removeClass("showing");
    $(".poster-2").addClass("showing");

    poster_state = 2;
  } else {
    // 포스터2에서 포스터1로 전환
    $(".poster-2").removeClass("showing");
    $(".poster-1").addClass("showing");

    poster_state = 1;
  }
});
