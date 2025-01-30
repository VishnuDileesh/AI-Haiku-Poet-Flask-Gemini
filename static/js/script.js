document.getElementById('haiku-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form submission

    // Get the theme value
    const theme = document.getElementById('theme').value;

    fetch('/generate-haiku', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ theme: theme })
    })
    .then(response => response.json())
    .then(data => {
        // Display the Haiku in the result div
        document.getElementById('haiku-result').innerHTML = `<p>${data.haiku}</p>`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
