def test_emoji_disabled_by_default_verbose(testdir, emoji_tests):
    # create a temporary pytest test module
    testdir.makepyfile(emoji_tests)

    # run pytest with the following cmd args
    result = testdir.runpytest("-v", "-o", "console_output_style=classic")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        [
            "*::test_passed PASSED",
            "*::test_failed FAILED",
            "*::test_xfailed XFAIL",
            "*::test_xpassed XPASS",
            "*::test_skipped SKIPPED",
            "*::test_error ERROR",
        ]
    )

    # make sure that that we get a '1' exit code
    # as we have at least one failure
    assert result.ret == 1


def test_emoji_enabled_verbose(testdir, emoji_tests):
    # create a temporary pytest test module
    testdir.makepyfile(emoji_tests)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        "-v", "--emoji", "-o", "console_output_style=classic"
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        [
            "*::test_passed PASSED 😃 ",
            "*::test_failed FAILED 😰 ",
            "*::test_xfailed XFAIL 😞 ",
            "*::test_xpassed XPASS 😲 ",
            "*::test_skipped SKIPPED 🙄 ",
            "*::test_error ERROR 😡 ",
        ]
    )

    # make sure that that we get a '1' exit code
    # as we have at least one failure
    assert result.ret == 1


def test_emoji_enabled_custom_verbose(testdir, emoji_tests, custom_emojis):
    testdir.makeconftest(custom_emojis)

    # create a temporary pytest test module
    testdir.makepyfile(emoji_tests)

    # run pytest with the following cmd args
    result = testdir.runpytest(
        "-v", "--emoji", "-o", "console_output_style=classic"
    )

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        [
            "*::test_passed PASSED 🍪 ",
            "*::test_failed FAILED 😿 ",
            "*::test_xfailed XFAIL 🤓 ",
            "*::test_xpassed XPASS 😜 ",
            "*::test_skipped SKIPPED 🙈 ",
            "*::test_error ERROR 💩 ",
        ]
    )

    # make sure that that we get a '1' exit code
    # as we have at least one failure
    assert result.ret == 1


def test_emoji_disabled_by_default_non_verbose(testdir, emoji_tests):
    # create a temporary pytest test module
    testdir.makepyfile(emoji_tests)

    # run pytest with the following cmd args
    result = testdir.runpytest("-o", "console_output_style=classic")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(["* .FxXsE"])

    # make sure that that we get a '1' exit code
    # as we have at least one failure
    assert result.ret == 1


def test_emoji_enabled_non_verbose(testdir, emoji_tests):
    # create a temporary pytest test module
    testdir.makepyfile(emoji_tests)

    # run pytest with the following cmd args
    result = testdir.runpytest("--emoji", "-o", "console_output_style=classic")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(["* 😃 😰 😞 😲 🙄 😡 "])

    # make sure that that we get a '1' exit code
    # as we have at least one failure
    assert result.ret == 1


def test_emoji_enabled_custom_non_verbose(testdir, emoji_tests, custom_emojis):
    testdir.makeconftest(custom_emojis)

    # create a temporary pytest test module
    testdir.makepyfile(emoji_tests)

    # run pytest with the following cmd args
    result = testdir.runpytest("--emoji", "-o", "console_output_style=classic")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(["* 🍪 😿 🤓 😜 🙈 💩 "])

    # make sure that that we get a '1' exit code
    # as we have at least one failure
    assert result.ret == 1
