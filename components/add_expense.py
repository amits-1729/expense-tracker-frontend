 # -------- ADD EXPENSE --------
import streamlit as st
from utils.helpers import get_categories_dict
import requests

# def add_expense(API_URL,headers):

#     amount = st.number_input("Enter amount")
#     category_dict = get_categories_dict(API_URL,headers)
#     col1, col2 = st.columns(2)
#     category = st.selectbox("Select Category", list(category_dict.keys()))
#     category_id = category_dict[category]
#     description = st.text_input("Enter description")
#     expense_date = st.date_input("Select date")
#     payment_method = st.selectbox("Payment method", ["Cash", "UPI", "Card"])

#     if st.button("Add Expense"):

#         data = {
#             "category_id": category_id,
#             "amount": amount,
#             "description": description,
#             "expense_date": str(expense_date),
#             "payment_method": payment_method
#         }

#         response = requests.post(
#             f"{API_URL}/add-expense",
#             json=data,
#             headers=headers
#         )

#         if response.status_code == 200:
#             st.success(response.json()["message"])
#         else:
#             st.error("Failed to add expense")


def add_expense(API_URL, headers):
    st.subheader("➕ Log New Expense")
    st.markdown("Fill in the details below to track your spending.")
    
    # Use a form to batch updates and prevent flickering
    with st.form("expense_form", clear_on_submit=True):
        
        # Row 1: Amount and Category
        col1, col2 = st.columns(2)
        with col1:
            amount = st.number_input("Amount", min_value=0.0, step=0.01, format="%.2f")
        with col2:
            category_dict = get_categories_dict(API_URL, headers)
            category = st.selectbox("Category", list(category_dict.keys()))
            category_id = category_dict[category]

        # Row 2: Date and Payment Method
        col3, col4 = st.columns(2)
        with col3:
            expense_date = st.date_input("Transaction Date")
        with col4:
            payment_method = st.selectbox("Payment Method", ["Cash", "UPI", "Card"])

        # Row 3: Description (Full width)
        description = st.text_input("Description", placeholder="e.g., Grocery shopping at Walmart")

        st.markdown("---")
        
        # Submit Button
        submit_button = st.form_submit_button("Save Expense", use_container_width=True)

    if submit_button:
        # Basic validation
        if amount <= 0:
            st.warning("Please enter an amount greater than 0.")
            return

        data = {
            "category_id": category_id,
            "amount": amount,
            "description": description,
            "expense_date": str(expense_date),
            "payment_method": payment_method
        }

        with st.spinner("Syncing with server..."):
            try:
                response = requests.post(
                    f"{API_URL}/add-expense",
                    json=data,
                    headers=headers
                )

                if response.status_code == 200:
                    st.success(f"✅ {response.json().get('message', 'Expense added successfully!')}")
                else:
                    st.error(f"❌ Error {response.status_code}: Could not save expense.")
            except Exception as e:
                st.error(f"⚠️ Connection Error: {str(e)}")