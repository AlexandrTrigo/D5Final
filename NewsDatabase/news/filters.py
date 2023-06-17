from django_filters import FilterSet, CharFilter, DateFilter, ChoiceFilter
from .models import Post, POST_TYPES


class PostFilter(FilterSet):

    author_filter = CharFilter(field_name='author__user__username',
                               lookup_expr='icontains',
                               label='По автору')
    header_filter = CharFilter(field_name='header',
                               lookup_expr='icontains',
                               label='По заголовку')
    date_filter = DateFilter(field_name='created_datetime',
                             lookup_expr='gt',
                             label='Опубликовано позднее')
    type_filter = ChoiceFilter(choices=POST_TYPES,
                               field_name='type',
                               label='По типу текста',
                               empty_label=None)

    class Meta:
        model = Post
        fields = (
            'author_filter', 'header_filter', 'type_filter',
            'date_filter'
        )