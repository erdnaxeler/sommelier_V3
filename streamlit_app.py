# main_app.py

import streamlit as st
from wine_data import wine_data  # Make sure to have the wine_data.py as previously defined

def main():
    # Initialize session state variables
    if 'current_characteristic_index' not in st.session_state:
        st.session_state.current_characteristic_index = 0
    if 'ratings' not in st.session_state:
        st.session_state.ratings = {}
    if 'init' not in st.session_state:
        st.session_state.init = True  # New flag for the initial state

    st.title("Wine Rating App")

    # Handling the first interaction separately
    if st.session_state.init:
        if st.button("Start Rating"):
            st.session_state.init = False
    else:
        # Display questions after starting the rating
        if st.session_state.current_characteristic_index < len(wine_data):
            characteristic = wine_data[st.session_state.current_characteristic_index]
            st.write(f"Rate the {characteristic['characteristic']}:")
            rating = st.slider("", characteristic["scale"][0], characteristic["scale"][1], 50, key=characteristic['characteristic'])

            if st.button('Next', key=f'next_{characteristic["characteristic"]}'):
                st.session_state.ratings[characteristic['characteristic']] = rating
                st.session_state.current_characteristic_index += 1

        # Check for completion of the rating process
        if st.session_state.current_characteristic_index >= len(wine_data):
            st.write("Wine rating completed!")
            st.write("Your ratings:", st.session_state.ratings)
            if st.button("Restart Rating"):
                st.session_state.current_characteristic_index = 0
                st.session_state.ratings = {}
                st.session_state.init = True  # Reset to initial state

if __name__ == "__main__":
    main()
