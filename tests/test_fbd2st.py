#
# This file is part of PLCreX (https://github.com/marwern/PLCreX).
#
# Copyright (c) 2022-2023 Marcel Werner.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from typer.testing import CliRunner

from plcrex import cli

runner = CliRunner()


def test_help():
    result = runner.invoke(cli.app, ["fbd-to-st", "--help"])
    assert result.exit_code == 0


def test_wrong_file():
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\other_examples\TC001_wrong_file.txt", "."])
    assert result.exit_code == 1


# TC004 Function Block

# 0 0 0 0
def test_0bwd_0formal_0iec_0st2ast():
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\plcopen_examples\TC004.xml", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# 0 0 0 1
def test_0bwd_0formal_0iec_1st2ast():
    result = runner.invoke(cli.app, ["fbd-to-st", "--st2ast", r".\tests\plcopen_examples\TC004.xml", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout



# 0 1 0 0
def test_0bwd_1formal_0iec_0st2ast():
    result = runner.invoke(cli.app, ["fbd-to-st", "--formal", r".\tests\plcopen_examples\TC004.xml", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# 0 1 0 1
# formal + st2ast not supported by st2ast


# 0 1 1 1
# formal + st2ast not supported by st2ast

# 1 0 0 0
def test_1bwd_0formal_0iec_0st2ast():
    result = runner.invoke(cli.app, ["fbd-to-st", "--bwd", r".\tests\plcopen_examples\TC004.xml", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# 1 0 0 1
def test_1bwd_0formal_0iec_1st2ast():
    result = runner.invoke(cli.app, ["fbd-to-st", "--bwd", "--st2ast", r".\tests\plcopen_examples\TC004.xml", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout



# 1 1 0 0
def test_1bwd_1formal_0iec_0st2ast():
    result = runner.invoke(cli.app, ["fbd-to-st", "--bwd", "--formal", r".\tests\plcopen_examples\TC004.xml", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout



# 1 1 1 1
# formal + st2ast not supported by st2ast

# TC005 Function Block
def test_0bwd_0formal_0iec_0st2ast2():
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\plcopen_examples\TC005_FB.xml", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# TC005 Function
def test_0bwd_0formal_0iec_0st2ast3():
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\plcopen_examples\TC005_FUN.xml", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# TC005 Program
def test_0bwd_0formal_0iec_0st2ast4():
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\plcopen_examples\TC005_PRG.xml", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# TC005 Program
def test_1bwd_1formal_0iec_0st2ast5():
    result = runner.invoke(cli.app, ["fbd-to-st", "--bwd", "--formal", r".\tests\plcopen_examples\TC005_PRG.xml", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# TC005 Program
def test_1bwd_0formal_0iec_0st2ast6():
    result = runner.invoke(cli.app, ["fbd-to-st", "--bwd", r".\tests\plcopen_examples\TC005_PRG.xml", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# tests to show differences in translation strategies -- START
def test_1bwd_0formal_0iec_0st2ast11():
    result = runner.invoke(cli.app, ["fbd-to-st", "--bwd", r".\tests\plcopen_examples\TC005_PRG.xml", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_1bwd_0formal_0iec_0st2ast22():
    result = runner.invoke(cli.app, ["fbd-to-st", "--bwd", "--formal", r".\tests\plcopen_examples\TC005_PRG.xml", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_1bwd_0formal_0iec_0st2ast33():
    result = runner.invoke(cli.app, ["fbd-to-st", "--formal", r".\tests\plcopen_examples\TC005_PRG.xml", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_1bwd_0formal_0iec_0st2ast44():
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\plcopen_examples\TC005_PRG.xml", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout
# tests to show differences in translation strategies -- END

