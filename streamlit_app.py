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

# Initialize session state
if 'init' not in st.session_state:
    st.session_state['current_question'] = 'acid'
    st.session_state['init'] = True  # Flag to indicate initialization is done

# Function to go to the next question
def next_question(current_value, next_q):
    st.session_state[st.session_state['current_question']] = current_value
    st.session_state['current_question'] = next_q

# Display questions based on current state
if st.session_state['current_question'] == 'acid':
    acid = st.number_input("Acidity", 0, 100, 50, step=1, key='acid')
    if st.button('Next - Tanin'):
        next_question(acid, 'tanin')

elif st.session_state['current_question'] == 'tanin':
    tanin = st.number_input("Tanin", 0, 100, 50, step=1, key='tanin')
    if st.button('Next - Douceur'):
        next_question(tanin, 'douceur')

elif st.session_state['current_question'] == 'douceur':
    douceur = st.number_input("Douceur", 0, 100, 50, step=1, key='douceur')
    if st.button('Next - Corps'):
        next_question(douceur, 'corps')

elif st.session_state['current_question'] == 'corps':
    corps = st.number_input("Corps", 0, 100, 50, step=1, key='corps')
    if st.button('Next - Alcool'):
        next_question(corps, 'alcool')

elif st.session_state['current_question'] == 'alcool':
    alcool = st.number_input("Alcool", 0, 100, 50, step=1, key='alcool')

# "Find Best Match" button appears after all preferences are set
if 'alcool' in st.session_state:
    if st.button('Find Best Match'):
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
