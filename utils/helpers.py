import requests


def get_categories_dict(API_URL,headers):
    response = requests.get(f"{API_URL}/get-categories",headers=headers)
    category_dict = {}
    if response.status_code == 200:
        categories = response.json()["categories"]
        for cat in categories:
            category_dict[cat["name"]] = cat["id"]
    return category_dict

def get_categories_dict2(API_URL,headers):
    response = requests.get(f"{API_URL}/get-categories",headers=headers)
    category_dict = {}
    if response.status_code == 200:
        categories = response.json()["categories"]
        for cat in categories:
            category_dict[cat["id"]] = cat["name"]
    return category_dict


def get_expense_dict(API_URL,headers):
    response = requests.get(f"{API_URL}/get-expense", headers=headers)
    expense_dict = {}
    if response.status_code == 200:
        expenses = response.json()["expenses"]
        for exp in expenses:
            label = f"{exp['amount']} | {exp['description']} | {exp['expense_date']}"
            expense_dict[label] = exp 
    return expense_dict