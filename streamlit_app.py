# main_app.py

import streamlit as st
from wine_data import wine_data  # Importing the wine data

def rate_wine():
    # Access the current characteristic
    characteristic = wine_data[st.session_state.current_characteristic]
    st.write(f"Rate the {characteristic['characteristic']}:")
    rating = st.slider("", characteristic["scale"][0], characteristic["scale"][1], 50)

    if st.button("Next"):
        # Store the rating and proceed to the next characteristic
        st.session_state.ratings[characteristic['characteristic']] = rating
        st.session_state.current_characteristic += 1

def main():
    if 'current_characteristic' not in st.session_state:
        st.session_state.current_characteristic = 0
    if 'ratings' not in st.session_state:
        st.session_state.ratings = {}

    st.title("Wine Rating App")

    if st.session_state.current_characteristic < len(wine_data):
        rate_wine()
    else:
        st.write("Wine rating completed!")
        st.write("Your ratings:", st.session_state.ratings)
        if st.button("Restart Rating"):
            st.session_state.current_characteristic = 0
            st.session_state.ratings = {}

if __name__ == "__main__":
    main()
