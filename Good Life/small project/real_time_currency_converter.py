# The real time currency converter by country names
import requests


def convert():
    country_to_currency = {
        'United States': 'USD',
        'Eurozone': 'EUR',
        'United Kingdom': 'GBP',
        'India': 'INR',
        'Japan': 'JPY',
        'Canada': 'CAD',
        'Australia': 'AUD',
    }

    print("Real time currency converter by country name.")
    from_country = input("Enter the source country name:").title()
    target_country = input("Enter the target country name:").title()
    amount = float(input("Enter the amount:"))

    if from_country in country_to_currency and target_country in country_to_currency:
        from_currency = country_to_currency[from_country]
        to_currency = country_to_currency[target_country]

        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if to_currency in data['rates']:
                rate = data['rates'][to_currency]
                converted_amount = rate * amount
                print(
                    f"{amount} {from_currency} from {from_country} to equal to {round(converted_amount, 2)} {to_currency} in {target_country}")
            else:
                print("Currency conversion is not supported.")
        else:
            print("Error in fetching currency data.")
    else:
        print("Invalid country name entered.")


convert()
