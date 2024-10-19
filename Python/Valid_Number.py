class Solution:
    def isNumber(self, s: str) -> bool:
        # Define state transitions for the finite state machine
        transitions = {
            'Start': {'digit': 'Integer', 'sign': 'Sign', 'dot': 'Dot'},
            'Sign': {'digit': 'Integer', 'dot': 'Dot'},
            'Integer': {'digit': 'Integer', 'dot': 'Fraction', 'e': 'Exponent'},
            'Dot': {'digit': 'Fraction'},
            'Fraction': {'digit': 'Fraction', 'e': 'Exponent'},
            'Exponent': {'digit': 'Exp_number', 'sign': 'Exp_sign'},
            'Exp_sign': {'digit': 'Exp_number'},
            'Exp_number': {'digit': 'Exp_number'}
        }
        
        # Define valid ending states for a valid number
        valid_end_states = {'Integer', 'Fraction', 'Exp_number'}

        # Function to determine the type of character
        def get_char_type(char):
            if char.isdigit():
                return 'digit'
            if char in '+-':
                return 'sign'
            if char in 'eE':
                return 'e'
            if char == '.':
                return 'dot'
            return None  # Invalid character

        # Start in the 'Start' state
        current_state = 'Start'

        # Process each character in the input string
        for char in s:
            char_type = get_char_type(char)  # Get the character type
            # If the character type is invalid or not allowed from the current state
            if not char_type or char_type not in transitions[current_state]:
                return False
            # Move to the next state based on the current state and character type
            current_state = transitions[current_state][char_type]

        # Check if the final state is one of the valid end states
        return current_state in valid_end_states


# Test cases
solution = Solution()

# Example test cases
print(solution.isNumber("0"))        # Output: True
print(solution.isNumber("e"))        # Output: False
print(solution.isNumber("."))        # Output: False
print(solution.isNumber("3.14"))     # Output: True
print(solution.isNumber("-42"))      # Output: True
print(solution.isNumber("1e10"))     # Output: True
print(solution.isNumber("1E-10"))    # Output: True
print(solution.isNumber("+.8"))       # Output: True
print(solution.isNumber("-.5e2"))     # Output: True
print(solution.isNumber("+-5"))       # Output: False
print(solution.isNumber("12e"))       # Output: False
print(solution.isNumber("1.2.3"))     # Output: False

