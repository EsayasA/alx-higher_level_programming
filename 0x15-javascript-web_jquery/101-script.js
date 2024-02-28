<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="101-script.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

    <!-- Add your JavaScript script here -->
    <script>
        $(document).ready(function() {
            // When the user clicks on DIV#add_item
            $("#add_item").click(function() {
                // Create a new <li> element with the text "Item"
                const newItem = $("<li>").text("Item");
                // Append the new item to UL.my_list
                $("ul.my_list").append(newItem);
            });

            // When the user clicks on DIV#remove_item
            $("#remove_item").click(function() {
                // Remove the last <li> element from UL.my_list
                $("ul.my_list li:last-child").remove();
            });

            // When the user clicks on DIV#clear_list
            $("#clear_list").click(function() {
                // Remove all <li> elements from UL.my_list
                $("ul.my_list").empty();
            });
        });
    </script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <div id="remove_item">Remove item</div>
    <div id="clear_list">Clear list</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
