from django.db import models


class CseEndeavour(models.Model):
    label = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.label
    
    class Meta:
        ordering = ['label']


class ComputerScienceEducatorsPost(models.Model):
    class PostType(models.TextChoices):
        QUESTION = 'QS', 'Question'
        ANSWER = 'AN', 'Answer'
        COMMENT = 'CM', 'Comment'

    stack_exchange_id = models.IntegerField(unique=True)
    type = models.CharField(
        max_length=2,
        choices=PostType.choices,
        default=PostType.QUESTION,
    )
    text = models.TextField()
    label = models.ForeignKey(CseEndeavour, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    @property
    def unique_id(self):
        return f'red_${self.id}'
    
    def __str__(self):
        return f'${self.text[:20]}...'

    class Meta:
        ordering = ['stack_exchange_id']
