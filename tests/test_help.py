from typer.testing import CliRunner

from plcrex import __app_name__, __version__, cli

runner = CliRunner()

def test_help():
    result = runner.invoke(cli.app, ["--help"])
    assert result.exit_code == 0