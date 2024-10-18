document.getElementById('calculate-button').addEventListener('click', function() {
    const k = document.getElementById('k-value').value;

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ k: parseInt(k) })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Number of Ways: ${data.ways}`;
    })
    .catch(error => console.error('Error:', error));
});
