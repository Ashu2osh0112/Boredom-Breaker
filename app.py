import streamlit as st
import data as d

# Page title
st.markdown(
    "<h1 style='text-align: center;'>Boredom Breaker</h1>",
    unsafe_allow_html=True
)

# Load activity only once when app starts
if "activity" not in st.session_state:
    st.session_state.activity = d.quest()

# Activity display box
st.markdown(
    f"""
    <div style="
        padding: 25px; 
        background-color: white; 
        border: 6px solid; 
        border-image: linear-gradient(90deg, violet, indigo, blue, green, yellow, orange, red) 1;
        border-radius: 15px; 
        margin-bottom: 20px;
        min-height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
    ">
        <h3 style='text-align: center; color: black;'>{st.session_state.activity}</h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.write("")

# Button to update the activity
col1, col2, col3 = st.columns([4, 2, 4])
with col2:
    if st.button("New Activity"):
        st.session_state.activity = d.quest()