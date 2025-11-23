# Workaround para Python 3.13+ que eliminó el módulo cgi
# Este módulo proporciona solo la función que Spyne necesita

def parse_header(line):
    """Parse a MIME header (Content-Type like) into a main value and a dictionary of options."""
    tokens = line.split(';')
    content_type = tokens[0].strip()
    options = {}
    for token in tokens[1:]:
        if '=' in token:
            key, value = token.split('=', 1)
            key = key.strip().lower()
            value = value.strip()
            # Remover comillas si existen
            if value and value[0] == value[-1] and value[0] in ('"', "'"):
                value = value[1:-1]
            options[key] = value
    return content_type, options
