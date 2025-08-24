AUTHOR = 'UlisesGC'
SITENAME = 'TequilaTech'
SITEURL = ""

THEME = 'themes/blue-penguin'
PATH = "content"

TIMEZONE = 'America/Mexico_City'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Guardar el índice del blog en /blog/ en lugar de /
INDEX_SAVE_AS = 'blog/index.html'

# Guardar las páginas de categorías en /blog/
CATEGORY_SAVE_AS = 'blog/{slug}.html'
CATEGORIES_SAVE_AS = 'blog/categories.html'

# Guardar los archivos de etiquetas en /blog/
TAG_SAVE_AS = 'blog/tag/{slug}.html'
TAGS_SAVE_AS = 'blog/tags.html'

# Guardar archivos de autores en /blog/
AUTHOR_SAVE_AS = 'blog/author/{slug}.html'
AUTHORS_SAVE_AS = 'blog/authors.html'

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

STATIC_PATHS = ['images']

# Menú personalizado (sin Contacto por ahora)
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
    ('Inicio', '/'),
    ('Blog', '/blog/'),
    ('Proyectos', '/pages/proyectos.html'),
    ('Sobre mí', '/pages/sobre-mi.html'),
)
