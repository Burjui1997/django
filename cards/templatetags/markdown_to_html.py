from django import template

register = template.Library()

@register.simple_tag(name='markdown_to_html')
def markdown_to_html(markdown_text: str) -> str:
    """

    :param markdown_text: строка из markdown
    :return: преобразованная строка в html
    """
    html_text = "Это HTML" + markdown_text.upper()

    return html_text
