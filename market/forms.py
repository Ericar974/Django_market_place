from django.forms import ModelForm
from market.models import Test


class TestForm(ModelForm):
	class Meta:
		model = Test
		fields = ('date', 'text', 'price', 'img', 'stock', 'description')