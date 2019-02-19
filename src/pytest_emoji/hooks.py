import pytest


@pytest.hookspec(firstresult=True)
def pytest_emoji_passed(config):
    """Called to get a representation for a passed test item.

    Requires a tuple of (<shortletter>, <verbose-word>)
    pytest defaults to ('.', 'PASSED')
    """


@pytest.hookspec(firstresult=True)
def pytest_emoji_failed(config):
    """Called to get a representation for a failed test item.

    Requires a tuple of (<shortletter>, <verbose-word>)
    pytest defaults to ('F', 'FAILED')
    """


@pytest.hookspec(firstresult=True)
def pytest_emoji_skipped(config):
    """Called to get a representation for a skipped test item.

    Requires a tuple of (<shortletter>, <verbose-word>)
    pytest default to ('s', 'SKIPPED')
    """


@pytest.hookspec(firstresult=True)
def pytest_emoji_error(config):
    """Called to get a representation for a error test item.

    Requires a tuple of (<shortletter>, <verbose-word>)
    pytest defaults to ('E', 'ERROR')
    """


@pytest.hookspec(firstresult=True)
def pytest_emoji_xfailed(config):
    """Called to get a representation for a xfailed test item.

    Requires a tuple of (<shortletter>, <verbose-word>)
    pytest defaults to ('x', 'XFAIL')
    """


@pytest.hookspec(firstresult=True)
def pytest_emoji_xpassed(config):
    """Called to get a representation for a xpassed test item.

    Requires a tuple of (<shortletter>, <verbose-word>)
    pytest defaults to ('X', 'XPASS')
    """
