from django.apps import AppConfig


class UsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.usuario'
    
    def ready(self):
        import apps.usuario.signals  # Importa las señales al iniciar la aplicación

