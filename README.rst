==============
kotti_etherpad
==============

This is an extension to the Kotti CMS to add an etherpad on your site.  

`Find out more about Kotti`_
`Find out more about etherpad`_

Setting up your etherpad
========================

This Addon provides an Content Type to present an etherpad on your Kotti
site. To set up the content type add ``kotti_etherpad.kotti_configure``
to the ``kotti.configurators`` setting in your ini file::

    kotti.configurators = kotti_etherpad.kotti_configure

Now you can add a new pad. You can host your own server (have a look to
the `etherpad documentation`_) or use a free one (choose from a 
`list of free etherpad servers`_).

.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
.. _Find out more about etherpad: https://github.com/Pita/etherpad-lite/
.. _etherpad documentation: https://github.com/Pita/etherpad-lite/blob/master/README.md
.. _list of free etherpad servers: http://etherpad.org/public-sites/
