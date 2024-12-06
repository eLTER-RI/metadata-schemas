import bleach

def sanitize_html(raw_html):
    allowed_tags = {'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'strong', 'em', 'ul', 'ol', 'li', 'a', 'br'}
    allowed_attributes = {'a': ['href', 'title']}

    return bleach.clean(text=str(raw_html), tags=allowed_tags, attributes=allowed_attributes)

