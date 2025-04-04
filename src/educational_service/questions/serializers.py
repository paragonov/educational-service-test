from rest_framework import serializers


class AnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField()


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    answers = AnswerSerializer(many=True)
    right_answers = AnswerSerializer(many=True)


class TestCaseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    questions = QuestionSerializer(many=True)


class ThemeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    test_cases = TestCaseSerializer(many=True)


class TestCaseResultsSerializer(serializers.Serializer):
    test_case_id = serializers.IntegerField()
    question_id = serializers.IntegerField()
    answer_id = serializers.IntegerField()


class TestCaseResultsStatisticSerializer(serializers.Serializer):
    test_case_id = serializers.IntegerField()
    question = QuestionSerializer()
    answer = AnswerSerializer()
    is_right = serializers.BooleanField()
