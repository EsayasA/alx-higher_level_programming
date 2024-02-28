dy(function() {
  // Make an AJAX request to fetch the translation
  $.ajax({
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    method: "GET",
    success: function(data) {
      // Extract the translated word for "hello"
      var translatedHello = data.hello;

      // Update the text content of the DIV#hello
      $("#hello").text(translatedHello);
    },
    error: function() {
      // Handle any errors (e.g., network issues, invalid URL)
      console.error("Error fetching translation data.");
    }
  });
});
