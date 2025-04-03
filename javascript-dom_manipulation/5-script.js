document.addEventListener("DOMContentLoaded", function () {
  let updateHeader = document.getElementById("update_header");
  let header = document.querySelector("header");

  updateHeader.addEventListener("click", function () {
    header.textContent = "New Header!!!";
  });
});
