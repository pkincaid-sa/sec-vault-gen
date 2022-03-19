from jinja2 import Environment, PackageLoader, select_autoescape
environment = Environment(
    loader=PackageLoader('lib'),
    autoescape=select_autoescape()
)
