import streamlit as st
import requests


def show_auth_page(API_URL):
    _, col, _ = st.columns([1, 2, 1])
    
    with col:
        st.markdown("<h1 style='text-align: center;'>🏦 WealthFlow</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: gray;'>Smart tracking for modern finance</p>", unsafe_allow_html=True)
        
        auth_tab1, auth_tab2 = st.tabs(["Login", "Create Account"])

        with auth_tab1:
            email = st.text_input("Email", key="login_email", placeholder="Enter your registered email")
            password = st.text_input("Password", type="password", key="login_password")
            
            if st.button("Sign In", type="primary"):
                data = {
                    "email": email,
                    "password": password
                }
                response = requests.post(f"{API_URL}/login", json=data)
                if response.status_code == 200:
                    res = response.json()
                    st.session_state["token"] = res["access_token"]
                    st.session_state["user_name"] = res["user_name"]
                    st.rerun()
                else:
                    st.error("Invalid credentials. Please try again.")

        with auth_tab2:
            name = st.text_input("Full Name", placeholder="John Doe")
            email = st.text_input("Email address", placeholder="name@company.com", key="reg_email")
            password = st.text_input("Choose Password", type="password")
            
            if st.button("Create Account", type="primary"):
                data = {
                    "name": name,
                    "email": email,
                    "password": password
                }
                response = requests.post(f"{API_URL}/register", json=data)
                if response.status_code == 200:
                    st.success("Account created! You can now log in.")
                else:
                    st.error("Registration failed. Email may already be in use.")