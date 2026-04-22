# -------- DELETE EXPENSE --------
import streamlit as st
import requests
from utils.helpers import get_expense_dict

def delete_expense(API_URL, headers):
    st.subheader("🗑️ Delete Transaction")
    
    expense_dict = get_expense_dict(API_URL, headers)

    if not expense_dict:
        st.info("No expenses available to delete.")
        return

    # Container for better visual grouping
    with st.container(border=True):
        st.warning("⚠️ **Warning:** This action is permanent and cannot be undone.")
        
        selected_expense = st.selectbox(
            "Select the expense to remove:", 
            options=list(expense_dict.keys()),
            key="DELETE_SELECT"
        )
        
        # Display the details of the selected item so they know exactly what's being deleted
        item_details = expense_dict[selected_expense]
        expense_id = item_details["id"]
        
        col1, col2, col3 = st.columns(3)
        col1.caption(f"**Amount:** ₹{item_details['amount']}")
        col2.caption(f"**Date:** {item_details['expense_date']}")
        col3.caption(f"**Method:** {item_details['payment_method']}")

        # Double-check confirmation
        confirm_delete = st.checkbox(f"I confirm I want to delete record #{expense_id}")

        # Use a full-width red button for destructive actions
        if st.button("Permanently Delete Expense", 
                     disabled=not confirm_delete, 
                     type="primary", 
                     use_container_width=True):
            
            with st.spinner("Deleting..."):
                try:
                    response = requests.delete(
                        f"{API_URL}/delete-expense/{expense_id}",
                        headers=headers
                    )

                    if response.status_code == 200:
                        st.success(f"✅ Transaction #{expense_id} deleted successfully.")
                        # Rerun is recommended here to refresh the expense list immediately
                        st.rerun()
                    else:
                        st.error("❌ Failed to delete the transaction. Please try again.")
                except Exception as e:
                    st.error(f"⚠️ Connection error: {str(e)}")


# def delete_expense(API_URL,headers):

#     expense_dict = get_expense_dict(API_URL,headers)
    

#     if len(expense_dict) == 0:
#         st.info("No expenses to delete")
#     else:
#         selected_expense = st.selectbox("Select Expense", list(expense_dict.keys()),key="DELETE")
#         expense_id = expense_dict[selected_expense]["id"]

#         if st.button("Delete Expense"):

#             response = requests.delete(
#                 f"{API_URL}/delete-expense/{expense_id}",
#                 headers=headers
#             )

#             if response.status_code == 200:
#                 st.success(response.json()["message"])
#             else:
#                 st.error("Failed to delete expense")