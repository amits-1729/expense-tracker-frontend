import streamlit as st
import requests
from utils.helpers import get_expense_dict
from utils.helpers import get_categories_dict
import datetime


def edit_expense(API_URL,headers):
    st.subheader("📝 Edit Transaction")
    expense_dict = get_expense_dict(API_URL,headers)

    if len(expense_dict) == 0:
        st.info("No expenses to edit")
    else:
        selected_expense = st.selectbox("Select Expense", list(expense_dict.keys()))
        selected_data = expense_dict[selected_expense]

        expense_id = selected_data["id"]

        # 🔥 Prefill values
        new_amount = st.number_input("New Amount", value=selected_data["amount"])
        new_description = st.text_input("New description", value=selected_data["description"])
        new_date = st.date_input("New Date", value=selected_data["expense_date"])
        pay_methods = ["Cash", "UPI", "Card"]
        new_payment = st.selectbox(
            "New Payment Method",
            pay_methods,
            index=pay_methods.index(selected_data["payment_method"])
        )
        category_dict = get_categories_dict(API_URL,headers)
        category_list = list(category_dict.keys())
        new_category = st.selectbox("Select Category", category_list,index=None, key="edit_cat")
        if new_category is None:
            new_category_id = selected_data["category_id"]
        else:
            new_category_id = category_dict[new_category]

        if st.button("Update Expense"):

            data = {
                "category_id": new_category_id,
                "amount": new_amount,
                "description": new_description,
                "expense_date": str(new_date),
                "payment_method": new_payment
            }

            response = requests.put(
                f"{API_URL}/update-expense/{expense_id}",
                json=data,
                headers=headers
            )

            if response.status_code == 200:
                st.success(response.json()["message"])
            else:
                st.error("Failed to update expense")