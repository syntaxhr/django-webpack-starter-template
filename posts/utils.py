from django.conf.settings import LANGUAGES


def get_translation_field_per_language(field, language=None):
    if (language):
        return ["{field}_{language}".format(field=field, language=language)]

    return ["{field}_{code}".format(field=field, code=code) for code, language in LANGUAGES]


def get_translation_fields_per_language(from_field, to_field, language=None):
    data = []

    # If a specific language is defined then return only the fields about that language
    if language:
        data.append({
            "from_field": "%s_%s" % (from_field, language),
            "to_field": "%s_%s" % (to_field, language),
            "title": "%s_%s" % ("title", language),
            "lang": language,
        })
        return data

    # Add the default field without language
    data.append({
        "from_field": from_field,
        "to_field": to_field,
        "title": "title",
        "lang": "default"
    })

    # Add field_language for every language defined in settings.py
    for code, language in LANGUAGES:
        data.append({
            "from_field": "%s_%s" % (from_field, code),
            "to_field": "%s_%s" % (to_field, code),
            "title": "%s_%s" % ("title", code),
            "lang": code,
        })

    return data
