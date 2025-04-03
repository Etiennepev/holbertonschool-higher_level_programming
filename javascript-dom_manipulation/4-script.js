document.addEventListener("DOMContentLoaded", function () {
  let addItem = document.getElementById("add_item");
  let myList = document.querySelector(".my_list");

  addItem.addEventListener("click", function () {
    let newItem = document.createElement("li");
    newItem.textContent = "Item";
    myList.appendChild(newItem);
  });
});
