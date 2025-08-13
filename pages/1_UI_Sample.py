import streamlit as st
import pandas as pd
import time
import plotly.express as px
import numpy as np
from utils.data import generate_cost_data

st.set_page_config(
    page_title="UI Sample",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🎨 Various UI Componeents")

col1, col2 = st.columns(2)
with col1:
    # Data를 차트에 시간에 따라 업데이트하는 샘플
    st.subheader("📊 Time series data")
    df = pd.DataFrame(np.random.randn(15, 3), columns=(["A", "B", "C"]))
    my_data_element = st.line_chart(df) # Chart 컴포넌트 생성

    for tick in range(10):
        time.sleep(.5)
        add_df = pd.DataFrame(np.random.randn(1, 3), columns=(["A", "B", "C"]))
        my_data_element.add_rows(add_df) # Chart 컴포넌트에 데이터 추가

    st.button("Regenerate")

with col2:
    # Data를 Pie 차트에 표시
    cost_df = generate_cost_data()
    st.subheader("💸 Cost by Service")
    service_costs = cost_df.groupby('service')['cost'].sum().sort_values(ascending=False)

    fig_services = px.pie(
        values=service_costs.values,
        names=service_costs.index,
        title="Cost Distribution by Service",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig_services.update_layout(height=400)
    st.plotly_chart(fig_services, use_container_width=True)