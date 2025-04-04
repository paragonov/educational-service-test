from rest_framework import generics, status
from rest_framework.response import Response

from educational_service.authentication.backends import CustomTokenAuthentication
from educational_service.questions.models import TestCase, Theme, Answer, Question, TestCaseResults
from educational_service.questions.serializers import ThemeSerializer, TestCaseResultsSerializer, AnswerSerializer, TestCaseResultsStatisticSerializer


class ThemeList(generics.ListAPIView):
    authentication_classes = [CustomTokenAuthentication]
    serializer_class = ThemeSerializer

    def get_queryset(self):
        return Theme.objects.all()

    def list(self, request, *args, **kwargs):
        return Response(self.serializer_class(self.get_queryset(), many=True).data)


class TestCaseResultsView(generics.CreateAPIView):
    authentication_classes = [CustomTokenAuthentication]
    serializer_class = TestCaseResultsSerializer

    def create(self, request, *args, **kwargs):
        user = request.user

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        test_case = TestCase.objects.filter(id=validated_data['test_case_id']).first()
        question = Question.objects.filter(id=validated_data['question_id']).first()
        current_answer = Answer.objects.filter(id=validated_data['answer_id']).first()

        detail = None
        if not test_case:
            detail = f"Test case with id {validated_data['test_case_id']}"
        elif not question:
            detail = f"Question with id {validated_data['question_id']}"
        elif not current_answer:
            detail = f"Answer with id {validated_data['answer_id']}"

        if detail:
            return Response(
                data={"detail": f"{detail} does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        is_right = True if current_answer in test_case.questions.filter(id=question.id).first().right_answers.all() else False

        _, is_created = TestCaseResults.objects.get_or_create(
            user=user,
            test_case=test_case,
            question=question,
            defaults={'answer': current_answer, 'is_right': is_right}
        )
        if not is_created:
            return Response({"detail": "Answer already exists"}, status=status.HTTP_409_CONFLICT)

        return Response(
            {
                "is_right": is_right,
                "current_answer": AnswerSerializer(current_answer).data,
                "right_answers": AnswerSerializer(question.right_answers.all(), many=True).data,
            }
        )


class TestCaseResultsStatisticView(generics.RetrieveAPIView):
    authentication_classes = [CustomTokenAuthentication]
    serializer_class = TestCaseResultsStatisticSerializer

    def get_queryset(self, user, test_case_id):
        return TestCaseResults.objects.filter(user=user, test_case_id=test_case_id)

    def retrieve(self, request, *args, **kwargs):
        test_case_id = request.GET.get('test_case')
        user = request.user

        queryset = self.get_queryset(user, test_case_id)
        is_complete = True
        for instance in queryset:
            if instance.is_right is False:
                is_complete = False

        return Response(
            {
                "results": self.serializer_class(queryset, many=True).data,
                "is_complete": is_complete,
            }
        )
