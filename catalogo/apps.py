from django.apps import AppConfig

##VERBOSE NAME ADICIONADO PARA MOSTRAR NO ADMIN##SEGUNDA PARTE NO __INIT__
class CatalogoConfig(AppConfig):
    name = 'catalogo'
    verbose_name = 'Catálogo'
