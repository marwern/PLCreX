#
# This file is part of PLCreX (https://github.com/marwern/PLCreX).
#
# Copyright (c) 2022 Marcel Werner.
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
    result = runner.invoke(cli.app, ["fbd2st", "--help"])
    assert result.exit_code == 0


def test_wrong_file():
    result = runner.invoke(cli.app, ["fbd2st", r".\tests\other_examples\TC001_wrong_file.txt"])
    assert result.exit_code == 1


# TC004 Function Block

# 0 0 0 0
def test_0bwd_0formal_0iec_0st2tree():
    result = runner.invoke(cli.app, ["fbd2st", r".\tests\plcopen_examples\TC004.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# 0 0 0 1
def test_0bwd_0formal_0iec_1st2tree():
    result = runner.invoke(cli.app, ["fbd2st", "--st-parser", r".\tests\plcopen_examples\TC004.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# 0 0 1 0
def test_0bwd_0formal_1iec_0st2tree():
    result = runner.invoke(cli.app, ["fbd2st", "--iec-check", r".\tests\plcopen_examples\TC004.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# 0 0 1 1
def test_0bwd_0formal_1iec_1st2tree():
    result = runner.invoke(cli.app, ["fbd2st", "--iec-check", "--st-parser", r".\tests\plcopen_examples\TC004.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# 0 1 0 0
def test_0bwd_1formal_0iec_0st2tree():
    result = runner.invoke(cli.app, ["fbd2st", "--formal", r".\tests\plcopen_examples\TC004.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# 0 1 0 1
# formal + st2tree not supported by st2tree

# 0 1 1 0
def test_0bwd_1formal_1iec_0st2tree():
    result = runner.invoke(cli.app, ["fbd2st", "--formal", "--iec-check", r".\tests\plcopen_examples\TC004.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# 0 1 1 1
# formal + st2tree not supported by st2tree

# 1 0 0 0
def test_1bwd_0formal_0iec_0st2tree():
    result = runner.invoke(cli.app, ["fbd2st", "--backward", r".\tests\plcopen_examples\TC004.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# 1 0 0 1
def test_1bwd_0formal_0iec_1st2tree():
    result = runner.invoke(cli.app, ["fbd2st", "--backward", "--st-parser", r".\tests\plcopen_examples\TC004.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# 1 0 1 0
def test_1bwd_0formal_1iec_0st2tree():
    result = runner.invoke(cli.app, ["fbd2st", "--backward", "--iec-check", r".\tests\plcopen_examples\TC004.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# 1 0 1 1
def test_1bwd_0formal_1iec_1st2tree():
    result = runner.invoke(cli.app, ["fbd2st", "--backward", "--iec-check", "--st-parser",
                                     r".\tests\plcopen_examples\TC004.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# 1 1 0 0
def test_1bwd_1formal_0iec_0st2tree():
    result = runner.invoke(cli.app, ["fbd2st", "--backward", "--formal", r".\tests\plcopen_examples\TC004.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# 1 1 0 1
# formal + st2tree not supported by st2tree

# 1 1 1 0
def test_1bwd_1formal_1iec_0st2tree():
    result = runner.invoke(cli.app,
                           ["fbd2st", "--backward", "--formal", "--iec-check", r".\tests\plcopen_examples\TC004.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# 1 1 1 1
# formal + st2tree not supported by st2tree

# TC005 Function Block
def test_0bwd_0formal_0iec_0st2tree2():
    result = runner.invoke(cli.app, ["fbd2st", r".\tests\plcopen_examples\TC005_FB.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# TC005 Function
def test_0bwd_0formal_0iec_0st2tree3():
    result = runner.invoke(cli.app, ["fbd2st", r".\tests\plcopen_examples\TC005_FUN.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# TC005 Program
def test_0bwd_0formal_0iec_0st2tree4():
    result = runner.invoke(cli.app, ["fbd2st", r".\tests\plcopen_examples\TC005_PRG.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# TC005 Program
def test_1bwd_1formal_0iec_0st2tree5():
    result = runner.invoke(cli.app, ["fbd2st", "--backward", "--formal", r".\tests\plcopen_examples\TC005_PRG.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# TC005 Program
def test_1bwd_0formal_0iec_0st2tree6():
    result = runner.invoke(cli.app, ["fbd2st", "--backward", r".\tests\plcopen_examples\TC005_PRG.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# tests to show differences in translation strategies -- START
def test_1bwd_0formal_0iec_0st2tree11():
    result = runner.invoke(cli.app, ["fbd2st", "--backward", r".\tests\plcopen_examples\TC005_PRG.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_1bwd_0formal_0iec_0st2tree22():
    result = runner.invoke(cli.app, ["fbd2st", "--backward", "--formal", r".\tests\plcopen_examples\TC005_PRG.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_1bwd_0formal_0iec_0st2tree33():
    result = runner.invoke(cli.app, ["fbd2st", "--formal", r".\tests\plcopen_examples\TC005_PRG.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_1bwd_0formal_0iec_0st2tree44():
    result = runner.invoke(cli.app, ["fbd2st", r".\tests\plcopen_examples\TC005_PRG.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout
# tests to show differences in translation strategies -- END

