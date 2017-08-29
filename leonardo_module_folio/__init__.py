
from django.apps import AppConfig

default_app_config = 'leonardo_module_folio.FolioConfig'


class Default(object):

    optgroup = ('Portfolio')

    @property
    def apps(self):
        return [
            'leonardo_module_folio',
        ]

    @property
    def plugins(self):
        return [
            ('leonardo_module_folio.apps.folio', 'Portfolio'),
        ]

    @property
    def widgets(self):
        return [
            'leonardo_module_folio.widget.featuredprojects.models.FeaturedProjectsWidget',
            'leonardo_module_folio.widget.projectcategories.models.ProjectCategoriesWidget',
        ]

class FolioConfig(AppConfig, Default):
    name = 'leonardo_module_folio'
    verbose_name = "Folio"


default = Default()
