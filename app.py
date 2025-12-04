import data as d
import streamlit as st

st.markdown(
    "<h1 style='text-align: center;'>Boredom Breaker</h1>",
    unsafe_allow_html=True
)

activity = d.quest()

st.markdown(
    f"""
    <div style="padding: 25px; background-color: white; border-radius: 15px; 
                border: 1px solid #ddd; margin-bottom: 20px;">
        <h3 style='text-align: center; color: black;'>{activity}</h3>
    </div>
    """,
    unsafe_allow_html=True
)

