import streamlit as st
import data as d

st.markdown(
    "<h1 style='text-align: center;'>Boredom Breaker</h1>",
    unsafe_allow_html=True
)

if "activity" not in st.session_state:
    st.session_state.activity = d.quest()

st.markdown(
    f"""
    <div style="
        padding: 25px; 
        background-color: white; 
        border-radius: 15px; 
        border: 1px solid #ddd; 
        margin-top: 30px;
        min-height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
    ">
        <h3 style='text-align: center; color: black;'>{st.session_state.activity}</h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

col1, col2, col3 = st.columns([4, 2, 4])
with col2:
    if st.button("New Activity"):
        st.session_state.activity = d.quest()