"""Application config module."""

from django.apps import AppConfig

from githubnavigator import container


# [TODO] WebConfig
class WebConfig(AppConfig):
    name = "web"

    # [TODO] WebConfig > ready
    def ready(self):
        container.wire(modules=[".views"])
