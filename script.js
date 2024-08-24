document.getElementById('product-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const products = document.getElementById('products').value;
    
    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ products: products })
    })
    .then(response => response.json())
    .then(data => {
        let resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';

        data.forEach(product => {
            resultsDiv.innerHTML += `
                <div class="result">
                    <h3>Product: ${product["Product Name"]}</h3>
                    <p><strong>Amazon:</strong> ${product["Amazon Name"]} - ₹${product["Amazon Price"]}</p>
                    <p><strong>Walmart:</strong> ${product["Walmart Name"]} - ₹${product["Walmart Price"]}</p>
                    <hr>
                </div>
            `;
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
});