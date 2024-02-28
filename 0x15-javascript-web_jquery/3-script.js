$(document).ready(function() {
    // Select the <div> with ID "red_header"
    const redHeaderDiv = $("#red_header");

    // Add a click event listener
    redHeaderDiv.on("click", function() {
      // Select the <header> element
      const headerElement = $("header");

      // Add the class "red" to the <header> element
      headerElement.addClass("red");
    });
  });
