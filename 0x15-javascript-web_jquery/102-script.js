<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="102-script.js"></script>
    <script>
        $(document).ready(function() {
            // When the user clicks on INPUT#btn_translate
            $("#btn_translate").click(function() {
                // Get the language code entered by the user
                const languageCode = $("#language_code").val();

                // Fetch the translation from the API
                $.get(`https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`, function(data) {
                    // Display the translation in DIV#hello
                    $("#hello").text(data.hello);
                });
            });
        });
    </script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
