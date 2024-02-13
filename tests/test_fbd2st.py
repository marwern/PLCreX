#
# This file is part of PLCreX (https://github.com/marwern/PLCreX).
#
# Copyright (c) 2022-2023 Marcel C. Werner.
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
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\other_examples\TC001_wrong_file.txt", r".\exports\fbd2st1.st"])
    assert result.exit_code == 1


# TC004 Function Block

# test_nobwd_noformal1
def test_nobwd_noformal1():
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\plcopen_examples\TC004.xml", r".\exports\fbd2st2.st"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# test_nobwd_noformal2
def test_nobwd_noformal2():
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\plcopen_examples\TC005_FB.xml", r".\exports\fbd2st3.st"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# test_nobwd_noformal3
def test_nobwd_noformal3():
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\plcopen_examples\TC005_FUN.xml", r".\exports\fbd2st4.st"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# test_nobwd_noformal4
def test_nobwd_noformal4():
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\plcopen_examples\TC005_PRG.xml", r".\exports\fbd2st5.st"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# test_nobwd_formal1
def test_nobwd_formal1():
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\plcopen_examples\TC004.xml", r".\exports\fbd2st62.st", "--formal"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# test_nobwd_formal2
def test_nobwd_formal2():
    result = runner.invoke(cli.app,
                           ["fbd-to-st", r".\tests\plcopen_examples\TC005_PRG.xml", r".\exports\fbd2st7.st", "--formal"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# formal + stp not supported by stp

# test_bwd_noformal1
def test_bwd_noformal1():
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\plcopen_examples\TC004.xml", r".\exports\fbd2st8.st", "--bwd"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# test_bwd_noformal2
def test_bwd_noformal2():
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\plcopen_examples\TC005_PRG.xml", r".\exports\fbd2st9.st", "--bwd"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# test_bwd_formal1
def test_bwd_formal1():
    result = runner.invoke(cli.app,
                           ["fbd-to-st", r".\tests\plcopen_examples\TC004.xml", r".\exports\fbd2st10.st", "--bwd", "--formal"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# test_bwd_formal2
def test_bwd_formal2():
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\plcopen_examples\TC005_PRG.xml", r".\exports\fbd2st11.st", "--bwd",
                                     "--formal"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


# test_bwd_noformal_st2ast
def test_bwd_noformal_st2ast():
    result = runner.invoke(cli.app, ["fbd-to-st", r".\tests\plcopen_examples\TC004.xml", r".\exports\fbd2st12.st", "--bwd"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout
    #result = runner.invoke(cli.app,
    #                       ["st-parser", r".\PLCreX_outputs\fbd2st12.st", r".\exports\fbdst13", "--txt"])
    #assert result.exit_code == 0
    assert f"Success!" in result.stdout
