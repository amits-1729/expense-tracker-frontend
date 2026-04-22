import streamlit as st
import requests
from components.add_expense import add_expense
from components.view_expense import view_expense
from components.edit_expense import edit_expense
from components.delete_expense import delete_expense
from components.metric import daily_top_metric, weekly_top_metric
from tabs.auth_page import show_auth_page
from components.trends import daily_spending_by_cat, weekly_spending_by_cat, show_trends


API_URL = st.secrets["API_URL"]

# ------------------ NOT LOGGED IN ------------------
if "token" not in st.session_state:
    show_auth_page(API_URL)


# ------------------ LOGGED IN ------------------
else:
    headers = {
        "Authorization": f"Bearer {st.session_state['token']}"
    }

    with st.sidebar:
        _, col_img, _ = st.columns([1, 2, 1])
        with col_img:
            st.image("expense_app_logo.png", use_container_width=True)
        
        st.markdown(f"### Welcome, **{st.session_state.get('user_name', 'User')}**!")
        st.caption("Manage your finances with ease.")
        
        st.divider()

        if st.button("🚪 Log Out", use_container_width=True, type="secondary"):
            st.session_state.clear()
            st.rerun()

    st.title("💰 Expense Tracker")

    # -------- EXPENSE TABS --------
    tab1, tab2 = st.tabs([
        "Expenses",
        "Spending Trends"
    ])

    # All expense operations
    with tab1:
        with st.container(border=True):
            choice = ["ADD", "VIEW", "EDIT", "DELETE"]
            selected_oper = st.pills("Transaction Operations", choice, selection_mode="single")
        
        with st.container(border=True):
            if selected_oper == "ADD":
                add_expense(API_URL,headers)

            elif selected_oper == "VIEW":
                view_expense(API_URL,headers)

            elif selected_oper == "EDIT":
                edit_expense(API_URL,headers)

            elif selected_oper == "DELETE":
                delete_expense(API_URL,headers)
            
            else:
                st.info("Select above options to perform any operations")


    # -------- SPENDING TRENDS --------
    with tab2:
        options = ["Daily", "Weekly","Monthly"]
        selection = st.pills("Options", options, selection_mode="single")

        if selection == "Daily":
            with st.container(border=True):
                st.markdown("📅 **Daily Overview**")
                daily_top_metric(API_URL, headers)

            # st.subheader("Category-wise spent")
            with st.container(border=True):
                daily_spending_by_cat(API_URL, headers)

        elif selection == "Weekly":
            with st.container(border=True):
                st.markdown("📅 **Weekly Overview**")
                weekly_top_metric(API_URL, headers)

            # st.subheader("Category-wise spent")
            with st.container(border=True):
                weekly_spending_by_cat(API_URL, headers)

            # st.subheader("Total spent over days")
            with st.container(border=True):
                show_trends(API_URL, headers)


        elif selection == "Monthly":
            st.info("comming soon")
        else:
            st.info("Select the trend which you want to see")