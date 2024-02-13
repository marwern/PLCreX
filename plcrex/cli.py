#
# This file is part of PLCreX (https://github.com/marwern/PLCreX).
#
# Copyright (c) 2022-2024 Marcel C. Werner.
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

import colorama
from typing import Optional
from plcrex.tools.fbdia import call_io_analysis
from plcrex.tools.fbd2st import call_fbd2st_compiler
from plcrex.tools.tcgen import call_test_case_gen
from plcrex.tools.stp import call_st_parser
from plcrex.tools.fbd2x import call_fbd_optimizer
from plcrex.tools.xmlval import call_xml_validator
from plcrex.tools.ieccheck import call_iec_checker
from plcrex.tools.st2qrz import call_st2qrz_compiler
from plcrex.tools.st2scl import call_st2scl_compiler
from plcrex.tools.misc.generic_functions import *
from pathlib import Path
from plcrex import __version__
from rich.console import Console
import os

console = Console()
app = typer.Typer(context_settings={"help_option_names": ["--help"]}, add_completion=True, rich_markup_mode="rich")
colorama.init()

# -----------------------------------------------------------------------------------------------------------------
@app.command("fbd-to-sctx")
def fbd2sctx(
        source: Path = typer.Argument(help="source path"),
        exe: Path = typer.Argument(help="NuSMV.exe path"),
        export: Path = typer.Argument(help="export path"),
        edge_opt: bool = typer.Option(False, help="optimize edges"),
        var_opt: bool = typer.Option(False, help="optimize variables"),
        op_opt: bool = typer.Option(False, help="optimize operators")
        ):
    """FBD-to-SCCharts Compiler (Data-Flow)\t*.xml → *.sctx"""
    # Extract the base name (file name with extension)
    base_name = os.path.basename(export)
    filename, _ = os.path.splitext(base_name)
    call_fbd_optimizer.cli(source, export, filename, exe, edge_opt, var_opt, op_opt, "sctx")
    typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
    raise typer.Exit()
# -----------------------------------------------------------------------------------------------------------------
@app.command("fbd-to-st")
def fbd2st(
        source: Path = typer.Argument(help="source path"),
        export: Path = typer.Argument(help="export path"),
        bwd: bool = typer.Option(False, help="use backward translation"),
        formal: bool = typer.Option(False, help="formal parameter list")
        ):
    """FBD-to-ST Compiler\t\t\t*.xml → *.st"""
    # Extract the base name (file name with extension)
    base_name = os.path.basename(export)
    filename, _ = os.path.splitext(base_name)
    dir_name = os.path.dirname(export)
    call_fbd2st_compiler.cli(source, Path(dir_name), filename, bwd, formal)
    typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
    raise typer.Exit()
# -----------------------------------------------------------------------------------------------------------------
@app.command("fbd-to-st-ext")
def fbd2stext(
        source: Path = typer.Argument(help="source path"),
        exe: Path = typer.Argument(help="NuSMV.exe path"),
        export: Path = typer.Argument(help="export path"),
        edge_opt: bool = typer.Option(False, help="optimize edges"),
        var_opt: bool = typer.Option(False, help="optimize variables"),
        op_opt: bool = typer.Option(False, help="optimize operators")
        ):
    """FBD-to-ST Compiler (extended)\t\t*.xml → *.st"""
    # Extract the base name (file name with extension)
    base_name = os.path.basename(export)
    filename, _ = os.path.splitext(base_name)
    dir_name = os.path.dirname(export)
    call_fbd_optimizer.cli(source, Path(dir_name), filename, exe, edge_opt, var_opt, op_opt, "st")
    typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
    raise typer.Exit()
# -----------------------------------------------------------------------------------------------------------------
@app.command("iec-check")
def ieccheck(
        source: Path = typer.Argument(help="source path"),
        exe: Path = typer.Argument(help="iec_checker_Windows_x86_64_v0.4.exe path"),
        export: Path = typer.Argument(help="export path"),
        verbose: bool = typer.Option(False, help="print full log"),
        help_: bool = typer.Option(False, "--help_iec_checker", help="call iec-check help")
):
    """IEC-Checker\t\t\t\t*.st → *.log"""
    # Extract the base name (file name with extension)
    base_name = os.path.basename(export)
    filename, _ = os.path.splitext(base_name)
    dir_name = os.path.dirname(export)
    call_iec_checker.cli(source, exe, verbose, Path(dir_name), filename, help_)
    typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
    raise typer.Exit()
