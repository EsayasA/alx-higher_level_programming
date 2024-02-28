$(document).ready(function() {
        // Add a click event listener to the <div> with ID "red_header"
        $("#red_header").click(function() {
            // Select the <header> element by its tag name
            $("header").addClass("red");
        });
    });
