from typer.testing import CliRunner

from plcrex import cli

runner = CliRunner()

#st2tree ".\tests\st_examples\TC001.st" -dot -txt
#st2tree ".\tests\st_examples\TC001.st" -dot
#st2tree ".\tests\st_examples\TC001.st" -txt

def test_help():
    result = runner.invoke(cli.app, ["st2tree", "--help"])
    assert result.exit_code == 0

def test_dot_txt():
    result = runner.invoke(cli.app, ["st2tree", r".\tests\st_examples\TC081.st", "-dot", "-txt"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_dot():
    result = runner.invoke(cli.app, ["st2tree", r".\tests\st_examples\TC081.st", "-dot"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_txt():
    result = runner.invoke(cli.app, ["st2tree", r".\tests\st_examples\TC081.st", "-txt"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_wrong_file():
    result = runner.invoke(cli.app, ["st2tree", r".\tests\other_examples\TC001_wrong_file.txt", "-txt"])
    assert result.exit_code == 1