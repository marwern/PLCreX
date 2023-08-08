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
import typer

import os
import colorama
from typing import Optional
from plcrex.tools.fbd2ia import _fbd2ia
from plcrex.tools.fbd2st import _fbd2st
from plcrex.tools.ds2ts import _ds2ts
from plcrex.tools.st2ast import _st2ast
from plcrex.tools.xmlval import _xmlval
from plcrex.tools.iec_checker import _iec_checker
from pathlib import Path
from plcrex import __app_name__, __version__
from rich.console import Console

console = Console()
app = typer.Typer(context_settings={"help_option_names": ["--help"]}, add_completion=False, rich_markup_mode="rich")
colorama.init()

# decorator to print name header before every output
def header():
    #print(colored(pyfiglet.figlet_format("PLCreX", font="ANSI Shadow", width=600), 'green'))
    #"Patorjk's Cheese" font by patorjk (patorjk@gmail.com) and x98.
    #ANSI Shadow.flf is not part of pyfiglet v0.7.6
    #changed manually: E -> e, R->r
    #print(typer.style("""
 #██████╗ ██╗      ██████╗██████╗ ███████╗██╗  ██╗
 #██╔══██╗██║     ██╔════╝██╔══██╗██╔════╝╚██╗██╔╝
 #██████╔╝██║     ██║     ██████╔╝█████╗   ╚███╔╝
 #██╔═══╝ ██║     ██║     ██╔══██╗██╔══╝   ██╔██╗
 #██║     ███████╗╚██████╗██║  ██║███████╗██╔╝ ██╗
 #╚═╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝""", fg=typer.colors.BRIGHT_YELLOW, bold=True))
    print(typer.style("""
 ██████╗  ██╗       ██████╗  █████╗   █████╗  ██╗  ██╗
 ██╔══██╗ ██║      ██╔════╝ ██╔══██╗ ██╔══██╗ ╚██╗██╔╝
 ██████╔╝ ██║      ██║      ██║  ╚═╝ ██████╔╝  ╚███╔╝
 ██╔═══╝  ██║      ██║      ██║      ██╔═══╝   ██╔██╗
 ██║      ███████╗ ╚██████╗ ██║      ╚█████╗  ██╔╝ ██╗
 ╚═╝      ╚══════╝  ╚═════╝ ╚═╝       ╚════╝  ╚═╝  ╚═╝
 """, fg=typer.colors.BRIGHT_YELLOW, bold=True))

@app.command("iec-checker", epilog=fr"[yellow]PLCreX-{__version__}, plcrex.info@gmail.com[/yellow]")
def iec_checker(
        source: Path= typer.Argument(help="source path"),
        exe: Path= typer.Argument(help="iec_checker_Windows_x86_64_v0.4.exe path"),
        verbose: bool = typer.Option(False, help="print full log"),
        help_: bool = typer.Option(False, "--help_iec_checker", help="call iec-checker help")):
    if source.is_file():
        if exe.is_file():
            if source.suffix == '.st' or source.suffix == '.xml':
                # call iec-checker with ONE supported OPTIONS (only a subset is covered)
                if help_:
                    _iec_checker.execution(source, exe, '--help')
                elif not verbose:
                    _iec_checker.execution(source, exe, '--quiet')
                elif verbose:
                    _iec_checker.execution(source, exe, '--verbose')
                typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
            else:
                raise RuntimeError("no ST/xml file found")
        else:
            raise RuntimeError(rf"no .exe found at {exe}")
    raise typer.Exit()

@app.command("test-case-gen", epilog=fr"[yellow]PLCreX-{__version__}, plcrex.info@gmail.com[/yellow]")
def ds2ts(formula: str = typer.Argument(help="condition \"(,),&,|,!,==,!=\""),
          constr: str = typer.Option("", help="constraints \"(c1)&(c2)&(..)\""),
          full: bool = typer.Option(True, help="find all solutions")):
    _ds2ts.create(formula, constr, full)
    typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))				  

