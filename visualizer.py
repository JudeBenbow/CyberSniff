import streamlit as st
import pandas as pd
import plotly.express as px
import os
import time

# Set page configuration
st.set_page_config(page_title="CyberSniff Dashboard", layout="wide")

st.title("🛡️ Network Packet Visualizer")
st.write("Real-time analysis of captured network traffic")

# Placeholder for the dashboard content
placeholder = st.empty()

def load_data():
    if os.path.exists("network_log.csv"):
        df = pd.read_csv("network_log.csv")
        # Convert timestamp to actual datetime objects
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        return df
    return None

df = load_data()

# Filtering
st.sidebar.header("Filtering Options")

if df is not None and not df.empty:
    all_protocols = df['Protocol'].unique().tolist()
    selected_protocols = st.sidebar.multiselect(
        "Select Protocol",
        all_protocols,
        default=all_protocols,
        key="protocol_selector_widget" # The "Name Tag"
    )

    # Applying filter to dataframe
    df = df[df['Protocol'].isin(selected_protocols)]

    # Key Metrics
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Total Packets", len(df))
    kpi2.metric("Unique IPs", df['Source'].nunique())

    # Conversion Logic
    total_mb = df['Length'].sum() / (1024 * 1024)
    kpi3.metric("Total Data", f"{total_mb:.2f} MB")

    # Charts
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Protocol Distribution")
        fig_pie = px.pie(df, names='Protocol', hole=0.4,
                            color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig_pie, use_container_width=True, key="protocol_pie_chart")

    with col2:
        st.subheader("Traffic Volume Over Time")
        # Group by second to see spikes
        df_time = df.set_index('Timestamp').resample('s').count()
        fig_line = px.line(df_time, y='Protocol', labels={'Protocol': 'Packets/Sec'})
        st.plotly_chart(fig_line, use_container_width=True, key="traffic_line_chart")
    # Recent Traffic Table
        st.subheader("Recent Packets (Top 10)")
        st.dataframe(df.tail(10).sort_values(by='Timestamp', ascending=False), use_container_width=True)

else:
    st.warning("Waiting for data... Make sure your sniffer.py is running!")

time.sleep(2) # Refresh every 2 seconds
st.rerun()