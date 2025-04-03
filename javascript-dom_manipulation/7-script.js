document.addEventListener("DOMContentLoaded", function () {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      data.results.forEach(movie => {
        document.getElementById("list_movies").innerHTML += `<li>${movie.title}</li>`;
      });
    })
    .catch(error => console.error("Error:", error));
});
