from flatpickr._settings import WidgetSettings


class WidgetMedia:
    def yield_js(self, settings: WidgetSettings):
        yield settings.NPM_URL + 'flatpickr@4.5.2/dist/flatpickr.min.js'
        yield (
            settings.GITHUB_URL +
            'monim67/django-flatpickr@1.0.0/static/js/django-flatpickr.js'
        )
        if 'locale' in settings.OPTIONS:
            yield (
                settings.NPM_URL +
                ('flatpickr@4.5.2/dist/l10n/%s.js' %
                 settings.OPTIONS['locale'])
            )

    def yield_css(self, settings: WidgetSettings):
        yield settings.NPM_URL + 'flatpickr@4.5.2/dist/flatpickr.min.css'
        if settings.THEME_URL:
            yield settings.THEME_URL
        elif settings.THEME_NAME:
            yield (
                settings.NPM_URL +
                ('flatpickr@4.5.2/dist/themes/%s.css' % settings.THEME_NAME)
            )

    js = tuple(yield_js(None, WidgetSettings))
    css = {'all': tuple(yield_css(None, WidgetSettings))}
