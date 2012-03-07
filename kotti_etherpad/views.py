import colander

from kotti import DBSession
from kotti.views.edit import ContentSchema
from kotti.views.edit import generic_edit
from kotti.views.edit import generic_add
from kotti.views.view import view_node
from kotti.views.util import ensure_view_selector
from kotti.views.util import template_api

from kotti_etherpad.resources import Etherpad

class EtherpadSchema(ContentSchema):
    pad_room = colander.SchemaNode(colander.String())
    default_user_name = colander.SchemaNode(colander.String())
    server_url = colander.SchemaNode(colander.String())
    server_port = colander.SchemaNode(colander.Integer())
    show_controls = colander.SchemaNode(colander.Boolean())
    show_chat = colander.SchemaNode(colander.Boolean())
    show_line_numbers = colander.SchemaNode(colander.Boolean())
    use_monospace_font = colander.SchemaNode(colander.Boolean())
    no_colors = colander.SchemaNode(colander.Boolean())
    hide_QR_code = colander.SchemaNode(colander.Boolean())
    width = colander.SchemaNode(colander.String())
    height = colander.SchemaNode(colander.String())
    border = colander.SchemaNode(colander.String())
    border_style = colander.SchemaNode(colander.String())


@ensure_view_selector
def edit_etherpad(context, request):
    return generic_edit(context, request, EtherpadSchema())


def add_etherpad(context, request):
    return generic_add(context, request, EtherpadSchema(), Etherpad, u'etherpad')


def view_etherpad(context, request):
    # session = DBSession()
    host = ''
    if not context.server_url.startswith('http://'):
        host += 'http://'
    host = "%s%s" % (host, context.server_url)
    if int(context.server_port) != '80':
        host = "%s:%s" % (host, context.server_port)

    return {
        'api': template_api(context, request),
        'pad_room': context.pad_room,
        'host': host,
        'baseUrl': '/p/',
        'showControls': context.show_controls and 'true' or 'false',
        'showChat': context.show_chat and 'true' or 'false',
        'showLineNumbers': context.show_line_numbers and 'true' or 'false',
        'userName': context.default_user_name,  # TODO: use logged in name
        'useMonospaceFont': context.use_monospace_font and 'true' or 'false',
        'noColors': context.no_colors and 'true' or 'false',
        'hideQRCode': context.hide_QR_code and 'true' or 'false',
        'width': context.width,
        'height': context.height,
        'border': context.border,
        'borderStyle': context.border_style,
        }


def includeme_edit(config):

    config.add_view(
        edit_etherpad,
        context=Etherpad,
        name='edit',
        permission='edit',
        renderer='kotti:templates/edit/node.pt',
        )

    config.add_view(
        add_etherpad,
        name=Etherpad.type_info.add_view,
        permission='add',
        renderer='kotti:templates/edit/node.pt',
        )


def includeme_view(config):
    config.add_view(
        view_etherpad,
        context=Etherpad,
        name='view',
        permission='view',
        renderer='templates/etherpad-view.pt',
        )

    config.add_static_view('static-kotti_etherpad', 'kotti_etherpad:static')


def includeme(config):
    includeme_edit(config)
    includeme_view(config)
