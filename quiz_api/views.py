from django.shortcuts import render
from rest_framework.views import APIView
import datetime
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionSetSerializer, QuestionSerializer, AnswerOptionSerializer, AnswerSerializer, SaveSerializer
from .models import Question_set, Question_type, Question, Answer_option, Answer_option, Answer, QuizParticipant

class SetsView(APIView):
    """
    LIST OF ACTIVE QUESTION SETS
    """
    def get(self, request):
        today = datetime.date.today()
        sets = Question_set.objects.filter(start_date__lte=today, end_date__gte=today)
        serializer = QuestionSetSerializer(sets, many=True)
        return Response({"sets" : serializer.data})

class QuestionView(APIView):
    """
    LIST OF QUESTIONS
    """
    def get(self, request, index):
        question = Question.objects.filter(id=index)
        options = Answer_option.objects.filter(question__id=index)
        q_serializer = QuestionSerializer(question, many=True)
        o_serializer = AnswerOptionSerializer(options, many=True)
        return Response({'question': q_serializer.data, 'options': o_serializer.data})

class UserAnswersView(APIView):
    """
    LIST OF USER ANSWERS
    """
    def get(self, request, user_id):
        answers = Answer.objects.filter(user__user_number=user_id)
        a_serializer = AnswerSerializer(answers, many=True)
        return Response({'answers': a_serializer.data})

class SaveUserAnswerView(APIView):
    """
    SAVE USER ANSWER
    """
    def get(self, request):
        answers = Answer.objects.filter(user__user_number=user_id)
        a_serializer = AnswerSerializer(answers, many=True)
        return Response({'answers': a_serializer.data})

    def post(self, request, *args, **kwargs):
        data = {
            'user': request.data.get('user'),
            'question' : request.data.get('question'),
            'option': request.data.get('option'),
            'freetext': request.data.get('freetext'),
        }
        serializer = SaveSerializer(data=data)
        if serializer.is_valid():
            try:
                user = get_object_or_404(QuizParticipant, user_number=serializer.data['user'])
                option = Answer_option.objects.get(id=serializer.data['option'])
                question = Question.objects.get(id=serializer.data['question'])
                answer=Answer()
                answer.user = user
                answer.option = option
                answer.question = question
                answer.freetext = serializer.data['freetext']
                answer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response(serializer.errors, status=status .HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status .HTTP_400_BAD_REQUEST)

