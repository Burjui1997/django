from django import template
from django.utils.safestring import mark_safe
from markdown import markdown

register = template.Library()


@register.filter(name='markdown_to_html')
def markdown_to_html(markdown_text: str) -> str:
    html_text = "ЭТО HTML " + markdown_text.upper()
    return html_text
