import inspect

from hundred_coverage import __version__


def test_smoke() -> None:
    assert __version__ is not None
