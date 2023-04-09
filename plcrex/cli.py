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

from typing import Optional
from plcrex import _st2tree, _iec_checker, _xml_checker, _fbd2st, _spec2test
from docs.source.conf import __app_name__, __version__
from pathlib import Path
import typer

app = typer.Typer()

@app.command("test-case-gen")
def test_case_gen(formula: str):
    _spec2test.create(formula)
    typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))				  


@app.command("iec-checker")
def iec_checker(
        src: Path,
        verbose: bool = typer.Option(False, help="print full log"),
        help_: bool = typer.Option(False, "--help_iec_checker", help="call iec-checker help")):
    if src.is_file():
        if src.suffix == '.st' or src.suffix == '.xml':
            # call iec-checker with ONE supported OPTIONS (only a subset is covered)
            if help_:
                _iec_checker.execution(src, '--help')
            elif not verbose:
                _iec_checker.execution(src, '--quiet')
            elif verbose:
                _iec_checker.execution(src, '--verbose')
            typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
        else:
            raise RuntimeError("no ST/xml file found")
    raise typer.Exit()


@app.command("fbd2st")
def fbd2st(
        src: Path,
        iec_check: bool = typer.Option(False, help="run IEC Checker"),  # "-static-tests",
        formal: bool = typer.Option(False, help="formal parameter list"),
        backward: bool = typer.Option(False, help="use backward translation"),  # "-bw",
        st_parser: bool = typer.Option(False, help="run ST parser with exports"),
        impact_analysis: bool = typer.Option(False, help="chek I/O impact analysis")
):
    if src.is_file():
        if src.suffix == '.xml':
            _fbd2st.translation(src, iec_check, backward, formal, st_parser, impact_analysis)
            typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
        else:
            raise RuntimeError("no xml file found")
    raise typer.Exit()


@app.command("st2tree")
def st2tree(
        src: Path,
        txt: bool = typer.Option(True, help="tree export as *.txt"),
        dot: bool = typer.Option(True, help="tree export as *.dot"),
        beckhoff: bool = typer.Option(False, help="use Beckhoff TwinCAT ST grammar")):
    if src.is_file():
        if src.suffix == '.st':
            _st2tree.translation(src, txt, dot, beckhoff)
            typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
        else:
            raise RuntimeError("no ST file found")
    raise typer.Exit()


@app.command("xml-checker")
def xml_checker(
        src: Path,
        v201: bool = typer.Option(False, help="use tc6_xml_v201.xsd")):
    if src.is_file():
        if src.suffix == '.xml':
            if v201:
                # tc6_xml_v201.xsd (https: // plcopen.org / downloads / plcopen-xml-version-201-xsd-file-0)
                _xml_checker.validate(src, "tc6_xml_v201.xsd")
                typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
            else:
                # tc6_xml_v10.xsd (Beremiz v1.2)
                _xml_checker.validate(src, "tc6_xml_v10.xsd")
                typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
        else:
            raise RuntimeError()
    raise typer.Exit()


def version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(version: Optional[bool] = typer.Option(None, "--version", "-v", callback=version_callback, is_eager=True)):
    return
