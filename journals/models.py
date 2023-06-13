from django.utils import timezone
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


from accounts.models import CustomUser


status_list = (
    ('user', 'Foydalanuvchi'),
    ('editor', 'Tahrirlovchi')
)

class Language(models.Model):
	name = models.CharField("Til", max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


	class Meta:
		verbose_name = "Til"
		verbose_name_plural = "Tillar"




class Editor(models.Model):
    editor = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="Tahrirlovchi")
    image = models.ImageField("Avatar", upload_to="editor_image/", default="default.jpg")
    position = models.CharField("Lavozimi", max_length=120)
    bio_short = models.CharField("Bio", max_length=120, null=True, blank=True)
    bio_long = models.TextField(max_length=3000, null=True, blank=True)


    @receiver(post_save, sender=CustomUser)
    def save_editor_profile(sender, instance, **kwargs):
    	if instance.status == 'editor':
    		Editor.objects.create(editor=instance)

    class Meta:
        verbose_name = "Tahrirlovchi"
        verbose_name_plural = 'Tahrirlovchilar'

    def __str__(self):
        return self.editor.first_name + ' ' + self.editor.last_name



class Journal(models.Model):
	name = models.CharField("Nomi", max_length=120)
	image = models.ImageField("Rasmi", upload_to="journal_images/", null=True, blank=True)
	description = models.CharField("Tavsif", max_length=250)
	volume = models.IntegerField(default=1)
	main_editor = models.ForeignKey(Editor, on_delete=models.SET_NULL, null=True, blank=True)
	isbn = models.CharField("ISBN", max_length=50)
	language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
	created_at = models.DateTimeField(default=timezone.now)
	copyright = models.CharField("Litsenziya", max_length=250)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Jurnal"
		verbose_name_plural = "Jurnallar"


class References(models.Model):
	file_url = models.URLField("Fayl url", max_length=250)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.file_url


	class Meta:
		verbose_name = "Referens"
		verbose_name_plural = "Referenslar"


class Article(models.Model):
	journal = models.ForeignKey(Journal, on_delete=models.CASCADE, verbose_name="Jurnal")
	authors = models.ManyToManyField(CustomUser, related_name="users", verbose_name="Mualliflar")
	pages = models.CharField(max_length=50, verbose_name="Safihalar")
	title = models.CharField(max_length=120, verbose_name="Sarlavha")
	abstract = models.TextField(max_length=3000, verbose_name="Abstrakt")
	keywords = models.TextField(max_length=3000, verbose_name="Kalit so'zlar")
	file = models.FileField(upload_to="article_files/")
	references = models.ForeignKey(References, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Referens")
	editor = models.OneToOneField(Editor, on_delete=models.CASCADE, verbose_name="Tahrirlovchi")
	created_at = models.DateTimeField(default=timezone.now)


	def __str__(self):
		return self.title


	class Meta:
		verbose_name = "Maqola"
		verbose_name_plural = "Maqolalar"
