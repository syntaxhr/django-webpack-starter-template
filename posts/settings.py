from django.utils.translation import ugettext_lazy as _

############### CONFIGURATION ##################

CMS_PLUGIN_MODULE = _("Posts")
CMS_TOOLBAR_APP_NAME = 'post-app'

############# END CONFIGURATION ################

#################### URLS ######################

POST_DETAIL_URL = 'detail'
POSTS_LIST_URL = 'list'
POSTS_CATEGORY_DETAIL_URL = 'category_detail'
POSTS_SEARCH_URL = 'search'

################### END URLS ###################

################### FILTERS ####################

NEW_FILTER = '-date'
OLD_FILTER = 'date'

NEW_FILTER_LABEL = _("Newest first")
OLD_FILTER_LABEL = _("Oldest first")

SORT_FILERS = [
    (OLD_FILTER, OLD_FILTER_LABEL),
    (NEW_FILTER, NEW_FILTER_LABEL),
]

################# END FILTERS ##################

################# TEMPLATES ####################

# Templates
POSTS_LIST_BY_CATEGORY_TEMPLATE = 'posts/posts_list.html'
POSTS_LIST_TEMPLATE = 'posts/posts_list.html'
POST_DETAIL_TEMPLATE = 'posts/post_detail.html'
POST_SEARCH_TEMPLATE = 'posts/posts_search.html'

section_templates = [
    (POSTS_LIST_TEMPLATE, _('Default')),
    # ('posts/some_other_template_list.html', _(u'Template display name')),
]

category_templates = [
    (POSTS_LIST_BY_CATEGORY_TEMPLATE, _('Default')),
    # ('posts/some_other_template_list.html', _(u'Template display name')),
]

post_templates = [
    (POST_DETAIL_TEMPLATE, _('Default')),
    # ('posts/some_other_template_detail.html', _(u'Template display name')),
]

################ END TEMPLATES #################
