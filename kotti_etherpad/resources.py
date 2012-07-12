from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Boolean,
)
from kotti.resources import Content
from kotti.util import _


class Etherpad(Content):
    """This type contains all information wich pad is to displayed
       from an etherpad server and how to display it.
    """
    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)
    pad_id = Column('pad_id', String(64))
    server_domain = Column('server_domain', String(256))
    server_port = Column('server_port', Integer())
    show_controls = Column('show_controls', Boolean())
    show_chat = Column('show_chat', Boolean())
    show_line_numbers = Column('show_line_numbers', Boolean())
    use_monospace_font = Column(Boolean())
    no_colors = Column('no_colors', Boolean())
    hide_QR_code = Column('hide_QR_code', Boolean())
    width = Column('width', String(16))
    height = Column('height', String(16))
    border = Column('border', Integer())
    border_style = Column('border_style', String(16))

    type_info = Content.type_info.copy(
        name=u'Etherpad',
        title=_(u'Etherpad'),
        add_view=u'add_etherpad',
        addable_to=[u'Document'],
        )

    def __init__(self, pad_id='etherpad', server_domain='localhost',
                 server_port=9001, show_controls=True, show_chat=True,
                 show_line_numbers=True, use_monospace_font=True,
                 no_colors=False, hide_QR_code=False, width='100%', height='800px',
                 border=0, border_style='solid', **kwargs):
        super(Etherpad, self).__init__(**kwargs)
        self.pad_id = pad_id
        self.server_domain = server_domain
        self.server_port = server_port
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

    def host(self):
        host = self.server_domain
        if int(self.server_port) != '80':
            host = "%s:%s" % (host, self.server_port)
        return host
