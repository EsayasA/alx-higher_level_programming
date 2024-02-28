git clone https://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@github.com/EsayasA/alx-higher_level_programming.git




$(document).ready(function() {
    // Select the <div> with ID "red_header"
    const redHeaderDiv = $("#red_header");

    // Add a click event listener
    redHeaderDiv.on("click", function() {
      // Select the <header> element
      const headerElement = $("header");

      // Update the text color to red
      headerElement.css("color", "#FF0000");
    });
  });
