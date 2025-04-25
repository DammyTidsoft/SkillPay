# payout.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()
FLW_SECRET_KEY = os.getenv("FLW_SECRET_KEY")

def pay_worker(phone: str, amount: int):
    url = "https://api.flutterwave.com/v3/disbursements"
    headers = {"Authorization": f"Bearer {FLW_SECRET_KEY}"}
    data = {
        "account_bank": "MPS",  # Mobile Money
        "account_number": phone,
        "amount": amount,
        "currency": "NGN"
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Example usage
print(pay_worker("07012345678", 5000))  # Pay ₦5000
