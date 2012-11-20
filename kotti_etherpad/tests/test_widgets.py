from kotti.testing import UnitTestBase
from kotti_etherpad.widgets import render_protocol_widget


class TestProtocolWidget(UnitTestBase):

    def test_listing(self):
        from kotti import DBSession
        from kotti.testing import DummyRequest
        from kotti.resources import get_root
        from kotti_etherpad.resources import Etherpad
        request = DummyRequest()
        root = get_root()
        pad = root[u'pad1'] = Etherpad()
        pad2 = root[u'pad2'] = Etherpad()
        pad2  # pyflakes
        DBSession.flush()
        widget = render_protocol_widget(pad, request)
        wpad1 = widget['pads'][0]
        wpad2 = widget['pads'][1]
        assert u'http://example.com/pad1' == wpad1['url']
        assert u'http://example.com/pad1?timeslider=1' == wpad1['url_ts']
        assert u'http://example.com/pad2' == wpad2['url']
        assert u'http://example.com/pad2?timeslider=1' == wpad2['url_ts']
