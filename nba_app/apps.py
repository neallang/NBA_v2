from django.apps import AppConfig


class NbaComparatorConfig(AppConfig):
    name = 'nba_app'

    def ready(self):
        import nba_app.templatetags.custom_filters
