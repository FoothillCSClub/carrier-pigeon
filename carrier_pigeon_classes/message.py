
"""
Class for encapsulating text messages
"""
import json

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
        return json.dumps(self.text)

    def deserialize(string):
        obj = json.loads(string)
        objtype = type(obj)
        if objtype != str:
            raise TypeError("JSON decode yields wrong object type: expected str, got " + objtype)
        return Message(obj)
