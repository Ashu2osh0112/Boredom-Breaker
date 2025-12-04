# ⭐ Boredom Breaker

Boredom Breaker is a small Streamlit web app that shows fun random activities.  
It uses the Bored API to fetch a new activity every time you click the button.

---

## 🚀 Features

- Shows a random activity on page load  
- Click **New Activity** to get a fresh idea  
- Colorful rainbow border for a fun look  
- Simple and clean UI  
- Uses Streamlit + Python  

---

## 🛠️ How It Works

- `data.py` calls the Bored API and returns an activity  
- `app.py` displays the activity in a styled box  
- `session_state` keeps the activity stable until the button is clicked  

---

## ▶️ Run the App

### Install Streamlit:

📌 Files

app.py → Streamlit user interface

data.py → API request function

```bash
pip install streamlit
```

## 📚 API Used

Bored API (App Brewery version):
https://bored-api.appbrewery.com/random