@app.command("fbd-to-st", epilog=fr"[yellow]PLCreX-{__version__}, plcrex.info@gmail.com[/yellow]")
def fbd2st(
        source: Path= typer.Argument(help="source path"),
        export: Path= typer.Argument(help="export path"),
        filename: str= typer.Argument(help="filename without file extension"),
        bwd: bool = typer.Option(False, help="use backward translation"),
        formal: bool = typer.Option(False, help="formal parameter list"),
):
    if source.is_file():
        if source.suffix == '.xml':
            dir_path  = Path(fr'{export}\PLCreX_outputs')
            # Ensure the directory exists
            os.makedirs(dir_path, exist_ok=True)
            _fbd2st.translation(source, dir_path, filename, bwd, formal)
            typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
        else:
            raise RuntimeError("no xml file found")
    raise typer.Exit()

@app.command("impact-analysis", epilog=fr"[yellow]PLCreX-{__version__}, plcrex.info@gmail.com[/yellow]")
def impact_anal(
        source: Path= typer.Argument(help="source path"),
        export: Path= typer.Argument(help="export path"),
        filename: str= typer.Argument(help="filename without file extension")):
    if source.is_file():
        if source.suffix == '.xml':
            dir_path  = Path(fr'{export}\PLCreX_outputs')
            # Ensure the directory exists
            os.makedirs(dir_path, exist_ok=True)

            #FBD-to-ST
            _fbd2st.translation(source, dir_path, filename, True, False)

            #ST-to-I/O Dependency
            #_fbd2ia.data_flow_analysis_st(Path(fr'{dir_path}\{Path(source).name}_{True}_{False}_{False}_{True}.st'),
            #                              dir_path)
            _fbd2ia.data_flow_analysis_st(Path(fr'{dir_path}\{filename}.st'), dir_path, filename)
            typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
        else:
            raise RuntimeError("no xml file found")
    raise typer.Exit()

@app.command("st-parser", epilog=fr"[yellow]PLCreX-{__version__}, plcrex.info@gmail.com[/yellow]")
def st2ast(
        source: Path= typer.Argument(help="source path"),
        export: Path= typer.Argument(help="export path"),
        filename: str= typer.Argument(help="filename without file extension"),
        txt: bool = typer.Option(True, help="tree export as *.txt"),
        dot: bool = typer.Option(True, help="tree export as *.dot"),
        beckhoff: bool = typer.Option(False, help="use Beckhoff TwinCAT ST grammar")):
    if source.is_file():
        if source.suffix == '.st':
            dir_path  = Path(fr'{export}\PLCreX_outputs')
            # Ensure the directory exists
            os.makedirs(dir_path, exist_ok=True)

            _st2ast.translation(source, dir_path, filename, txt, dot, beckhoff)
            typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
        else:
            raise RuntimeError("no ST file found")
    raise typer.Exit()


@app.command("xml-validator", epilog=fr"[yellow]PLCreX-{__version__}, plcrex.info@gmail.com[/yellow]")
def xmlval(
        source: Path= typer.Argument(help="source path"),
        v201: bool = typer.Option(False, help="use tc6_xml_v201.xsd")):
    #header()
    if source.is_file():
        if source.suffix == '.xml':
            if v201:
                # tc6_xml_v201.xsd (https: // plcopen.org / downloads / plcopen-xml-version-201-xsd-file-0)
                _xmlval.validate(source, "tc6_xml_v201.xsd")
                typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
            else:
                # tc6_xml_v10.xsd (Beremiz v1.2)
                _xmlval.validate(source, "tc6_xml_v10.xsd")
                typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
        else:
            raise RuntimeError()
    raise typer.Exit()


def version_callback(value: bool):
    header()
    if value:
        typer.echo(f"{__app_name__} R{__version__}")
        raise typer.Exit()

@app.callback(epilog=fr"[yellow]PLCreX-{__version__}, plcrex.info@gmail.com[/yellow]")
def main(version: Optional[bool] = typer.Option(None, "--version", callback=version_callback, is_eager=True)):
    return