from datetime import timezone
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model =Task
        fields =('id' ,'title' ,'description' ,'status_choices', 'status','due_date' ,'user')



        def validate_due_date(self, value):
            if value < timezone.now().date():
                raise serializers.ValidationError("Due date must be in the future.")
            return value