# -*- coding: utf-8 -*-

from pytest_emoji import hooks


def pytest_emoji_passed(config):
    # SMILING FACE WITH OPEN MOUTH
    return u"😃 ", u"PASSED 😃 "


def pytest_emoji_failed(config):
    # FACE WITH OPEN MOUTH AND COLD SWEAT
    return u"😰 ", u"FAILED 😰 "


def pytest_emoji_skipped(config):
    # FACE WITH ROLLING EYES
    return u"🙄 ", u"SKIPPED 🙄 "


def pytest_emoji_error(config):
    # POUTING FACE
    return u"😡 ", u"ERROR 😡 "


def pytest_emoji_xfailed(config):
    # DISAPPOINTED FACE
    return u"😞 ", u"xfail 😞 "


def pytest_emoji_xpassed(config):
    # DIZZY FACE
    return u"😲 ", u"XPASS 😲 "


def pytest_addhooks(pluginmanager):
    # Register new hooks from pytest_emoji.hooks
    pluginmanager.add_hookspecs(hooks)


def pytest_configure(config):
    if config.option.emoji is False:
        # Do not enable the EmojiPlugin and modify reporting,
        # unless pytest is called with --emoji
        return

    config.pluginmanager.register(EmojiPlugin(config), "_emoji")


class EmojiPlugin(object):
    def __init__(self, config):
        self.config = config

    def pytest_report_teststatus(self, report):
        error_hook = self.config.hook.pytest_emoji_error
        failed_hook = self.config.hook.pytest_emoji_failed
        passed_hook = self.config.hook.pytest_emoji_passed
        skipped_hook = self.config.hook.pytest_emoji_skipped
        xfailed_hook = self.config.hook.pytest_emoji_xfailed
        xpassed_hook = self.config.hook.pytest_emoji_xpassed

        # Handle error and skipped in setup and teardown phase
        if report.when in ("setup", "teardown"):
            if report.failed:
                short, verbose = error_hook(config=self.config)
                return "error", short, verbose
            elif report.skipped:
                short, verbose = skipped_hook(config=self.config)
                return "skipped", short, verbose

        # Handle xfailed and xpassed
        if hasattr(report, "wasxfail"):
            if report.skipped:
                short, verbose = xfailed_hook(config=self.config)
                return "xfailed", short, verbose
            elif report.passed:
                short, verbose = xpassed_hook(config=self.config)
                return "xpassed", short, verbose
            else:
                return "", "", ""

        # Handle passed, skipped and failed in call phase
        if report.when == "call":
            if report.passed:
                short, verbose = passed_hook(config=self.config)
            elif report.skipped:
                short, verbose = skipped_hook(config=self.config)
            elif report.failed:
                short, verbose = failed_hook(config=self.config)
            return report.outcome, short, verbose


def pytest_addoption(parser):
    group = parser.getgroup("emoji")
    group.addoption(
        "--emoji",
        action="store_true",
        default=False,
        help="Add emojis to the test result log.",
    )
