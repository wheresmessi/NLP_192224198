class FiniteStateAutomaton:
    def __init__(self):
        self.state = 0  # Initial state

    def transition(self, char):
        """Defines state transitions"""
        if self.state == 0:
            self.state = 1 if char == 'a' else 0
        elif self.state == 1:
            self.state = 2 if char == 'b' else 1 if char == 'a' else 0
        elif self.state == 2:
            self.state = 2 if char == 'b' else 1 if char == 'a' else 0

    def is_accepting(self):
        """Checks if the final state is an accepting state"""
        return self.state == 2

    def recognize(self, string):
        """Processes the input string through the FSA"""
        self.state = 0  # Reset to initial state
        for char in string:
            self.transition(char)
        return self.is_accepting()


# Testing the finite state automaton
fsa = FiniteStateAutomaton()

test_strings = ["ab", "aab", "bbab", "baba", "abc", "aabb"]
for s in test_strings:
    result = "Accepted" if fsa.recognize(s) else "Rejected"
    print(f"String '{s}': {result}")
