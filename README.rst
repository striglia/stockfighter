===============================
Stockfighter
===============================

.. image:: https://img.shields.io/pypi/v/stockfighter.svg
        :target: https://pypi.python.org/pypi/stockfighter

.. image:: https://img.shields.io/travis/striglia/stockfighter.svg
        :target: https://travis-ci.org/striglia/stockfighter

.. image:: https://readthedocs.org/projects/stockfighter/badge/?version=latest
        :target: https://readthedocs.org/projects/stockfighter/?badge=latest
        :alt: Documentation Status


API wrapper for Stockfighter

* Free software: ISC license
* Documentation someday at: https://stockfighter.readthedocs.org.

Get things started
--------------------

Not hard!

.. code-block:: shell

    pip install stockfighter

Using the standard API

.. code-block:: python

    from stockfighter import Stockfighter
    s = Stockfighter(venue='TESTEX', account='EXB123456')
    print(s.venue_stocks())

...and the GM API for managing levels and such

.. code-block:: python

    from stockfighter import GM
    gm = GM()
    print gm.start('first_steps')  # Start the first level programmatically

Features
--------------------

* Calling the core Stockfighter API is pretty important :)
* Includes some rudimentary support for the GM API, such as it is known
* .....get back to me later on what else
