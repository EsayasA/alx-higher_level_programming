// Fetch the translation from HelloSalut
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
.then(function(response) {
    return response.json();
})
.then(function(data) {
    // Get the translated "hello" value
    const translatedHello = data.hello;

    // Display the translation in the div with ID "hello"
    $('#hello').text(translatedHello);
})
.catch(function(error) {
    console.error('Error fetching translation:', error);
});