# -----------------------------------------------------------------------------------------------------------------
@app.command("impact-analysis")
def fbdia(
        source: Path = typer.Argument(help="source path"),
        export: Path = typer.Argument(help="export path")
        ):
    """I/O-Impact Analysis\t\t\t*.xml → *.dot"""
    # Extract the base name (file name with extension)
    base_name = os.path.basename(export)
    filename, _ = os.path.splitext(base_name)
    dir_name = os.path.dirname(export)
    call_io_analysis.cli(source, Path(dir_name), filename)
    typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
    raise typer.Exit()
# -----------------------------------------------------------------------------------------------------------------
@app.command("st-parser")
def stp(
        source: Path = typer.Argument(help="source path"),
        export: Path = typer.Argument(help="export path"),
        txt: bool = typer.Option(True, help="tree export as *.txt"),
        dot: bool = typer.Option(True, help="tree export as *.dot"),
        beckhoff: bool = typer.Option(False, help="use Beckhoff TwinCAT ST grammar")
        ):
    """ST-Parser\t\t\t\t*.st → *.dot/*.txt"""
    # Extract the base name (file name with extension)
    base_name = os.path.basename(export)
    filename, _ = os.path.splitext(base_name)
    dir_name = os.path.dirname(export)
    call_st_parser.cli(source, Path(dir_name), filename, txt, dot, beckhoff)
    typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
    raise typer.Exit()
# -----------------------------------------------------------------------------------------------------------------
@app.command("st-to-qrz")
def st2qrz(
        source: Path = typer.Argument(help="source path"),
        export: Path = typer.Argument(help="export path")
        ):
    """ST-to-Quartz Compiler\t\t\t*.st → *.qrz"""
    call_st2qrz_compiler.cli(source, export)
    typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
    raise typer.Exit()
# -----------------------------------------------------------------------------------------------------------------
@app.command("st-to-scl")
def st2scl(
        source: Path = typer.Argument(help="source path"),
        export: Path = typer.Argument(help="export path"),
        ):
    """ST-to-SCL Compiler\t\t\t*.st → *.scl"""
    call_st2scl_compiler.cli(source, export, Path(""), "scl")
    typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
    raise typer.Exit()
# -----------------------------------------------------------------------------------------------------------------
@app.command("st-to-sctx")
def st2sctx(
        source: Path = typer.Argument(help="source path"),
        export: Path = typer.Argument(help="export path"),
        bat_dir: Path = typer.Argument(help="kicodia-win.bat path")
        ):
    """ST-to-SCCharts Compiler (Control-Flow)\t*.st → *.sctx"""
    call_st2scl_compiler.cli(source, export, bat_dir, "sctx")
    typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
    raise typer.Exit()
# -----------------------------------------------------------------------------------------------------------------
@app.command("test-case-gen")  # epilog=fr"[yellow]PLCreX-{__version__}, plcrex.info@gmail.com[/yellow]"
def tcgen(formula: str = typer.Argument(help="condition \"(,),&,|,^,~,<=>,0,1,?:\""),
          sc: bool = typer.Option(False, help="print statement coverage test case"),
          dc: bool = typer.Option(False, help="print decision coverage test cases"),
          mcdc: bool = typer.Option(False, help="print modified condition/decision coverage test cases"),
          mcc: bool = typer.Option(False, help="print multiple condition coverage test cases")
          ):
    """Test-Case-Generator\t\t\tstdin → stdout"""
    call_test_case_gen.cli(formula, sc, dc, mcdc, mcc)
    typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
    raise typer.Exit()
# -----------------------------------------------------------------------------------------------------------------
@app.command("xml-validator")
def xmlval_cli(
        source: Path = typer.Argument(help="source path"),
        v201: bool = typer.Option(False, help="use tc6_xml_v201.xsd")
        ):
    """XML-Validator\t\t\t\t*.xml → stdout"""
    call_xml_validator.cli(source, v201)
    typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
    raise typer.Exit()
# -----------------------------------------------------------------------------------------------------------------
def version_callback(value: bool):
    # print_plcrex_header()
    if value:
        typer.echo(fr"""
PLCreX-{__version__}, plcrex.info@gmail.com

Copyright (c) 2022-2024 Marcel C. Werner.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
        """)
        raise typer.Exit()
# -----------------------------------------------------------------------------------------------------------------
@app.callback()  # epilog=fr"[yellow]PLCreX-{__version__}, plcrex.info@gmail.com[/yellow]"
def main(
        version: Optional[bool] = typer.Option(None, "--version", callback=version_callback, is_eager=True)
    ):
    return
