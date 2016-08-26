# -*- coding: utf-8 -*-

import textwrap

import pytest


@pytest.fixture
def emoji_tests():
    return textwrap.dedent("""
        # -*- coding: utf-8 -*-

        import pytest

        def test_passed():
            assert True

        def test_failed():
            assert False

        @pytest.mark.xfail
        def test_xfailed():
            assert False

        @pytest.mark.xfail
        def test_xpassed():
            assert True

        def test_new_pytest_is_awesome():
            assert True

        @pytest.mark.skipif(True, reason='nope')
        def test_skipped():
            assert True

        @pytest.fixture
        def lol():
            raise RuntimeError

        @pytest.mark.raph
        def test_error(lol):
            assert True

        """)


@pytest.fixture
def custom_emojis():
    return textwrap.dedent("""
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

        """)


def test_emoji_disabled_by_default_verbose(testdir, emoji_tests):
    # create a temporary pytest test module
    testdir.makepyfile(emoji_tests)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '-v',
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_passed PASSED',
        '*::test_failed FAILED',
        '*::test_xfailed xfail',
        '*::test_xpassed XPASS',
        '*::test_new_pytest_is_awesome PASSED',
        '*::test_skipped SKIPPED',
        '*::test_error ERROR',
    ])

    # make sure that that we get a '1' exit code
    # as we have at least one failure
    assert result.ret == 1


def test_emoji_enabled_verbose(testdir, emoji_tests):
    # create a temporary pytest test module
    testdir.makepyfile(emoji_tests)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '-v',
        '--emoji',
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_passed PASSED 😃 ',
        '*::test_failed FAILED 😰 ',
        '*::test_xfailed xfail 😞 ',
        '*::test_xpassed XPASS 😲 ',
        '*::test_new_pytest_is_awesome PASSED 😃 ',
        '*::test_skipped SKIPPED 🙄 ',
        '*::test_error ERROR 😡 ',
    ])

    # make sure that that we get a '1' exit code
    # as we have at least one failure
    assert result.ret == 1


def test_emoji_enabled_custom_verbose(testdir, emoji_tests, custom_emojis):
    testdir.makeconftest(custom_emojis)

    # create a temporary pytest test module
    testdir.makepyfile(emoji_tests)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '-v',
        '--emoji',
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*::test_passed PASSED 🍪 ',
        '*::test_failed FAILED 😿 ',
        '*::test_xfailed xfail 🤓 ',
        '*::test_xpassed XPASS 😜 ',
        '*::test_new_pytest_is_awesome PASSED 🍪 ',
        '*::test_skipped SKIPPED 🙈 ',
        '*::test_error ERROR 💩 ',
    ])

    # make sure that that we get a '1' exit code
    # as we have at least one failure
    assert result.ret == 1


def test_emoji_disabled_by_default_non_verbose(testdir, emoji_tests):
    # create a temporary pytest test module
    testdir.makepyfile(emoji_tests)

    # run pytest with the following cmd args
    result = testdir.runpytest()

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '* .FxX.sE',
    ])

    # make sure that that we get a '1' exit code
    # as we have at least one failure
    assert result.ret == 1


def test_emoji_enabled_non_verbose(testdir, emoji_tests):
    # create a temporary pytest test module
    testdir.makepyfile(emoji_tests)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--emoji',
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '* 😃 😰 😞 😲 😃 🙄 😡 ',
    ])

    # make sure that that we get a '1' exit code
    # as we have at least one failure
    assert result.ret == 1


def test_emoji_enabled_custom_non_verbose(testdir, emoji_tests, custom_emojis):
    testdir.makeconftest(custom_emojis)

    # create a temporary pytest test module
    testdir.makepyfile(emoji_tests)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        '--emoji',
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '* 🍪 😿 🤓 😜 🍪 🙈 💩 ',
    ])

    # make sure that that we get a '1' exit code
    # as we have at least one failure
    assert result.ret == 1
