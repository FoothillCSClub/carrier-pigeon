
"""
Class for encapsulating text messages
"""

class Message:
    def __init__(self, text = ""):
        self.text = text

    def __str__(self):
        return self.text

    def __bytes__(self):
        return bytes(self.text, "utf-8")

    def __len__(self):
        return len(self.text)

    def serialize(self):
        return bytes(self.text + "\n", "utf-8")
