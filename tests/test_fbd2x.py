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
    result = runner.invoke(cli.app, ["fbd-to-st-ext", "--help"])
    assert result.exit_code == 0

def test_help2():
    result = runner.invoke(cli.app, ["fbd-to-sctx", "--help"])
    assert result.exit_code == 0

def test_wrong_file1():
    result = runner.invoke(cli.app, ["fbd-to-st-ext", "--edge-opt", r".\tests\other_examples\TC001_wrong_file.txt", "bin/NuSMV.exe", r".\exports\st2x1.st"])
    assert result.exit_code == 1

def test_wrong_file2():
    result = runner.invoke(cli.app, ["fbd-to-sctx", "--edge-opt", r".\tests\other_examples\TC001_wrong_file.txt", "bin/NuSMV.exe", r".\exports\st2x1.sctx"])
    assert result.exit_code == 1

def test_edge_opt1_st():
    result = runner.invoke(cli.app, ["fbd-to-st-ext", "--edge-opt", r"tests/real_world_FBDs/Antivalence_3x.xml", "bin/NuSMV.exe", r".\exports\st2x2.st"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_edge_opt1_sctx():
    result = runner.invoke(cli.app, ["fbd-to-sctx", "--edge-opt", r"tests/real_world_FBDs/Antivalence_3x.xml", "bin/NuSMV.exe", r".\exports\st2x2.sctx"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_edge_opt2_st():
    result = runner.invoke(cli.app, ["fbd-to-st-ext", "--edge-opt", r"tests/real_world_FBDs/Bending_Machine_Control.xml", "bin/NuSMV.exe", r".\exports\st2x4.st"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_edge_opt2_sctx():
    result = runner.invoke(cli.app, ["fbd-to-sctx", "--edge-opt", r"tests/real_world_FBDs/Bending_Machine_Control.xml", "bin/NuSMV.exe", r".\exports\st2x4.sctx"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_edge_opt3_st():
    result = runner.invoke(cli.app, ["fbd-to-st-ext", "--edge-opt", r"tests/real_world_FBDs/Cylinder_Control_System.xml", "bin/NuSMV.exe", r".\exports\st2x6.st"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_edge_opt3_sctx():
    result = runner.invoke(cli.app, ["fbd-to-sctx", "--edge-opt", r"tests/real_world_FBDs/Cylinder_Control_System.xml", "bin/NuSMV.exe", r".\exports\st2x6.sctx"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_edge_opt4_st():
    result = runner.invoke(cli.app, ["fbd-to-st-ext", "--edge-opt", r"tests/real_world_FBDs/KV_Diagram_optimized_Chart.xml", "bin/NuSMV.exe", r".\exports\st2x8.st"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_edge_opt4_sctx():
    result = runner.invoke(cli.app, ["fbd-to-sctx", "--edge-opt", r"tests/real_world_FBDs/KV_Diagram_optimized_Chart.xml", "bin/NuSMV.exe", r".\exports\st2x8.sctx"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_var_opt_st():
    result = runner.invoke(cli.app, ["fbd-to-st-ext", "--var-opt", r"tests/real_world_FBDs/Antivalence_3x.xml", "bin/NuSMV.exe", r".\exports\st2x10.st"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_var_opt_sctx():
    result = runner.invoke(cli.app, ["fbd-to-sctx", "--var-opt", r"tests/real_world_FBDs/Antivalence_3x.xml", "bin/NuSMV.exe", r".\exports\st2x10.sctx"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_op_opt_st():
    result = runner.invoke(cli.app, ["fbd-to-st-ext", "--var-opt", r"tests/real_world_FBDs/Antivalence_3x.xml", "bin/NuSMV.exe", r".\exports\st2x12.st"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout

def test_op_opt_sctx():
    result = runner.invoke(cli.app, ["fbd-to-sctx", "--var-opt", r"tests/real_world_FBDs/Antivalence_3x.xml", "bin/NuSMV.exe", r".\exports\st2x12.sctx"])
    assert result.exit_code == 0
    assert f"Success!" in result.stdout