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


def test_1bwd_0formal_0iec_0st2tree44_1impact_analysis():
    result = runner.invoke(cli.app, ["fbd2st", "--backward", "--no-formal", "--impact-analysis", r".\tests\plcopen_examples\TC006_FBD.xml"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout
