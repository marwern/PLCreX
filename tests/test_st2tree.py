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
    result = runner.invoke(cli.app, ["st2ast", "--help"])
    assert result.exit_code == 0


def test_dot_txt():
    result = runner.invoke(cli.app, ["st2ast", r".\tests\st_examples\TC081.st", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_dot():
    result = runner.invoke(cli.app, ["st2ast", "--no-txt", r".\tests\st_examples\TC081.st", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_txt():
    result = runner.invoke(cli.app, ["st2ast", "--no-dot", r".\tests\st_examples\TC081.st", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_beckhoff_txt_dot():
    result = runner.invoke(cli.app, ["st2ast", "--beckhoff", r".\tests\st_examples\TC079.st", "."])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_wrong_file():
    result = runner.invoke(cli.app, ["st2ast", r".\tests\other_examples\TC001_wrong_file.txt", "."])
    assert result.exit_code == 1
