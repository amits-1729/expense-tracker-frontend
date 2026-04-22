import streamlit as st
import plotly.express as px
import requests
import pandas as pd
import matplotlib.pyplot as plt



def daily_top_metric(API_URL, headers):
    # Fetch data (simplified for example)
    res1 = requests.get(f"{API_URL}/expenses/daily-metric?filter=today", headers=headers)
    res2 = requests.get(f"{API_URL}/expenses/daily-metric?filter=yesterday", headers=headers)
    
    today = res1.json()
    yesterday = res2.json()

    # CSS for custom cards
    st.markdown("""
        <style>
        .metric-container {
            display: flex;
            justify-content: space-between;
            gap: 10px;
            margin-bottom: 20px;
        }
        .metric-card {
            background-color: #ffffff;
            border: 1px solid #e6e9ef;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            width: 100%;
            transition: transform 0.3s ease;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            border-color: #4CAF50;
        }
        .metric-label {
            font-size: 14px;
            color: #6b7280;
            font-weight: 600;
            text-transform: uppercase;
        }
        .metric-value {
            font-size: 24px;
            font-weight: 700;
            color: #111827;
            margin: 5px 0;
        }
        .metric-delta {
            font-size: 13px;
            font-weight: 500;
        }
        .delta-up { color: #ef4444; } /* Red for more spending */
        .delta-down { color: #10b981; } /* Green for less spending */
        </style>
    """, unsafe_allow_html=True)

    # Logic for deltas
    spend_diff = today["total_spend"] - yesterday["total_spend"]
    spend_class = "delta-up" if spend_diff > 0 else "delta-down"
    spend_arrow = "▲" if spend_diff > 0 else "▼"

    # HTML injection
    st.markdown(f"""
        <div class="metric-container">
            <div class="metric-card">
                <div class="metric-label">Total Spend</div>
                <div class="metric-value">₹{today['total_spend']:,.2f}</div>
                <div class="metric-delta {spend_class}">
                    {spend_arrow} ₹{abs(spend_diff):,.2f} <span style="color: #6b7280;">vs yesterday</span>
                </div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Transactions</div>
                <div class="metric-value">{today['total_transactions']}</div>
                <div class="metric-delta" style="color: #6b7280;">
                    Daily volume
                </div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Avg. Spend</div>
                <div class="metric-value">₹{today['avg_spend']:,.2f}</div>
                <div class="metric-delta" style="color: #6b7280;">
                    Per transaction
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)




def weekly_top_metric(API_URL, headers):
    # Fetch data (simplified for example)
    res1 = requests.get(f"{API_URL}/expenses/weekly-metrics?filter=current", headers=headers)
    res2 = requests.get(f"{API_URL}/expenses/weekly-metrics?filter=last", headers=headers)
    
    current = res1.json()
    last = res2.json()

    # CSS for custom cards
    st.markdown("""
        <style>
        .metric-container {
            display: flex;
            justify-content: space-between;
            gap: 10px;
            margin-bottom: 20px;
        }
        .metric-card {
            background-color: #ffffff;
            border: 1px solid #e6e9ef;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            width: 100%;
            transition: transform 0.3s ease;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            border-color: #4CAF50;
        }
        .metric-label {
            font-size: 14px;
            color: #6b7280;
            font-weight: 600;
            text-transform: uppercase;
        }
        .metric-value {
            font-size: 24px;
            font-weight: 700;
            color: #111827;
            margin: 5px 0;
        }
        .metric-delta {
            font-size: 13px;
            font-weight: 500;
        }
        .delta-up { color: #ef4444; } /* Red for more spending */
        .delta-down { color: #10b981; } /* Green for less spending */
        </style>
    """, unsafe_allow_html=True)

    # Logic for deltas
    spend_diff = current["total_spend"] - last["total_spend"]
    spend_class = "delta-up" if spend_diff > 0 else "delta-down"
    spend_arrow = "▲" if spend_diff > 0 else "▼"

    # HTML injection
    st.markdown(f"""
        <div class="metric-container">
            <div class="metric-card">
                <div class="metric-label">Total Spend</div>
                <div class="metric-value">₹{current['total_spend']:,.2f}</div>
                <div class="metric-delta {spend_class}">
                    {spend_arrow} ₹{abs(spend_diff):,.2f} <span style="color: #6b7280;">vs last week</span>
                </div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Transactions</div>
                <div class="metric-value">{current['total_transactions']}</div>
                <div class="metric-delta" style="color: #6b7280;">
                    Weekly volume
                </div>
            </div>
            <div class="metric-card">
                <div class="metric-label">Avg. Spend</div>
                <div class="metric-value">₹{current['avg_spend']:,.2f}</div>
                <div class="metric-delta" style="color: #6b7280;">
                    Per transaction
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)





# def weekly_top_metric(API_URL, headers):
#     # Fetch data
#     response1 = requests.get(f"{API_URL}/expenses/weekly-metrics?filter=current", headers=headers)
#     current = response1.json()
#     response2 = requests.get(f"{API_URL}/expenses/weekly-metrics?filter=last", headers=headers)
#     last = response2.json()

#     # Calculations
#     spend_delta = current["total_spend"] - last["total_spend"]
#     txn_delta = current["total_transactions"] - last["total_transactions"]
#     avg_delta = round((current["avg_spend"] - last["avg_spend"]), 2)

#     # Custom CSS for Professional Financial Cards
#     st.markdown("""
#         <style>
#         [data-testid="stMetric"] {
#             background-color: #ffffff;
#             border: 1px solid #f0f2f6;
#             padding: 15px;
#             border-radius: 12px;
#             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
#         }
#         [data-testid="stMetricLabel"] {
#             font-size: 14px !important;
#             font-weight: 700 !important;
#             color: #64748b !important;
#             text-transform: uppercase;
#         }
#         [data-testid="stMetricValue"] {
#             font-size: 24px !important;
#             font-weight: 800 !important;
#             color: #1e293b !important;
#         }
#         </style>
#     """, unsafe_allow_html=True)

#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         st.metric(
#             label="Total Spend",
#             value=f"₹{current['total_spend']:,}",
#             delta=f"₹{abs(spend_delta):,} {'increased' if spend_delta > 0 else 'decreased'}",
#             delta_color="inverse"  # Red if spending went up
#         )

#     with col2:
#         # For transactions, higher might be "good" (activity) or "bad" (impulse)
#         # Usually, fintech apps treat this as neutral (off-color)
#         st.metric(
#             label="Transactions",
#             value=f"{current['total_transactions']}",
#             delta=f"{txn_delta:+} vs last week",
#             delta_color="normal" 
#         )

#     with col3:
#         st.metric(
#             label="Avg. Ticket Size",
#             value=f"₹{round(current['avg_spend'], 2):,}",
#             delta=f"₹{abs(avg_delta):,} {'per txn'}",
#             delta_color="inverse"
#         )