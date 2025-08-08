import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def generate_response(user_input):
    # Process input with spaCy
    doc = nlp(user_input.lower())

    # Extract lemmas from the input for more flexible matching
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

# Example test
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    print("Bot:", generate_response(user_input))
