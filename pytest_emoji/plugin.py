# -*- coding: utf-8 -*-

import pytest

from pytest_emoji import hooks


def pytest_addhooks(pluginmanager):
    # Register new hooks from pytest_emoji.hooks
    pluginmanager.add_hookspecs(hooks)


def pytest_emoji_passed(config):
    # SMILING FACE WITH OPEN MOUTH
    return u'😃 ', u'PASSED 😃 '


def pytest_emoji_failed(config):
    # FACE WITH OPEN MOUTH AND COLD SWEAT
    return u'😰 ', u'FAILED 😰 '


def pytest_emoji_skipped(config):
    # FACE WITH ROLLING EYES
    return u'🙄 ', u'SKIPPED 🙄 '


def pytest_emoji_error(config):
    # POUTING FACE
    return u'😡 ', u'ERROR 😡 '


def pytest_emoji_xfailed(config):
    # DISAPPOINTED FACE
    return u'😞 ', u'xfail 😞 '


def pytest_emoji_xpassed(config):
    # DIZZY FACE
    return u'😲 ', u'XPASS 😲 '


def pytest_report_teststatus(report):
    if pytest.config.option.emoji is False:
        # Do not modify reporting unless pytest
        # is called with --emoji
        return

    error_hook = pytest.config.hook.pytest_emoji_error
    failed_hook = pytest.config.hook.pytest_emoji_failed
    passed_hook = pytest.config.hook.pytest_emoji_passed
    skipped_hook = pytest.config.hook.pytest_emoji_skipped
    xfailed_hook = pytest.config.hook.pytest_emoji_xfailed
    xpassed_hook = pytest.config.hook.pytest_emoji_xpassed

    # Handle error and skipped in setup and teardown phase
    if report.when in ('setup', 'teardown'):
        if report.failed:
            short, verbose = error_hook(config=pytest.config)
            return 'error', short, verbose
        elif report.skipped:
            short, verbose = skipped_hook(config=pytest.config)
            return 'skipped', short, verbose

    # Handle xfailed and xpassed
    if hasattr(report, 'wasxfail'):
        if report.skipped:
            short, verbose = xfailed_hook(config=pytest.config)
            return 'xfailed', short, verbose
        elif report.passed:
            short, verbose = xpassed_hook(config=pytest.config)
            return 'xpassed', short, verbose
        else:
            return '', '', ''

    # Handle passed, skipped and failed in call phase
    if report.when == 'call':
        if report.passed:
            short, verbose = passed_hook(config=pytest.config)
        elif report.skipped:
            short, verbose = skipped_hook(config=pytest.config)
        elif report.failed:
            short, verbose = failed_hook(config=pytest.config)
        return report.outcome, short, verbose


def pytest_addoption(parser):
    group = parser.getgroup('emoji')
    group.addoption(
        '--emoji',
        action='store_true',
        default=False,
        help='Add emojis to the test result log.'
    )
