# Function to calculate password strength score
def check_password_strength(password):
    score = 0

    # Check for length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1

    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1

    # Check for digits
    if any(char.isdigit() for char in password):
        score += 1

    # Check for special characters
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if any(char in special_characters for char in password):
        score += 1

    return score
    
    










