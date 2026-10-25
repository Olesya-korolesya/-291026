# #Задание 1
# from django.db import models
#
# class Contact(models.Model):
#     name = models.CharField(
#         max_length=100, verbose_name="Имя"
#     )
#     email = models.EmailField(
#         verbose_name="Электронная почта"
#     )
#     message = models.TextField(
#         verbose_name="Сообщение"
#     )
#     created_at = models.DateTimeField(
#         auto_now_add=True, verbose_name="Дата отправки сообщения"
#     )
#
#     class Meta:
#         verbose_name = "Обратная связь"
#         verbose_name_plural = "Обратная связь"
#         ordering = ["-created_at"]
#
#     def __str__(self):
#         return f"Сообщение от {self.name} ({self.email})"

# # Задание 2
#
# from django.db import models
#
# class Feedback(models.Model):
#     name = models.CharField(max_length=100, verbose_name="Ваше имя")
#     email = models.EmailField(verbose_name="Электронная почта")
#     message = models.TextField(verbose_name="Сообщение")
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Сообщение от {self.name} ({self.email})"

# # Задание 3
#
# from django.db import models
#
# class Feedback(models.Model):
#
#     name = models.CharField(
#         max_length=100,
#         verbose_name="Имя"
#     )
#
#     email = models.EmailField(
#         verbose_name="Электронная почта"
#     )
#
#     message = models.TextField(
#         verbose_name="Сообщение"
#     )
#
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name="Дата отправки"
#     )
#
#     class Meta:
#         verbose_name = "Обратная связь"
#         verbose_name_plural = "Обратная связь"
#         ordering = ['-created_at']
#
#     def __str__(self):
#         return f"Сообщение от {self.name} ({self.email})"