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
    result = runner.invoke(cli.app, ["iec-check", "--help"])
    assert result.exit_code == 0


def test_help_iec_checker():
    result = runner.invoke(cli.app, ["iec-check", r".\tests\st_examples\TC001.st", r".\bin\iec_checker_Windows_x86_64_v0.4.exe", "--help_iec_checker", r".\exports\iec_checker1"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_verbose_st():
    result = runner.invoke(cli.app, ["iec-check", r".\tests\st_examples\TC001.st", r".\bin\iec_checker_Windows_x86_64_v0.4.exe", "--verbose", r".\exports\iec_checker2"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_quiet_st():
    result = runner.invoke(cli.app, ["iec-check", r".\tests\st_examples\TC001.st", r".\bin\iec_checker_Windows_x86_64_v0.4.exe", r".\exports\iec_checker3"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_wrong_file():
    result = runner.invoke(cli.app, ["iec-check", r".\tests\other_examples\TC001_wrong_file.txt", r".\bin\iec_checker_Windows_x86_64_v0.4.exe", r".\exports\iec_checker4"])
    assert result.exit_code == 1


def test_verbose_xml():
    result = runner.invoke(cli.app, ["iec-check", r".\tests\plcopen_examples\TC001.xml", r".\bin\iec_checker_Windows_x86_64_v0.4.exe", "--verbose", r".\exports\iec_checker5"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_quiet_xml():
    result = runner.invoke(cli.app, ["iec-check", r".\tests\plcopen_examples\TC001.xml", r".\bin\iec_checker_Windows_x86_64_v0.4.exe", r".\exports\iec_checker6"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_wrong_exe():
    result = runner.invoke(cli.app, ["iec-check", r".\tests\plcopen_examples\TC001.xml", r".\bin\_.exe", r".\exports\iec_checker7"])
    assert result.exit_code == 1
