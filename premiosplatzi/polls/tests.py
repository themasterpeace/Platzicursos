import datetime 

from django.test import TestCase
from django.utils import timezone

from .models import Question
#Models 
#Vistas 

class QuestionModelTest(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        """was_published_recently returns False for question whose pud_date is in the future """
        time = timezone.now() + datetime.delta(days=30)
        future_question = Question(question_text="¿Quien es el mejor CD de Platzi?")
        self.assertIs(future_question.was_published_recently(), False)