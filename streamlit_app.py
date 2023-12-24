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
    st.session_state['preferences'] = {}

# Define the questions
questions = {
    'acid': "Acidity",
    'tanin': "Tanin",
    'douceur': "Douceur",
    'corps': "Corps",
    'alcool': "Alcool"
}

# Update question
def update_question():
    questions_list = list(questions.keys())
    current_index = questions_list.index(st.session_state['current_question'])
    if current_index < len(questions_list) - 1:
        st.session_state['current_question'] = questions_list[current_index + 1]
    else:
        st.session_state['current_question'] = 'done'

# Display current question
current_question = st.session_state['current_question']
if current_question != 'done':
    preference = st.number_input(questions[current_question], 0, 100, 50, step=1, key=current_question)
    if st.button('Next'):
        st.session_state['preferences'][current_question] = preference
        if current_question == 'acid':  # Special handling for the first question
            update_question()

# Handle subsequent questions
if 'next_pressed' in st.session_state and st.session_state['next_pressed']:
    update_question()
    st.session_state['next_pressed'] = False

if current_question != 'acid' and st.button('Next', key='next_button'):
    st.session_state['next_pressed'] = True

# "Find Best Match" button appears after all preferences are set
if current_question == 'done':
    if st.button('Find Best Match'):
        user_preferences = st.session_state['preferences']
        best_match = find_best_match(bottles, user_preferences)
        st.write("Top Matching Bottles:")
        for bottle in best_match[:3]:
            st.write(f"Bottle: {bottle[0]}, Variance Score: {bottle[1]}")
