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
if 'current_question_index' not in st.session_state:
    st.session_state['current_question_index'] = 0
    st.session_state['preferences'] = {}

# Define the questions
questions = [
    {"label": "Acidity", "key": "acid"},
    {"label": "Tanin", "key": "tanin"},
    {"label": "Douceur", "key": "douceur"},
    {"label": "Corps", "key": "corps"},
    {"label": "Alcool", "key": "alcool"}
]

# Function to handle the next question
def handle_next():
    if st.session_state['current_question_index'] < len(questions) - 1:
        st.session_state['current_question_index'] += 1
    else:
        st.session_state['completed'] = True

# Show current question
if st.session_state['current_question_index'] < len(questions):
    question = questions[st.session_state['current_question_index']]
    value = st.number_input(question['label'], 0, 100, 50, step=1, key=question['key'])
    if st.button('Next', key=f'next_{question["key"]}'):
        st.session_state['preferences'][question['key']] = value
        handle_next()

# Show results if all questions are answered
if 'completed' in st.session_state and st.session_state['completed']:
    user_preferences = st.session_state['preferences']
    best_match = find_best_match(bottles, user_preferences)
    st.write("Top Matching Bottles:")
    for bottle in best_match[:3]:
        st.write(f"Bottle: {bottle[0]}, Variance Score: {bottle[1]}")

# Reset quiz
if st.button('Reset Quiz'):
    st.session_state['current_question_index'] = 0
    st.session_state['preferences'] = {}
    st.session_state['completed'] = False
