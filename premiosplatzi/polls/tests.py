import datetime 

from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone

from .models import Question
#Models 
#Vistas 

class QuestionModelTests(TestCase):
    
    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for question whose pud_date is in the future """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quien es el mejor CD de Platzi?")
        self.assertIs(future_question.was_published_recently(), False)

def create_question(question_text, days):
    """
    Create a question with de given "question_test". and published the given
    number of days offset to now (negative for question published in the past,
    positive for question that have yet to be published)
    """        
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=timezone.now())

class QuestionIndexViewTests(TestCase):
    
    def test_now_questions(self):
        """"If no question exist, an appropiate message is displayed """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
        
    def test_future_question(self):
        """ 
        Questions with a pub_date in thee future aren´t displayed on the index page
        """
        create_question("Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
    
    def test_past_question(self):
        """ 
        Question with a pub_date in the past are displayed on the index page 
        """
        question = create_question("Past question", days=-10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])
        
    def test_future_question_and_past_question(self):
        """ 
        Even if both past and future question exist, only past questions are displayed
        """
        past_question = create_question(question_text="Past questions", days=-30)
        future_question = create_question(question_text="Future questions", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"], 
            [past_question]
            )
        
        
    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions. 
        """
        past_question1 = create_question(question_text="Past questions 1", days=-30)
        past_question2 = create_question(question_text="Past questions 2", days=-40)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [past_question1, past_question2]                         
        )
        
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future 
        return a 404 error nor found
        """
        future_question = create_question(question_text="Future questions", days=30)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertAlmostEqual(response.status_code, 404)
           
    def test_past_question(self):
        """
        The detail view of a question with a pud_date in the past
        displays the question´s text 
        """
        past_question = create_question(question_text="Past questions", days=-30)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertAlmostContains(response, past_question.question_text)
        
        
        