from rest_framework import serializers
from .models import Answer_option, Answer, Question_set, Question_type, Question, QuizParticipant


class UserSerializer(serializers.ModelSerializer):
    """
    USER SERIALIZER
    """

    class Meta:
        model = QuizParticipant
        fields = ['user_number']

class QuestionSetSerializer(serializers.ModelSerializer):
    """
    QUESTION SET SERIALIZER
    """

    class Meta:
        model = Question_set
        fields = ["title", "start_date", "end_date"]

class QuestionTypeSerializer(serializers.ModelSerializer):
    """
    QUESTION TYPE SERIALIZER
    """
    class Meta:
        model = Question_type
        fields = ["type"] 

class SaveSerializer(serializers.Serializer):
    """
    SAVE QUESTION SERIALIZER
    """
    question = serializers.IntegerField()
    freetext = serializers.CharField(max_length=500)
    option = serializers.IntegerField()
    user = serializers.IntegerField()

class AnswerOptionSerializer(serializers.ModelSerializer):
    """
    ANSWER OPTION SERIALIZER
    """
    class Meta:
        model = Answer_option
        fields = ["id", "text"]


class QuestionSerializer(serializers.ModelSerializer):
    """
    QUESTION SERIALIZER
    """
    type = QuestionTypeSerializer(read_only=True)
    set = QuestionSetSerializer(read_only=True)
    
    class Meta:
        model = Question
        fields = ["id", "type", "set", "text"]


class AnswerSerializer(serializers.ModelSerializer):
    """
    ANSWER SERIALIZER
    """
    question = QuestionSerializer(read_only=True)
    option = AnswerOptionSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ('user', 'question', 'option')



