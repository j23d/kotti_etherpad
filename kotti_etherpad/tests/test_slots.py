from kotti.tests import UnitTestBase
from kotti_etherpad.slots import render_protocol_widget


class TestProtocolWidget(UnitTestBase):

    def test_render(self):
        widget = render_protocol_widget(None, None)
        self.assertTrue(widget.startswith('<!DOCTYPE html>'))

    def test_listing(self):
        from kotti import DBSession
        from kotti.testing import DummyRequest
        from kotti.resources import get_root
        from kotti_etherpad.resources import Etherpad
        request = DummyRequest()
        root = get_root()
        pad = root[u'pad1'] = Etherpad()
        pad2 = root[u'pad2'] = Etherpad()
        DBSession.flush()
        widget = render_protocol_widget(pad, request)
        self.assert_(u'href="http://example.com/pad1"' in widget)
        self.assert_(u'href="http://example.com/pad1?timeslider=1"' in widget)
        self.assert_(u'href="http://example.com/pad2"' in widget)
        self.assert_(u'href="http://example.com/pad1?timeslider=1"' in widget)
