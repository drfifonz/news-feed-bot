def process_message(text):
    """Processing user input, returning proper response"""
    formatted_message = text.lower().strip()
    if formatted_message == "test":
        response = "Test successful"
    return response
