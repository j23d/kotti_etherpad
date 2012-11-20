from pyramid.traversal import resource_path

from kotti import DBSession
from kotti.views.slots import assign_slot

from kotti_etherpad.resources import Etherpad


def render_protocol_widget(context, request, name=''):
    """Collect all pads for the user and provide links to pad and its
       protocol."""
    session = DBSession()
    # TODO: filter by permissions
    all_pads = session.query(Etherpad).all()
    pads = []
    for pad in all_pads:
        url = request.application_url + resource_path(pad)
        pads.append({
            'title': pad.title,
            'url': url,
            'url_ts': url + '?timeslider=1',
        })
    return {'pads': pads}


def include_protocol_widget(config, where='right'):
    config.add_view(
        render_protocol_widget,
        name='render-protocol-widget',
        renderer='templates/protocol_widget.pt',
        )
    assign_slot('render-protocol-widget', where)


def include_protocol_widget_left(config):  # pragma: no cover
    include_protocol_widget(config, 'left')
