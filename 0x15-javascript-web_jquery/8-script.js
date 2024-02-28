$(document).ready(function() {
    // Define the URL for movie data
    const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';

    // Fetch movie data
    $.getJSON(apiUrl, function(data) {
      // Extract movie titles
      const movieTitles = data.results.map(movie => movie.title);

      // Create an <li> element for each title
      const listItems = movieTitles.map(title => $('<li>').text(title));

      // Append the list items to UL#list_movies
      $('ul#list_movies').append(listItems);
    });
  });
