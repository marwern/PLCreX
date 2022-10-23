from typer.testing import CliRunner

from plcrex import __app_name__, __version__, cli

runner = CliRunner()

def test_version_1():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout

def test_version_2():
    result = runner.invoke(cli.app, ["-v"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout