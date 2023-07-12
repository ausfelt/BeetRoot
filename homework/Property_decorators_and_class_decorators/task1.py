import re


class Contact:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        self.valid_format = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.match(self.valid_format, self.email):
            raise ValueError("This is not a valid email address.")


my_contact = Contact("linus.ausfelt@gmail.com")

was_error_raised = False
try:
    invalid_contact = Contact("linus.ausfelt.gmail.com")
except ValueError:
    was_error_raised = True

assert was_error_raised

another_invalid_contact = Contact("linus.com")
