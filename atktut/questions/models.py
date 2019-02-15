from django.db import models
from atktut.commons.models import AbstractModel
from atktut.course.models import Lesson


# Create your models here.
class Question(AbstractModel):
    TRUEFALSE = 'TF'
    MULTICHOICE = 'MC'
    SINGLECHOICE = 'SC'
    BLANKQUESTION = 'BQ'
    QUESTION_TYPE = (
        (TRUEFALSE, 'True Or False'),
        (MULTICHOICE, 'Multi Choice'),
        (SINGLECHOICE, 'Single Choice'),
        (BLANKQUESTION, 'Blank Question'),
    )
    content = models.TextField()
    question_type = models.CharField(max_length=2, choices=QUESTION_TYPE)
    lesson = models.ForeignKey(Lesson, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.question_type)



class Answer(AbstractModel):
    content = models.CharField(max_length=256)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.content)