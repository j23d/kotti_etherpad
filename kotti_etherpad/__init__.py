from pyramid.i18n import TranslationStringFactory
_ = TranslationStringFactory('kotti_etherpad')


def kotti_configure(settings):
    settings['pyramid.includes'] += ' kotti_etherpad.views'
    settings['kotti.available_types'] += ' kotti_etherpad.resources.Etherpad'
