data = {
    "timestamp": 1725221220,
    "metal": "XAG",
    "currency": "USD",
    "exchange": "FOREXCOM",
    "symbol": "FOREXCOM:XAGUSD",
    "prev_close_price": 29.424,
    "open_price": 29.424,
    "low_price": 28.6925,
    "high_price": 29.591,
    "open_time": 1724976000,
    "price": 28.8635,
    "ch": -0.561,
    "chp": -1.9,
    "ask": 28.884,
    "bid": 28.843,
    "price_gram_24k": 0.928,
    "price_gram_22k": 0.8507,
    "price_gram_21k": 0.812,
    "price_gram_20k": 0.7733,
    "price_gram_18k": 0.696,
    "price_gram_16k": 0.6187,
    "price_gram_14k": 0.5413,
    "price_gram_10k": 0.3867
}


price_gram_data = {key: value for key,
                   value in data.items() if key.startswith('price_gram')}

print(price_gram_data)
