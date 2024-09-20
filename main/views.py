from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MetalStuff, Currency
from django.shortcuts import get_object_or_404
import requests
import json

# Create your views here.

currency_names = {
    "United States Dollar": "USD",
    "Euro": "EUR",
    "British Pound Sterling": "GBP",
    "Japanese Yen": "JPY",
    "Australian Dollar": "AUD",
    "Canadian Dollar": "CAD",
    "Swiss Franc": "CHF",
    "Chinese Yuan": "CNY",
    "Indian Rupee": "INR",
    "Brazilian Real": "BRL",
    "Russian Ruble": "RUB",
    "South African Rand": "ZAR",
    "Hong Kong Dollar": "HKD",
    "Singapore Dollar": "SGD",
    "Mexican Peso": "MXN",
    "New Zealand Dollar": "NZD",
    "South Korean Won": "KRW",
    "Swedish Krona": "SEK",
    "Norwegian Krone": "NOK",
    "Danish Krone": "DKK",
    "Malaysian Ringgit": "MYR",
    "Thai Baht": "THB",
    "Indonesian Rupiah": "IDR",
    "Turkish Lira": "TRY",
    "United Arab Emirates Dirham": "AED",
    "Saudi Riyal": "SAR",
    "Philippine Peso": "PHP",
    "Polish Zloty": "PLN",
    "Israeli New Shekel": "ILS",
    "Hungarian Forint": "HUF",
}

metals = [
    {"id": 1, "name": "Gold", "symbol": "XAU"},
    {"id": 2, "name": "Silver", "symbol": "XAG"},
    {"id": 3, "name": "Platinum", "symbol": "XPT"},
    {"id": 4, "name": "Palladium", "symbol": "XPD"},
]


def hello(request):
    metal = (i["name"] for i in metals)
    cu = (i for i in currency_names.keys())
    return render(request, "index.html", {"metal": metal, "cu": cu})


def get_conversion_rate():
    api_key = "47f1b3a61ca06a4ef02f064c"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    data = response.json()

    convert = data["conversion_rates"]
    # want_curr = currency

    # final = convert[want_curr]

    data = Currency.objects.create(data=convert)
    data.save()


@csrf_exempt
def process_selection(request):
    if request.method == "POST":
        selected_metal = request.POST.get("selected_metal")
        selected_cu = request.POST.get("selected_cu")
        # metal_sym = next(i["symbol"] for i in metals if i["name"] == selected_metal)
        cu_sym = currency_names.get(selected_cu)

        metal_data = get_object_or_404(MetalStuff, name=selected_metal)
        new_metal_data = json.loads(metal_data.data)

        currency_data = get_object_or_404(Currency, id=1)
        price_gram_data = {
            key: value * currency_data.data[cu_sym]
            for key, value in new_metal_data.items()
            if key.startswith("price_gram")
        }

        formatted_data = {key[11:].upper(): value for key, value in price_gram_data.items()}    

        data = {
            "price_gram_data": formatted_data,
        }

        return render(request, "table.html", data)



@csrf_exempt
def getData():
    def make_gapi_request(metal):
        api_key = "goldapi-qwx1slzeoc5xb-io"
        curr = "USD"
        date = ""

        url = f"https://www.goldapi.io/api/{metal}/{curr}{date}"

        headers = {"x-access-token": api_key, "Content-Type": "application/json"}

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        result = response.json()
        formated_result = json.dumps(result, indent=2)

        return formated_result

    for i in metals:
        old_item = MetalStuff.objects.get(id=i["id"])
        old_item.delete()
        data = make_gapi_request(i["symbol"])
        item = MetalStuff.objects.create(id=i["id"], name=i["name"], data=data)
        item.save()

    print("done")
