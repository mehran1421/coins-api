from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from coins.routing import ws_urlpatterns
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':
        AuthMiddlewareStack(
            URLRouter(
                ws_urlpatterns
            )
        )
})
