import streamlit as st
import plotly.express as px
import requests
import pandas as pd
import matplotlib.pyplot as plt

def daily_spending_by_cat(API_URL, headers):
    response = requests.get(
        f"{API_URL}/expenses/category-split?filter=daily",
        headers=headers
    )
    
    if response.status_code == 200:
        data = response.json().get("cat_expenses", [])
        df = pd.DataFrame(data)

        if df.empty:
            st.info("No categorical data found for this week.")
            return

        # Sort for visual flow
        df = df.sort_values('total', ascending=True) # Ascending for better horizontal bar display
        total_sum = df['total'].sum()

        # Modern Fintech Color Palette
        colors = px.colors.sequential.Blues_r 

        col1, div1, col2 = st.columns([10, 0.1, 6])

        with col1:
            # Horizontal Bar Chart (Easier to read labels)
            fig = px.bar(
                df,
                y="category",
                x="total",
                orientation='h',
                title='<b>Spending by Category</b>',
                color='total',
                color_continuous_scale='Blues'
            )
            
            fig.update_traces(
                marker_line_width=0,
                texttemplate='₹%{x:,.0f}', 
                textposition='outside',
                cliponaxis=False
            )

            fig.update_layout(
                height=400,
                template='plotly_white',
                xaxis=dict(showticklabels=False, title='', showgrid=False),
                yaxis=dict(title='', tickfont=dict(size=13)),
                coloraxis_showscale=False,
                margin=dict(l=0, r=50, t=40, b=0)
            )
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

        with div1:
            # Vertical Divider
            st.markdown('<div style="border-left: 1px solid #f0f2f6; height: 350px; margin-top: 25px;"></div>', unsafe_allow_html=True)

        with col2:
            # Sophisticated Donut Chart
            fig1 = px.pie(
                df,
                names="category",
                values="total",
                hole=0.7,  # Larger hole for cleaner look
                color_discrete_sequence=colors
            )
            
            fig1.update_traces(
                textinfo='none', # Hide text labels on slices for cleanliness
                hoverinfo='label+percent',
                marker=dict(line=dict(color='#FFFFFF', width=2))
            )

            fig1.update_layout(
                height=400,
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
                margin=dict(l=20, r=20, t=60, b=20),
                annotations=[
                    dict(
                        text='Total',
                        x=0.5, y=0.6,
                        font=dict(size=14, color="gray"),
                        showarrow=False
                    ),
                    dict(
                        text=f"<b>₹{total_sum:,.0f}</b>",
                        x=0.5, y=0.45,
                        font=dict(size=22, color="#1f1f1f"),
                        showarrow=False
                    )
                ]
            )
            st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False})



def weekly_spending_by_cat(API_URL, headers):
    response = requests.get(
        f"{API_URL}/expenses/category-split?filter=weekly",
        headers=headers
    )
    
    if response.status_code == 200:
        data = response.json().get("cat_expenses", [])
        df = pd.DataFrame(data)

        if df.empty:
            st.info("No categorical data found for this week.")
            return

        # Sort for visual flow
        df = df.sort_values('total', ascending=True) # Ascending for better horizontal bar display
        total_sum = df['total'].sum()

        # Modern Fintech Color Palette
        colors = px.colors.sequential.Blues_r 

        col1, div1, col2 = st.columns([10, 0.1, 6])

        with col1:
            # Horizontal Bar Chart (Easier to read labels)
            fig = px.bar(
                df,
                y="category",
                x="total",
                orientation='h',
                title='<b>Spending by Category</b>',
                color='total',
                color_continuous_scale='Blues'
            )
            
            fig.update_traces(
                marker_line_width=0,
                texttemplate='₹%{x:,.0f}', 
                textposition='outside',
                cliponaxis=False
            )

            fig.update_layout(
                height=400,
                template='plotly_white',
                xaxis=dict(showticklabels=False, title='', showgrid=False),
                yaxis=dict(title='', tickfont=dict(size=13)),
                coloraxis_showscale=False,
                margin=dict(l=0, r=50, t=40, b=0)
            )
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

        with div1:
            # Vertical Divider
            st.markdown('<div style="border-left: 1px solid #f0f2f6; height: 350px; margin-top: 25px;"></div>', unsafe_allow_html=True)

        with col2:
            # Sophisticated Donut Chart
            fig1 = px.pie(
                df,
                names="category",
                values="total",
                hole=0.7,  # Larger hole for cleaner look
                color_discrete_sequence=colors
            )
            
            fig1.update_traces(
                textinfo='none', # Hide text labels on slices for cleanliness
                hoverinfo='label+percent',
                marker=dict(line=dict(color='#FFFFFF', width=2))
            )

            fig1.update_layout(
                height=400,
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
                margin=dict(l=20, r=20, t=60, b=20),
                annotations=[
                    dict(
                        text='Total',
                        x=0.5, y=0.6,
                        font=dict(size=14, color="gray"),
                        showarrow=False
                    ),
                    dict(
                        text=f"<b>₹{total_sum:,.0f}</b>",
                        x=0.5, y=0.45,
                        font=dict(size=22, color="#1f1f1f"),
                        showarrow=False
                    )
                ]
            )
            st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False})


def show_trends(API_URL, headers):
    response = requests.get(f"{API_URL}/expenses/daily-trend", headers=headers)
    
    if response.status_code == 200:
        data = response.json().get("trend", [])
        df = pd.DataFrame(data)

        if df.empty:
            st.info("No data available to display trends.")
            return

        # Data Preparation
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')

        # Create a professional Area Chart
        fig = px.area(
            df,
            x='date',
            y='total_spent',
            title='<b>Daily Spending Velocity</b>',
            labels={'total_spent': 'Amount (₹)', 'date': 'Date'},
            template='plotly_white'  # Clean white background
        )

        # Professional Styling Overrides
        fig.update_traces(
            line_color='#2E5BFF',      # Modern "Fintech" Blue
            line_width=3,
            fillcolor='rgba(46, 91, 255, 0.1)', # Subtle blue tint under the curve
            marker=dict(size=8, color='white', line=dict(width=2, color='#2E5BFF')),
            hovertemplate='<b>Date:</b> %{x}<br><b>Spent:</b> ₹%{y:,.2f}<extra></extra>'
        )

        fig.update_layout(
            font_family="Inter, sans-serif",
            hovermode="x unified",     # Vertical line on hover
            margin=dict(l=0, r=0, t=50, b=0),
            height=400,
            xaxis=dict(
                showgrid=False,
                tickfont=dict(color='gray'),
                title=''
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='#f0f0f0',    # Light gray grid lines
                tickfont=dict(color='gray'),
                title='',
                tickprefix="₹"
            ),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )

        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})