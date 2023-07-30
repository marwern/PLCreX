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
    result = runner.invoke(cli.app, ["iec-checker", "--help"])
    assert result.exit_code == 0


def test_help_iec_checker():
    result = runner.invoke(cli.app, ["iec-checker", r".\tests\st_examples\TC001.st", r".\bin\iec_checker_Windows_x86_64_v0.4.exe", "--help_iec_checker"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_verbose_st():
    result = runner.invoke(cli.app, ["iec-checker", r".\tests\st_examples\TC001.st", r".\bin\iec_checker_Windows_x86_64_v0.4.exe", "--verbose"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_quiet_st():
    result = runner.invoke(cli.app, ["iec-checker", r".\tests\st_examples\TC001.st", r".\bin\iec_checker_Windows_x86_64_v0.4.exe"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_wrong_file():
    result = runner.invoke(cli.app, ["iec-checker", r".\tests\other_examples\TC001_wrong_file.txt", r".\bin\iec_checker_Windows_x86_64_v0.4.exe"])
    assert result.exit_code == 1


def test_verbose_xml():
    result = runner.invoke(cli.app, ["iec-checker", r".\tests\plcopen_examples\TC001.xml", r".\bin\iec_checker_Windows_x86_64_v0.4.exe", "--verbose"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_quiet_xml():
    result = runner.invoke(cli.app, ["iec-checker", r".\tests\plcopen_examples\TC001.xml", r".\bin\iec_checker_Windows_x86_64_v0.4.exe"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_wrong_exe():
    result = runner.invoke(cli.app, ["iec-checker", r".\tests\plcopen_examples\TC001.xml", r".\bin\_.exe"])
    assert result.exit_code == 1