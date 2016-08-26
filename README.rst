pytest-emoji
===================================

|pypi| |pyversions| |license| |travis-ci| |appveyor|

pytest + emoji == 😍

Do you find writing tests tedious or boring? It can be - but it doesn't need to
be.

.. |pypi| image:: https://img.shields.io/pypi/v/pytest-emoji.svg
   :target: https://pypi.python.org/pypi/pytest-emoji
   :alt: PyPI Package

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/pytest-emoji.svg
   :target: https://pypi.python.org/pypi/pytest-emoji/
   :alt: PyPI Python Versions

.. |license| image:: https://img.shields.io/pypi/l/pytest-emoji.svg
   :target: https://pypi.python.org/pypi/pytest-emoji
   :alt: PyPI Package License

.. |travis-ci| image:: https://travis-ci.org/hackebrot/pytest-emoji.svg?branch=master
    :target: https://travis-ci.org/hackebrot/pytest-emoji
    :alt: See Build Status on Travis CI

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/hackebrot/pytest-emoji?branch=master
    :target: https://ci.appveyor.com/project/hackebrot/pytest-emoji/branch/master
    :alt: See Build Status on AppVeyor

pytest
------

**pytest** is a mature testing framework for Python that is developed by a
thriving and ever-growing community of volunteers. It uses plain assert
statements and regular Python comparisons. Writing tests with pytest requires
little to no boilerplate code and powerful features allow easy parametrization
and intelligent test selection.

It can be easily extended and has hundreds of plugins available. Distributed
under the terms of the MIT license, pytest is free and open source software.

Check out `pytest`_ if you haven't already and if you're not sold just yet,
install this plugin. Maybe that will get you motivated 😁

This `pytest`_ plugin was generated with `Cookiecutter`_ along with
`@hackebrot`_'s `Cookiecutter-pytest-plugin`_ template.


Installation
------------

**pytest-emoji** is available for Python 3. 🐍

You can install **pytest-emoji** via `pip`_ from `PyPI`_::

    $ pip install pytest-emoji

This will automatically install **pytest** of version 3.0.1 or higher.


Features
--------

This plugin adds a ``--emoji`` CLI flag to pytest, which replaces the test
result indicator to emojis, both for *normal* and *verbose* mode.

- ``😃 / PASSED 😃`` for passed tests
- ``😰 / FAILED 😰`` for failed tests
- ``😞 / xfail 😞`` for xfailed tests
- ``😲 / XPASS 😲`` for xpassed tests
- ``🙄 / SKIPPED 🙄`` for skipped tests
- ``😡 / ERROR 😡`` for tests with errors

Normal mode:

.. code-block:: text
    
    $ pytest --emoji


.. code-block:: text

    tests/test_emoji.py 😃 😰 😞 😲 🙄 😡


Verbose mode:

.. code-block:: text

    $ pytest --verbose --emoji


.. code-block:: text

    tests/test_emoji.py::test_passed PASSED 😃
    tests/test_emoji.py::test_failed FAILED 😰
    tests/test_emoji.py::test_xfailed xfail 😞
    tests/test_emoji.py::test_xpassed XPASS 😲
    tests/test_emoji.py::test_skipped SKIPPED 🙄
    tests/test_emoji.py::test_error ERROR 😡


Customization
-------------

You can change also the emojis, if you want. 😛

Add a ``conftest.py`` to your tests folder and implement the following hooks.
If you wish to use the default, omit the according hook.


.. code-block:: python

    def pytest_emoji_passed(config):
        return u'🍪 ', u'PASSED 🍪 '


    def pytest_emoji_failed(config):
        return u'😿 ', u'FAILED 😿 '


    def pytest_emoji_skipped(config):
        return u'🙈 ', u'SKIPPED 🙈 '


    def pytest_emoji_error(config):
        return u'💩 ', u'ERROR 💩 '


    def pytest_emoji_xfailed(config):
        return u'🤓 ', u'xfail 🤓 '


    def pytest_emoji_xpassed(config):
        return u'😜 ', u'XPASS 😜 '


Naming is important, make sure you don't make any typos!

All of these hooks receive the pytest ``config`` object, which allows you to
check options and further customize the output. All hooks need to return a
tuple of ``str`` as in ``('<shortletter>', '<verbose-word>')``.

It's recommended for emoji to add an extra ``' '`` (blank) for better formatting.


Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_.


License
-------

Distributed under the terms of the `MIT`_ license, **pytest-emoji** is free and
open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed
description.


Code of Conduct
---------------

Everyone interacting in the **pytest-emoji** project's codebases, issue
trackers, chat rooms, and mailing lists is expected to follow the `PyPA Code of
Conduct`_.


.. _`@hackebrot`: https://github.com/hackebrot
.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`PyPA Code of Conduct`: https://www.pypa.io/en/latest/code-of-conduct/
.. _`PyPI`: https://pypi.python.org/pypi
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/hackebrot/pytest-emoji/issues
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
