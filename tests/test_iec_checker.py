from typer.testing import CliRunner

from plcrex import cli

runner = CliRunner()


def test_help():
    result = runner.invoke(cli.app, ["iec-checker", "--help"])
    assert result.exit_code == 0

def test_help_iec_checker():
    result = runner.invoke(cli.app, ["iec-checker", r".\tests\st_examples\TC001.st", "--help_iec_checker"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_v_st():
    result = runner.invoke(cli.app, ["iec-checker", r".\tests\st_examples\TC001.st", "-v"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_v_st_default():
    result = runner.invoke(cli.app, ["iec-checker", r".\tests\st_examples\TC001.st"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_q_st():
    result = runner.invoke(cli.app, ["iec-checker", r".\tests\st_examples\TC001.st", "-q"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_wrong_file():
    result = runner.invoke(cli.app, ["iec-checker", r".\tests\other_examples\TC001_wrong_file.txt", "-q"])
    assert result.exit_code == 1

def test_v_xml():
    result = runner.invoke(cli.app, ["iec-checker", r".\tests\plcopen_examples\TC001.xml", "-v"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_q_xml():
    result = runner.invoke(cli.app, ["iec-checker", r".\tests\plcopen_examples\TC001.xml", "-q"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout