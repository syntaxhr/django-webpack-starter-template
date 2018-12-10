from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from commons.models import WidgetPlugin
from commons.settings import CMS_PLUGIN_MODULE


class SliderPlugin(CMSPluginBase):
    model = WidgetPlugin
    module = CMS_PLUGIN_MODULE
    fields = ['title',]
    allow_children = True
    cache = False


class SliderItemPlugin(CMSPluginBase):
    model = WidgetPlugin
    module = CMS_PLUGIN_MODULE
    require_parent = True
    cache = False


#################################
### Slider for Header ###
#################################

# Slider Header
@plugin_pool.register_plugin
class SliderHeaderPlugin(SliderPlugin):
    name = _("Header Slider")
    render_template = 'commons/cms/slider/slider_header.html'
    child_classes = ['SliderItemHeaderPlugin']


# Slider item for Header
@plugin_pool.register_plugin
class SliderItemHeaderPlugin(SliderItemPlugin):
    name = _("Slider item for Header")
    render_template = 'commons/cms/slider/slider_header_item.html'
    fields = ['content_html', 'link', 'image',]
    parent_classes = ['SliderHeaderPlugin',]


#################################
### Slider for components ###
#################################

# Slider components
@plugin_pool.register_plugin
class SliderComponentsPlugin(SliderPlugin):
    name = _("Slider components")
    render_template = 'commons/cms/slider/slider_components.html'
    child_classes = ['SliderItemComponentsPlugin']

    def render(self, context, instance, placeholder):
        context = super(SliderComponentsPlugin, self).render(context, instance, placeholder)

        number_of_child = len(instance.child_plugin_instances)
        number_of_child = number_of_child if number_of_child < 5 else 5
        context.update({"number_of_child": number_of_child})

        return context


# Slider item for components
@plugin_pool.register_plugin
class SliderItemComponentsPlugin(SliderItemPlugin):
    name = _("Slider item for components")
    render_template = 'commons/cms/slider/slider_components_item.html'
    fields = ['content_html', 'image',]
    parent_classes = ['SliderComponentsPlugin', ]
