import requests

# Cryptocurrency symbol and target currency
CRYPTO_SYMBOL = 'bitcoin'
TARGET_CURRENCY = 'usd'

# Endpoint URL for getting cryptocurrency prices from CoinGecko API
ENDPOINT = f'https://api.coingecko.com/api/v3/simple/price?ids={CRYPTO_SYMBOL}&vs_currencies={TARGET_CURRENCY}'

# Send API request
response = requests.get(ENDPOINT)

# Check if the request was successful
if response.status_code == 200:
    # Extract the price from the response
    data = response.json()
    price = data[CRYPTO_SYMBOL][TARGET_CURRENCY]
    print(f'Current price of {CRYPTO_SYMBOL} in {TARGET_CURRENCY}: {price}')
else:
    print(f'Failed to get cryptocurrency price. Status code: {response.status_code}')
