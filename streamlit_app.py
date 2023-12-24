import streamlit as st

# Define the bottles data
bottles = [
    {"name": "Blanc de Noirs, Domaine Armand Heitz", "acid": 50, "tanin": 20, "douceur": 0, "corps": 20, "alcool": 40},
    {"name": "Bourgogne Blanc, Domaine Armand Heitz", "acid": 50, "tanin": 0, "douceur": 0, "corps": 20, "alcool": 40},
    {"name": "1er Cru Passetemps, Domaine de Villaine", "acid": 100, "tanin": 70, "douceur": 0, "corps": 90, "alcool": 40},
    {"name": "Pernand-Vergelesses En Caradeux, Maison Champy", "acid": 100, "tanin": 0, "douceur": 0, "corps": 50, "alcool": 40},
    {"name": "1er Cru Ile des Vergelesses, Domaine Pavelot", "acid": 100, "tanin": 50, "douceur": 0, "corps": 50, "alcool": 40},
    {"name": "Les Grèves, Domaine de la Vougeraie", "acid": 100, "tanin": 50, "douceur": 0, "corps": 50, "alcool": 40},
    {"name": "Château Montrose", "acid": 100, "tanin": 100, "douceur": 0, "corps": 90, "alcool": 40},
    {"name": "Château Mouton Rothshild", "acid": 10, "tanin": 100, "douceur": 0, "corps": 90, "alcool": 80}
]

def calculate_variance(user_preferences, bottle):
    variance = sum(abs(user_preferences[criteria] - bottle[criteria]) for criteria in user_preferences)
    return variance

def find_best_match(bottles, user_preferences):
    variance_scores = [(bottle["name"], calculate_variance(user_preferences, bottle)) for bottle in bottles]
    sorted_bottles = sorted(variance_scores, key=lambda x: x[1])
    return sorted_bottles

# Streamlit app
st.title("Wine Preference Quiz")

# Initialize current question in session state
if 'current_question' not in st.session_state:
    st.session_state['current_question'] = 'acid'

# Function to go to the next question
def next_question(next_q):
    st.session_state['current_question'] = next_q

# Question sequence
if st.session_state['current_question'] == 'acid':
    acid = st.number_input("Acidity", 0, 100, 50, step=1)
    if st.button('Next - Tanin'):
        st.session_state['acid'] = acid
        next_question('tanin')

elif st.session_state['current_question'] == 'tanin':
    tanin = st.number_input("Tanin", 0, 100, 50, step=1)
    if st.button('Next - Douceur'):
        st.session_state['tanin'] = tanin
        next_question('douceur')

elif st.session_state['current_question'] == 'douceur':
    douceur = st.number_input("Douceur", 0, 100, 50, step=1)
    if st.button('Next - Corps'):
        st.session_state['douceur'] = douceur
        next_question('corps')

elif st.session_state['current_question'] == 'corps':
    corps = st.number_input("Corps", 0, 100, 50, step=1)
    if st.button('Next - Alcool'):
        st.session_state['corps'] = corps
        next_question('alcool')

elif st.session_state['current_question'] == 'alcool':
    alcool = st.number_input("Alcool", 0, 100, 50, step=1)
    if st.button('Find Best Match'):
        st.session_state['alcool'] = alcool
        user_preferences = {
            "acid": st.session_state['acid'],
            "tanin": st.session_state['tanin'],
            "douceur": st.session_state['douceur'],
            "corps": st.session_state['corps'],
            "alcool": st.session_state['alcool']
        }
        best_match = find_best_match(bottles, user_preferences)
        st.write("Top Matching Bottles:")
        for bottle in best_match[:3]:
            st.write(f"Bottle: {bottle[0]}, Variance Score: {bottle[1]}")
