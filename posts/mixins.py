from posts.settings import NEW_FILTER


class ListViewUtilsMixin(object):

    # Check current filter
    def get_active_filter(self, request, *args, **kwargs):

        active_filter = NEW_FILTER
        if 'sort' in request.GET:
            active_filter = request.GET['sort']

        return active_filter
