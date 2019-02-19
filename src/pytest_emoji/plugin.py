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
    return u"😞 ", u"XFAIL 😞 "


def pytest_emoji_xpassed(config):
    # DIZZY FACE
    return u"😲 ", u"XPASS 😲 "


def pytest_addhooks(pluginmanager):
    # Register new hooks from pytest_emoji.hooks
    pluginmanager.add_hookspecs(hooks)


def pytest_report_teststatus(report, config):
    if config.option.emoji is False:
        # Do not modify reporting, unless pytest is called with --emoji
        return

    # Handle error and skipped in setup and teardown phase
    if report.when in ("setup", "teardown"):
        if report.failed:
            short, verbose = config.hook.pytest_emoji_error(config=config)
            return "error", short, verbose
        elif report.skipped:
            short, verbose = config.hook.pytest_emoji_skipped(config=config)
            return "skipped", short, verbose

    # Handle xfailed and xpassed
    if hasattr(report, "wasxfail"):
        if report.skipped:
            short, verbose = config.hook.pytest_emoji_xfailed(config=config)
            return "xfailed", short, verbose
        elif report.passed:
            short, verbose = config.hook.pytest_emoji_xpassed(config=config)
            return "xpassed", short, verbose
        else:
            return "", "", ""

    # Handle passed, skipped and failed in call phase
    if report.when == "call":
        if report.passed:
            short, verbose = config.hook.pytest_emoji_passed(config=config)
        elif report.skipped:
            short, verbose = config.hook.pytest_emoji_skipped(config=config)
        elif report.failed:
            short, verbose = config.hook.pytest_emoji_failed(config=config)
        return report.outcome, short, verbose


def pytest_addoption(parser):
    group = parser.getgroup("emoji")
    group.addoption(
        "--emoji",
        action="store_true",
        default=False,
        help="Add emojis to the test result log.",
    )
