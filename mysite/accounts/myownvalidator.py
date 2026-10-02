
from django.core.exceptions import ValidationError

class CheckSpecialChracters():

    def validate(self, password, user=None):
        special_characters = "[$€£!?@+-*_.()%]"
        if not any(char in special_characters for char in password):
            raise ValidationError(('Password must contain at least 1 special character.'))

    def get_help_text(self):
        return "Your password must contain at least 1 special character ($ € £ ! ? @ + - * _ . ( ) %)."
