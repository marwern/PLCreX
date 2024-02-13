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


def test_help1():
    result = runner.invoke(cli.app, ["st-to-scl", "--help"])
    assert result.exit_code == 0

def test_help2():
    result = runner.invoke(cli.app, ["st-to-sctx", "--help"])
    assert result.exit_code == 0

def test_tc01_22_scl():
    for i in range(1, 22):
        if i != 3:
            result = runner.invoke(cli.app,
                                   ["st-to-scl", fr"tests/st_to_synchr_models/TC{i:02}.st",
                                    fr"exports/TC{i:02}.scl"])
            assert result.exit_code == 0
            assert f"Success!" in result.stdout

def test_tc01_22_sctx():
    for i in range(1, 22):
        if i != 3:
            result = runner.invoke(cli.app,
                                   ["st-to-sctx", fr"tests/st_to_synchr_models/TC{i:02}.st",
                                    fr"exports/TC{i:02}.sctx", r".\bin\kicodia-win.bat"])
            assert result.exit_code == 0
            assert f"Success!" in result.stdout
