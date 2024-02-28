$(document).ready(function() {
    // Define the URL for the character data
    const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

    // Fetch the character data
    $.getJSON(apiUrl, function(data) {
      // Extract the character name
      const characterName = data.name;

      // Display the character name in the DIV#character
      $('#character').text(characterName);
    });
  });
