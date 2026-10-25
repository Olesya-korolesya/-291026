# #Задание 1
# from django.contrib import messages
# from django.shortcuts import redirect, render
# from .forms import ContactForm
#
# def contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Ваше сообщение отправлено!")
#             return redirect("contact")
#     else:
#         form = ContactForm()
#
#     return render(request, "contact.html", {"form": form})

# # Задание 2
# from django.shortcuts import render, redirect
# from .forms import FeedbackForm
#
# def feedback_view(request):
#     if request.method == 'POST':
#
#         form = FeedbackForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('blog:success_url')
#     else:
#
#         form = FeedbackForm()
#
#     return render(request, 'feedback.html', {'form': form})
#
# def success_view(request):
#     return render(request, 'success.html')


# # Задание 3
#
# from django.shortcuts import render, redirect
# from .forms import FeedbackForm
#
# def my_view(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#
#             pass
#         else:
#
#             for field_name, errors in form.errors.items():
#                 if field_name != '__all__':
#                     form.fields[field_name].widget.attrs.update({
#                         'class': form.fields[field_name].widget.attrs.get('class', '') + ' is-invalid'
#                     })
#     else:
#         form = FeedbackForm()
#
#     return render(request, 'my_template.html', {'form': form})
