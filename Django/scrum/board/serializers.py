
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Sprint,Task

User = get_user_model()



class UserSerializer(serializers.ModelSerializer):
	full_name = serializers.CharField(source='get_full_name',read_only=True)
	links = serializers.SerializerMethodField()
	class Meta:
		model = User
		field = ('id',User.USERNAME_FIELD,'full_name','is_active',)
	def get_links(self,obj):
		 request = self.context['request']
		 username = obj.get_username()
		 return {
			 'self': reverse('user-detail',
			 	kwargs={User.USERNAME_FIELD:username},request=request)
		 }

class TaskSerializer(serializers.ModelSerializer):
	
	assigned = serializers.SlugRelatedField(
		slug_field=User.USERNAME_FIELD,required=False,allow_null = True,
		queryset = User.objects.all()
	)

	status_display = serializers.SerializerMethodField()
	links = serializers.SerializerMethodField()

	class Meta:
		model = Task
		field = ('id','name','description','sprint','status',
		'order','assigned','started','due','completed',)
	
	def get_status_display(self,obj):
		return obj.get_status_display()

	def get_links(self,obj):
		request = self.context['request']
		links =  {
			 'self': reverse('task-detail',
			 	kwargs={'pk':obj.pk},request=request),
			'sprintf':None,
			'assigned':None
		}
		if obj.sprint_id:
			links['sprint'] = reverse('sprint-detail',
				kwargs={'pk':obj.sprint_id},request=request)
		if obj.assigned:
			links['assigned'] = reverse('user-detail',
				kwargs={User.USERNAME_FIELD:obj.assigned},request=request)
		return links

class SprintSerializer(serializers.ModelSerializer):
	
	links = serializers.SerializerMethodField()

	class Meta:
		model = Sprint
		field = ('id','name','description','end',)
	def get_links(self,obj):
		 request = self.context['request']
		 return {
			 'self': reverse('sprint-detail',
			 	kwargs={'pk':obj.pk},request=request)
		 }