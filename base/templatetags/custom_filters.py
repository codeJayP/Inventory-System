# myapp/templatetags/custom_filters.py
from django import template
import re

register = template.Library()

@register.filter
def capitalize_sentences(text):
    if not text:
        return text
    sentences = re.split('(\.|\?|\!)', text)
    sentences = [s.strip().capitalize() if s.strip() else s for s in sentences]
    return ''.join(sentences)
