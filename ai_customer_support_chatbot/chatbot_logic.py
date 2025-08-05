import spacy

nlp = spacy.load("en_core_web_sm")

def generate_response(user_input):
    user_input = user_input.lower()
    doc = nlp(user_input)

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"

    elif "refund" in user_input:
        return "To request a refund, please go to your orders and click 'Request Refund'."

    elif "cancel order" in user_input:
        return "To cancel your order, visit your orders page and select 'Cancel'."

    elif "contact" in user_input or "email" in user_input:
        return "You can contact us at support@example.com"

    elif "problem" in user_input or "issue" in user_input:
        return "I'm sorry to hear that. Can you describe the issue in more detail?"

    else:
        return "Sorry, I didn't understand that. Could you please rephrase your question?"
