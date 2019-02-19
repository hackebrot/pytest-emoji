import textwrap
import pytest

pytest_plugins = "pytester"


@pytest.fixture(name="emoji_tests")
def fixture_emoji_tests():
    return textwrap.dedent(
        """\
        import pytest

        def test_passed():
            assert "emoji" == "emoji"

        def test_failed():
            assert "emoji" == "hello world"

        @pytest.mark.xfail
        def test_xfailed():
            assert 1234 == 100

        @pytest.mark.xfail
        def test_xpassed():
            assert 1234 == 1234

        @pytest.mark.skipif(True, reason="don't run this test")
        def test_skipped():
            assert "emoji" == "emoji"

        @pytest.fixture
        def name():
            raise RuntimeError

        @pytest.mark.hello
        def test_error(name):
            assert name == "hello"
        """
    )


@pytest.fixture(name="custom_emojis")
def fixture_custom_emojis():
    return textwrap.dedent(
        """\
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
        """
    )
