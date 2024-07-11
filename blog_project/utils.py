from html_sanitizer import Sanitizer

def sanitize_html(content):
    sanitizer = Sanitizer()
    
    return sanitizer.sanitize(content)
