from typer.testing import CliRunner

from plcrex import cli

runner = CliRunner()

def test_help():
    result = runner.invoke(cli.app, ["xml-checker", "--help"])
    assert result.exit_code == 0

def test_v201_passed():
    result = runner.invoke(cli.app, ["xml-checker", r".\tests\plcopen_examples\TC001.xml", "-v201"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_v201_failed():
    result = runner.invoke(cli.app, ["xml-checker", r".\tests\plcopen_examples\TC001_failed.xml", "-v201"])
    assert result.exit_code == 1

def test_v10_failed():
    result = runner.invoke(cli.app, ["xml-checker", r".\tests\plcopen_examples\TC001.xml", "-v10"])
    assert result.exit_code == 1

def test_wrong_file():
    result = runner.invoke(cli.app, ["xml-checker", r".\tests\other_examples\TC001_wrong_file.txt", "-v201"])
    assert result.exit_code == 1