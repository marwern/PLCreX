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


def test_with_static_tests():
    result = runner.invoke(cli.app, ["fbd2st", r".\tests\plcopen_examples\TC004.xml", "-static-tests"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_without_static_tests_fb():
    result = runner.invoke(cli.app, ["fbd2st", r".\tests\plcopen_examples\TC005_FB.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_without_static_tests_prg():
    result = runner.invoke(cli.app, ["fbd2st", r".\tests\plcopen_examples\TC005_PRG.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_without_static_tests_f():
    result = runner.invoke(cli.app, ["fbd2st", r".\tests\plcopen_examples\TC005_FUN.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_with_static_tests_bw():
    result = runner.invoke(cli.app, ["fbd2st", r".\tests\plcopen_examples\TC004.xml", "-static-tests", "-bw"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_without_static_tests_fb_bw():
    result = runner.invoke(cli.app, ["fbd2st", r".\tests\plcopen_examples\TC005_FB.xml", "-bw"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_without_static_tests_prg_bw():
    result = runner.invoke(cli.app, ["fbd2st", r".\tests\plcopen_examples\TC005_PRG.xml", "-bw"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_without_static_tests_f_bw():
    result = runner.invoke(cli.app, ["fbd2st", r".\tests\plcopen_examples\TC005_FUN.xml", "-bw"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_wrong_file():
    result = runner.invoke(cli.app, ["fbd2st", r".\tests\other_examples\TC001_wrong_file.txt"])
    assert result.exit_code == 1
