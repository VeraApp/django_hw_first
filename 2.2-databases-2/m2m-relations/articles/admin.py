from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            dict = form.cleaned_data
            if not dict.get('is_main'):
                continue
            elif dict['is_main'] is True:
                i += 1
        if i == 0:
            raise ValidationError('Выберите основной раздел')
        elif i > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()

class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset

@admin.register(Article, Tag)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
    save_on_top = True
