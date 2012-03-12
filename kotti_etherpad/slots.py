from pyramid.renderers import render
from pyramid.traversal import resource_path

from kotti import DBSession
from kotti.views.slots import (
    register,
    RenderRightSlot,
    RenderLeftSlot,
)

from kotti_etherpad.resources import Etherpad


def render_protocol_widget(context, request, name=''):
    """Collect all pads for the user and provide links to pad and its
       protocol."""
    session = DBSession()
    # TODO: filter by permissions
    all_pads = session.query(Etherpad).all()
    variables = {
        'pads': [],
    }
    for pad in all_pads:
        url = request.application_url + resource_path(pad)
        variables['pads'].append({
            'title': pad.title,
            'url': url,
            'url_ts': url + '?timeslider=1',
        })
    return render('templates/protocol_widget.pt', variables, request)


def include_protocol_widget(config, where=RenderRightSlot):  # pragma: no cover
    register(where, None, render_protocol_widget)


def include_protocol_widget_left(config):  # pragma: no cover
    include_protocol_widget(config, RenderLeftSlot)
