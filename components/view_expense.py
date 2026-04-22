import pandas as pd
import streamlit as st
from utils.helpers import get_categories_dict2
import requests

def view_expense(API_URL, headers):
    st.subheader("📊 Expense History")

    # Layout for Controls
    col_header, col_btn = st.columns([4, 1])
    with col_header:
        st.write("Review and filter your recent transactions.")
    with col_btn:
        refresh = st.button("🔄 Refresh Data", use_container_width=True)

    # Fetch Data
    try:
        response = requests.get(f"{API_URL}/get-expense", headers=headers)
        
        if response.status_code == 200:
            expenses = response.json().get("expenses", [])

            if not expenses:
                st.info("No expenses found. Start by adding one in the 'Add Expense' tab!")
                return

            # Convert to DataFrame
            df = pd.DataFrame(expenses)
            
            # Map Categories
            category_dict = get_categories_dict2(API_URL, headers)
            df['Category'] = df['category_id'].map(category_dict)

            # Cleanup and Rename
            df = df.rename(columns={
                "amount": "Amount (₹)",
                "description": "Description",
                "expense_date": "Date",
                "payment_method": "Payment"
            })

            # Reorder columns
            display_df = df[["Date", "Category", "Description", "Amount (₹)", "Payment"]]
            display_df['Date'] = pd.to_datetime(display_df['Date']).dt.date

            # # --- PROFESSIONAL METRICS SECTION ---
            # total_spend = df["Amount (₹)"].sum()
            # total_count = len(df)
            # avg_spend = total_spend / total_count if total_count > 0 else 0

            # m1, m2, m3 = st.columns(3)
            # m1.metric("Total Spending", f"₹{total_spend:,.2f}")
            # m2.metric("Transactions", total_count)
            # m3.metric("Avg. per Expense", f"₹{avg_spend:,.2f}")

            # st.markdown("---")

            # # --- SEARCH & FILTER ---
            # search_query = st.text_input("🔍 Search description...", "")
            # if search_query:
            #     display_df = display_df[display_df['Description'].str.contains(search_query, case=False, na=False)]

            # --- DATA TABLE ---
            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Amount (₹)": st.column_config.NumberColumn(format="₹ %.2f"),
                    "Date": st.column_config.DateColumn("Date"),
                    "Payment": st.column_config.TextColumn("Method")
                }
            )

        else:
            st.error(f"❌ Failed to fetch expenses (Status: {response.status_code})")

    except Exception as e:
        st.error(f"⚠️ Connection Error: {str(e)}")



# def view_expense(API_URL,headers):

#     if st.button("RELOAD"):

#         response = requests.get(f"{API_URL}/get-expense", headers=headers)

#         if response.status_code == 200:
#             expenses = response.json()["expenses"]

#             if len(expenses) == 0:
#                 st.info("No expenses found")
#             else:
#                 df = pd.DataFrame(expenses)
#                 # df['id'] = df['id'].astype(int)
#                 category_dict = get_categories_dict2(API_URL,headers)
#                 df['category'] = df['category_id'].map(category_dict)
#                 # Rename columns for UI
#                 df = df.rename(columns={
#                     "category": "Category",
#                     "amount": "Amount (₹)",
#                     "description": "Description",
#                     "expense_date": "Date",
#                     "payment_method": "Payment"
#                 })
#                 df = df[["Category","Amount (₹)","Description","Date","Payment"]]

#                 st.dataframe(df, use_container_width=True)
#         else:
#             st.error("Failed to fetch expenses")