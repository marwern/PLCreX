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
from typing import Optional
from plcrex.tools.fbd2ia import _fbd2ia
from plcrex.tools.fbd2st import _fbd2st
from plcrex.tools.ds2ts import _ds2ts
from plcrex.tools.st2ast import _st2ast
from plcrex.tools.xmlval import _xmlval
from pathlib import Path
from plcrex import __app_name__, __version__

app = typer.Typer()

@app.command("ds2ts")
def ds2ts(formula: str):
    _ds2ts.create(formula)
    typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))				  

@app.command("fbd2st")
def fbd2st(
        src: Path,
        export: Path,
        bwd: bool = typer.Option(False, help="use backward translation"),
        formal: bool = typer.Option(False, help="formal parameter list"),
        st2ast: bool = typer.Option(False, help="run ST parser with exports"),
        impact_analysis: bool = typer.Option(False, help="check I/O impact analysis")
):
    if src.is_file():
        if src.suffix == '.xml':
            dir_path  = Path(fr'{export}\PLCreX_outputs')
            # Ensure the directory exists
            os.makedirs(dir_path, exist_ok=True)

            _fbd2st.translation(src, dir_path, bwd, formal, st2ast, impact_analysis)
            if st2ast:
                _st2ast.translation(Path(fr'{dir_path}\{Path(src).name}_{bwd}_{formal}_{st2ast}_{impact_analysis}.st'), dir_path,
                            True, True, False)
            if impact_analysis:
                _fbd2ia.data_flow_analysis_st(Path(fr'{dir_path}\{Path(src).name}_{bwd}_{formal}_{st2ast}_{impact_analysis}.st'), dir_path)
            typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
        else:
            raise RuntimeError("no xml file found")
    raise typer.Exit()


@app.command("st2ast")
def st2ast(
        src: Path,
        export: Path,
        txt: bool = typer.Option(True, help="tree export as *.txt"),
        dot: bool = typer.Option(True, help="tree export as *.dot"),
        beckhoff: bool = typer.Option(False, help="use Beckhoff TwinCAT ST grammar")):
    if src.is_file():
        if src.suffix == '.st':
            dir_path  = Path(fr'{export}\PLCreX_outputs')
            # Ensure the directory exists
            os.makedirs(dir_path, exist_ok=True)

            _st2ast.translation(src, dir_path, txt, dot, beckhoff)
            typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
        else:
            raise RuntimeError("no ST file found")
    raise typer.Exit()


@app.command("xml-val")
def xmlval(
        src: Path,
        v201: bool = typer.Option(False, help="use tc6_xml_v201.xsd")):
    if src.is_file():
        if src.suffix == '.xml':
            if v201:
                # tc6_xml_v201.xsd (https: // plcopen.org / downloads / plcopen-xml-version-201-xsd-file-0)
                _xmlval.validate(src, "tc6_xml_v201.xsd")
                typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
            else:
                # tc6_xml_v10.xsd (Beremiz v1.2)
                _xmlval.validate(src, "tc6_xml_v10.xsd")
                typer.echo("\n" + typer.style("Success!", fg=typer.colors.GREEN, bold=True))
        else:
            raise RuntimeError()
    raise typer.Exit()


def version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} R{__version__}")
        raise typer.Exit()


@app.callback()
def main(version: Optional[bool] = typer.Option(None, "--version", "-v", callback=version_callback, is_eager=True)):
    return
