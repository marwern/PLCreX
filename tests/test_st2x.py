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
    result = runner.invoke(cli.app, ["fbd-optimizer", "--help"])
    assert result.exit_code == 0

def test_wrong_file():
    result = runner.invoke(cli.app, ["fbd-optimizer", "--edge-opt", r".\tests\other_examples\TC001_wrong_file.txt", "bin/NuSMV.exe", ".", "st2x1"])
    assert result.exit_code == 1

def test_edge_opt1():
    result = runner.invoke(cli.app, ["fbd-optimizer", "--edge-opt", r"tests/real_world_FBDs/Antivalence_3x.xml", "bin/NuSMV.exe", ".", "st2x2"])
    assert result.exit_code == 0

    result = runner.invoke(cli.app,
                           ["st-parser", "--beckhoff", r".\PLCreX_outputs\st2x2.st", ".", "st2x3"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_edge_opt2():
    result = runner.invoke(cli.app, ["fbd-optimizer", "--edge-opt", r"tests/real_world_FBDs/Bending_Machine_Control.xml", "bin/NuSMV.exe", ".", "st2x4"])
    assert result.exit_code == 0

    result = runner.invoke(cli.app,
                           ["st-parser", "--beckhoff", r".\PLCreX_outputs\st2x4.st", ".", "st2x5"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_edge_opt3():
    result = runner.invoke(cli.app, ["fbd-optimizer", "--edge-opt", r"tests/real_world_FBDs/Cylinder_Control_System.xml", "bin/NuSMV.exe", ".", "st2x6"])
    assert result.exit_code == 0

    result = runner.invoke(cli.app,
                           ["st-parser", "--beckhoff", r".\PLCreX_outputs\st2x6.st", ".", "st2x7"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout


def test_edge_opt4():
    result = runner.invoke(cli.app, ["fbd-optimizer", "--edge-opt", r"tests/real_world_FBDs/KV_Diagram_optimized_Chart.xml", "bin/NuSMV.exe", ".", "st2x8"])
    assert result.exit_code == 0

    result = runner.invoke(cli.app,
                           ["st-parser", "--beckhoff", r".\PLCreX_outputs\st2x8.st", ".", "st2x9"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_var_opt():
    result = runner.invoke(cli.app, ["fbd-optimizer", "--var-opt", r"tests/real_world_FBDs/Antivalence_3x.xml", "bin/NuSMV.exe", ".", "st2x10"])
    assert result.exit_code == 0

    result = runner.invoke(cli.app,
                           ["st-parser", r".\PLCreX_outputs\st2x10.st", ".", "st2x11"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_op_opt():
    result = runner.invoke(cli.app, ["fbd-optimizer", "--var-opt", r"tests/real_world_FBDs/Antivalence_3x.xml", "bin/NuSMV.exe", ".", "st2x12"])
    assert result.exit_code == 0

    result = runner.invoke(cli.app,
                           ["st-parser", r".\PLCreX_outputs\st2x12.st", ".", "st2x13"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout