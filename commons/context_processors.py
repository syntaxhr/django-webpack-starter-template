from commons.models import Settings


def commons_data(request):
    app_data = Settings.objects.all().first()
    return {app_data} if app_data else {}
