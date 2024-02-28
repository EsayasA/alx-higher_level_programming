$(document).ready(function() {
    // Initial class for the <header> element
    let headerClass = 'red';

    // Set the initial class for the <header> element
    $('header').addClass(headerClass);

    // Handle click event on DIV#toggle_header
    $('#toggle_header').click(function() {
      // Toggle the class between red and green
      if (headerClass === 'red') {
        headerClass = 'green';
      } else {
        headerClass = 'red';
      }

      // Update the class of the <header> element
      $('header').removeClass('red green').addClass(headerClass);
    });
  });
