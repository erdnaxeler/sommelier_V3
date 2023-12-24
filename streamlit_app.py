import streamlit as st

import streamlit as st

# Define the bottles data
bottles = [
    # ... (same as before)
]

# Function definitions remain the same

def calculate_variance(user_preferences, bottle):
    # ... (same as before)

def find_best_match(bottles, user_preferences):
    # ... (same as before)

# Streamlit app
st.title("Wine Preference Matcher")

# User inputs using sliders
st.sidebar.header("User Preferences")
acid = st.sidebar.slider("Acidity", 0, 100, 50)
tanin = st.sidebar.slider("Tanin", 0, 100, 50)
douceur = st.sidebar.slider("Douceur", 0, 100, 50)
corps = st.sidebar.slider("Corps", 0, 100, 50)
alcool = st.sidebar.slider("Alcool", 0, 100, 50)

user_preferences = {
    "acid": acid,
    "tanin": tanin,
    "douceur": douceur,
    "corps": corps,
    "alcool": alcool
}

# Button to find the best match
if st.button('Find Best Match'):
    best_match = find_best_match(bottles, user_preferences)
    st.write("Top Matching Bottles:")
    for bottle in best_match[:3]:
        st.write(f"Bottle: {bottle[0]}, Variance Score: {bottle[1]}")

# Running the Streamlit app
# To run this app, save the script as a .py file and run `streamlit run your_script.py` from the command line.
