$(document).ready(function() {
        // Select the <div> with ID "toggle_header"
        $("#toggle_header").click(function() {
            // Select the <header> element by its tag name
            const headerElement = $("header");

            // Toggle the class between "red" and "green"
            if (headerElement.hasClass("red")) {
                headerElement.removeClass("red").addClass("green");
            } else {
                headerElement.removeClass("green").addClass("red");
            }
        });
    });
