# pytest-emoji

A pytest plugin that adds emojis to your test result report 😍

## pytest

pytest is a mature testing framework for Python that is developed by a
thriving community of volunteers. It uses plain assert statements and regular
Python comparisons. Writing tests with pytest requires little to no
boilerplate code and powerful features allow easy parametrization and
intelligent test selection.

There are hundreds of plugins available for pytest with which you can extend
and customize your testing harness. Distributed under the terms of the MIT
license, pytest is free and open source software.

Check out [pytest][pytest] if you haven't already and if you're not sold just
yet, install this plugin. Maybe that will get you motivated to write more
tests! 😁

This pytest plugin was generated with [Cookiecutter][cookiecutter] along with
[@hackebrot][hackebrot]'s [cookiecutter-pytest-plugin][plugin-template]
template. 🍪

[cookiecutter]: https://github.com/audreyr/cookiecutter
[hackebrot]: https://github.com/hackebrot
[pytest]: https://github.com/pytest-dev/pytest
[plugin-template]: https://github.com/pytest-dev/cookiecutter-pytest-plugin

## Installation

**pytest-emoji** is available for Python 3. 🐍

You can install **pytest-emoji** via [pip][pip] from [PyPI][PyPI]:

```text
$ pip install pytest-emoji
```

This will automatically install **pytest** of version 4.2.1 or higher.

[pip]: https://pypi.python.org/pypi/pip/
[PyPI]: https://pypi.org/project/pytest-emoji/

## Features

This plugin adds a ``--emoji`` CLI flag to pytest, which replaces the test
result indicator to emojis, both for *normal* and *verbose* mode.

- ``😃 / PASSED 😃`` for passed tests
- ``😰 / FAILED 😰`` for failed tests
- ``😞 / XFAIL 😞`` for xfailed tests
- ``😲 / XPASS 😲`` for xpassed tests
- ``🙄 / SKIPPED 🙄`` for skipped tests
- ``😡 / ERROR 😡`` for tests with errors

Normal mode:

```text
$ pytest --emoji
```

```text
tests/test_emoji.py 😃 😰 😞 😲 🙄 😡
```

Verbose mode:

```text
$ pytest --verbose --emoji
```

```text
tests/test_emoji.py::test_passed PASSED 😃
tests/test_emoji.py::test_failed FAILED 😰
tests/test_emoji.py::test_xfailed XFAIL 😞
tests/test_emoji.py::test_xpassed XPASS 😲
tests/test_emoji.py::test_skipped SKIPPED 🙄
tests/test_emoji.py::test_error ERROR 😡
```

## Customization

You can also change the emojis, if you want. 😛

Add a ``conftest.py`` to your tests folder and implement the following hooks.
If you wish to use the default, omit the according hook.

```python
def pytest_emoji_passed(config):
    return "🍪 ", "PASSED 🍪 "


def pytest_emoji_failed(config):
    return "😿 ", "FAILED 😿 "


def pytest_emoji_skipped(config):
    return "🙈 ", "SKIPPED 🙈 "


def pytest_emoji_error(config):
    return "💩 ", "ERROR 💩 "


def pytest_emoji_xfailed(config):
    return "🤓 ", "XFAIL 🤓 "


def pytest_emoji_xpassed(config):
    return "😜 ", "XPASS 😜 "
```

**Naming the hooks correctly is important, make sure you don't make any typos**
⚠️

All of these hooks receive the pytest ``config`` object, which allows you to
check options and further customize the output. All hooks need to return a
tuple of ``str`` as in ``("<shortletter>", "<verbose-word>")``.

It's recommended for emoji to add an extra ``" "`` (blank) for better formatting.

## Community

Are you interested in contributing to **pytest-emoji**? Your contributions are
greatly appreciated! Every little bit helps, and credit will always be given!

Everyone interacting in the **pytest-emoji** project's codebases, issue
trackers, chat rooms, and mailing lists is expected to follow the [PyPA Code
of Conduct][coc].


[coc]: https://www.pypa.io/en/latest/code-of-conduct/

## Issues

If you encounter any problems, please [file an issue][issues] along with a
detailed description.

[issues]: https://github.com/hackebrot/pytest-emoji/issues

## License

Distributed under the terms of the [MIT][mit] license, **pytest-emoji** is
free and open source software

[mit]: http://opensource.org/licenses/MIT
