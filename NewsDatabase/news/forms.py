from django.forms import ModelForm, CharField, ChoiceField, \
    ModelChoiceField, ModelMultipleChoiceField, \
    CheckboxSelectMultiple, Textarea
from .models import Post, Author, Category, POST_TYPES


class CustomAuthorName(ModelChoiceField):
    def label_from_instance(self, author):
        return "%s" % author.user.username


class CustomCategoryName(ModelMultipleChoiceField):
    def label_from_instance(self, category):
        return "%s" % category.name


class PostForm(ModelForm):
    author = CustomAuthorName(queryset=Author.objects.all(),
                              label='Автор',
                              empty_label=None)
    header = CharField(max_length=255,
                       label='Заголовок')
    text = CharField(max_length=1000,
                     label='Текст',
                     widget=Textarea)
    category = CustomCategoryName(queryset=Category.objects.all(),
                                  label='Категории',
                                  widget=CheckboxSelectMultiple)
    type = ChoiceField(choices=POST_TYPES,
                       label='Тип текста')

    class Meta:
        model = Post
        fields = ['author', 'header', 'text',
                  'category', 'type']