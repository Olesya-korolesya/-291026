# #Задание 1
# from django import forms
# from .models import Contact
#
#
# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ["name", "email", "message"]
#
#         widgets = {
#             "name": forms.TextInput(
#                 attrs={
#                     "class": "form-control",
#                     "placeholder": "Введите ваше имя",
#                 }
#             ),
#             "email": forms.EmailInput(
#                 attrs={
#                     "class": "form-control",
#                     "placeholder": "name@gmail.com",
#                 }
#             ),
#             "message": forms.Textarea(
#                 attrs={
#                     "class": "form-control",
#                     "placeholder": "Ваше сообщение...",
#                     "rows": 4,
#                 }
#             ),
#         }

# # Задание 2
#
# from django import forms
# from .models import Feedback
#
# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model = Feedback
#
#         fields = ['name', 'email', 'message']
#
#         help_texts = {
#             'email': 'Мы не передаём Ваши данные.',
#         }

# #Задание 3
#
# from django import forms
# from .models import Feedback
#
# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         fields = ['name', 'email', 'message']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'message': forms.Textarea(attrs={'class': 'form-control'}),
#         }