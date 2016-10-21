
"""
Class for encapsulating text messages
"""

class Message:
    def __init__(self, text = ""):
        self.text = text

    def __str__(self):
        return self.text

    def __len__(self):
        return len(self.text)
