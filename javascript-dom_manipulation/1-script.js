document.addEventListener("DOMContentLoaded", function () {
  let redHeader = document.getElementById("red_header");
  let header = document.querySelector("header");
  redHeader.addEventListener("click", function () {
    header.style.color = "#FF0000";
  });
});
