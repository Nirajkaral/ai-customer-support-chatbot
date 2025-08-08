# Install and load spaCy
!pip install -U spacy
!python -m spacy download en_core_web_sm

import spacy
import ipywidgets as widgets
from IPython.display import display, clear_output

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Chatbot logic
def generate_response(user_input):
    doc = nlp(user_input.lower())
    lemmas = [token.lemma_ for token in doc]

    if "hello" in lemmas or "hi" in lemmas:
        return "Hello! How can I assist you today?"

    elif "refund" in lemmas:
        return "To request a refund, please go to your orders and click 'Request Refund'."

    elif "cancel" in lemmas and "order" in lemmas:
        return "To cancel your order, visit your orders page and select 'Cancel'."

    elif "contact" in lemmas or "email" in lemmas:
        return "You can contact us at support@example.com"

    elif "problem" in lemmas or "issue" in lemmas:
        return "I'm sorry to hear that. Can you describe the issue in more detail?"

    else:
        return "Sorry, I didn't understand that. Could you please rephrase your question?"

# Widgets: Input box and Submit button
input_box = widgets.Text(
    placeholder='Type your query here...',
    description='Your Query:',
    disabled=False
)

submit_button = widgets.Button(
    description='Submit',
    button_style='primary'
)

output_box = widgets.Output()

# Button click event
def on_submit_clicked(b):
    user_input = input_box.value.strip()
    with output_box:
        clear_output()
        if user_input == "":
            print("Please enter a query.")
        elif user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye!")
        else:
            print(f"You: {user_input}")
            print("Bot:", generate_response(user_input))
        input_box.value = ""

# Connect button to function
submit_button.on_click(on_submit_clicked)

# Display UI
display(input_box, submit_button, output_box)
