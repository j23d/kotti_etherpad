from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
    Integer,
    String,
    UnicodeText,
    Boolean,
)
from sqlalchemy.orm import mapper
from kotti import metadata
from kotti.resources import Content


class Etherpad(Content):
    type_info = Content.type_info.copy(
        name=u'Etherpad',
        add_view=u'add_etherpad',
        addable_to=[u'Document'],
        )

    def __init__(self, pad_room=u'etherpad', server_url='localhost',
                 server_port='9001', default_user_name='', show_controls=True,
                 show_chat=True, show_line_numbers=True, use_monospace_font=True,
                 no_colors=False, hide_QR_code=False, width='100%', height='800px',
                 border='0', border_style='solid', **kwargs):
        super(Etherpad, self).__init__(**kwargs)
        self.pad_room = pad_room
        self.server_url = server_url
        self.server_port = server_port
        self.default_user_name = default_user_name
        # set default values and descriptions for the widgets???
        self.show_controls = show_controls
        self.show_chat = show_chat
        self.show_line_numbers = show_line_numbers
        self.use_monospace_font = use_monospace_font
        self.no_colors = no_colors
        self.hide_QR_code = hide_QR_code
        self.width = width
        self.height = height
        self.border = border
        self.border_style = border_style


etherpad = Table('etherpad', metadata,
    Column('id', Integer, ForeignKey('contents.id'), primary_key=True),
    Column('pad_room', String()),
    Column('server_url', String()),
    Column('server_port', Integer()),
    Column('default_user_name', String()),
    Column('show_controls', Boolean()),
    Column('show_chat', Boolean()),
    Column('show_line_numbers', Boolean()),
    Column('use_monospace_font', Boolean()),
    Column('no_colors', Boolean()),
    Column('hide_QR_code', Boolean()),
    Column('width', String()),
    Column('height', String()),
    Column('border', Integer()),
    Column('border_style', String()),
)

mapper(Etherpad, etherpad, inherits=Content, polymorphic_identity='etherpad')
