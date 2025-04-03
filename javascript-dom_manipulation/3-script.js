document.addEventListener("DOMContentLoaded", function () {
  let toggleHeader = document.getElementById("toggle_header");
  let header = document.querySelector("header");

  toggleHeader.addEventListener("click", function () {
    if (header.classList.contains("red")) {
      header.classList.replace("red", "green");
    } else {
      header.classList.replace("green", "red");
    }
  });
});
