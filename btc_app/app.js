document.addEventListener('DOMContentLoaded', function() {
    getPrice();
    setInterval(getPrice, 5000); // Aggiorna il prezzo ogni 5 secondi
});

function getPrice() {
    fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    .then(response => response.json())
    .then(data => {
        const price = data.bitcoin.usd;
        displayPrice(price);
    })
    .catch(error => {
        console.error('Errore nella richiesta API:', error);
    });
}

function displayPrice(price) {
    const priceElement = document.getElementById('price');
    priceElement.textContent = `Prezzo attuale: $${price}`;
}
