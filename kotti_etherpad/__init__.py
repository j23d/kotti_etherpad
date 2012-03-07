def kotti_configure(settings):
    settings['kotti.includes'] += 'kotti_etherpad.views'
    settings['kotti.available_types'] += ' kotti_etherpad.resources.Etherpad'
