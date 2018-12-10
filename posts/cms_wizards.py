from cms.wizards.wizard_base import Wizard
from cms.wizards.wizard_pool import wizard_pool
from django.utils.translation import ugettext_lazy as _

from posts.forms import PostWizardForm


class PostWizard(Wizard):
    pass


post_wizard = PostWizard(
    title=_('New post'),
    weight=200,
    form=PostWizardForm,
    description=_('Create a new post instance')
)

wizard_pool.register(post_wizard)
