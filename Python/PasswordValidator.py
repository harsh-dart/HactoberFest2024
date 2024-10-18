import re
from typing import Tuple, List

# Function to check password length
def check_length(password: str, min_length: int = 8) -> Tuple[bool, str]:
    if len(password) >= min_length:
        return True, ""
    return False, f"Password should be at least {min_length} characters long."

# Function to check for at least one lowercase letter
def check_lowercase(password: str) -> Tuple[bool, str]:
    if re.search(r'[a-z]', password):
        return True, ""
    return False, "Password should contain at least one lowercase letter."

# Function to check for at least one uppercase letter
def check_uppercase(password: str) -> Tuple[bool, str]:
    if re.search(r'[A-Z]', password):
        return True, ""
    return False, "Password should contain at least one uppercase letter."

# Function to check for at least one digit
def check_digit(password: str) -> Tuple[bool, str]:
    if re.search(r'[0-9]', password):
        return True, ""
    return False, "Password should contain at least one digit."

# Function to check for at least one special character
def check_special_char(password: str) -> Tuple[bool, str]:
    special_characters = r'[@$!%*?&]'
    if re.search(special_characters, password):
        return True, ""
    return False, "Password should contain at least one special character (@, $, !, %, *, ?, &)."

# Function to run all checks and return a list of validation results
def run_password_checks(password: str) -> List[Tuple[bool, str]]:
    checks = [
        check_length(password),
        check_lowercase(password),
        check_uppercase(password),
        check_digit(password),
        check_special_char(password),
    ]
    return checks

# Main function to validate the password
def validate_password(password: str) -> str:
    validation_results = run_password_checks(password)
    
    # Collect all the error messages if validation fails
    errors = [error for valid, error in validation_results if not valid]

    # If errors exist, return them; otherwise, confirm the password is valid
    if errors:
        return "\n".join(errors)
    return "Password is valid."

# Test the password validator with input
if __name__ == "__main__":
    password = input("Enter your password: ")
    result = validate_password(password)
    print(result)
