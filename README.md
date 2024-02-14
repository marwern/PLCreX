PLCreX - Simplification, Transformation, Analysis, and Validation of IEC 61131-3 Programmable Logic Controllers
===============================================================================================================

<!-- -->
<!-- [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) -->
<!-- [![made-with-sphinx-doc](https://img.shields.io/badge/Made%20with-Sphinx-1f425f.svg)](https://www.sphinx-doc.org/) -->
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Windows](https://badgen.net/badge/icon/windows?icon=windows&label)](https://microsoft.com/windows/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Tests](https://img.shields.io/badge/Tests-passed-<COLOR>.svg)](https://shields.io/)
[![Coverage](https://img.shields.io/badge/coverage-96%25-<COLOR>.svg)](https://shields.io/)
[![Documentation Status](https://readthedocs.org/projects/plcrex/badge/?version=latest)](https://plcrex.readthedocs.io/en/latest/?badge=latest)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

<br />
<div align="center">
  <img src="https://github.com/marwern/PLCreX/assets/92115516/8558b705-720a-4e8c-80cb-10747f38fa58" width=650> <!-- width=400 -->

  <!-- <h3 align="center">PLCreX</h3> -->

  <p align="center">
    <strong>Quick links</strong>
    <br />
    <br />
    <a href="https://pypi.org/project/plcrex/">Releases</a>
    ·
    <a href="https://plcrex.readthedocs.io/en">Documentation</a>
    ·
    <a href="#quick-start">Quick Start</a>
    ·
    <a href="#key-features">Key Features</a>
    ·
    <a href="#licenses">Licenses</a>
    ·
    <a href="#acknowledgments">Acknowledgments</a>
  </p>
</div>

---


Quick Start
===========
<strong><a href="https://plcrex.readthedocs.io/en">Explore the docs »</a></strong>

* Download Python ``v3.9`` [[.url](https://www.python.org/downloads/release/python-390/)]
* Download IEC-Checker ``v0.4`` via IEC-Checker's GitHub releases [[.url](https://github.com/jubnzv/iec-checker/releases/tag/v0.4)]
* Download Kicodia ``v122798884`` via KIELER's Download page [[.url](https://rtsys.informatik.uni-kiel.de/~kieler/files/nightly/sccharts/cli/)]
* Download NuSMV symbolic model checker ``v2.6.0`` via NuSMV's homepage [[.url](https://nusmv.fbk.eu/)]
* Download Microsoft Build Tools 2015 [.url](https://www.microsoft.com/de-de/download/details.aspx?id=48159)
* Install PLCreX via PyPI: ``pip install plcrex`` or
* Install PLCreX via PLCreX's GitHub repository: ``install-windows.bat``
     * Activate virtual environment (venv): ``run.bat``
     * [optional] Run local tests: ``coverage run -m pytest ./tests/ --verbose``


Key Features
============

```
 Usage: plcrex [OPTIONS] COMMAND [ARGS]...

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --version                                                                                                      │
│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell.       │
│                                                              [default: None]                                   │
│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell, to copy  │
│                                                              it or customize the installation.                 │
│                                                              [default: None]                                   │
│ --help                                                       Show this message and exit.                       │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ fbd-to-sctx              FBD-to-SCCharts Compiler (Data-Flow)    *.xml → *.sctx                                │
│ fbd-to-st                FBD-to-ST Compiler                      *.xml → *.st                                  │
│ fbd-to-st-ext            FBD-to-ST Compiler (extended)           *.xml → *.st                                  │
│ iec-check                IEC-Checker                             *.st → *.log                                  │
│ impact-analysis          I/O-Impact Analysis                     *.xml → *.dot                                 │
│ st-parser                ST-Parser                               *.st → *.dot/*.txt                            │
│ st-to-qrz                ST-to-Quartz Compiler                   *.st → *.qrz                                  │
│ st-to-scl                ST-to-SCL Compiler                      *.st → *.scl                                  │
│ st-to-sctx               ST-to-SCCharts Compiler (Control-Flow)  *.st → *.sctx                                 │
│ test-case-gen            Test-Case-Generator                     stdin → stdout                                │
│ xml-validator            XML-Validator                           *.xml → stdout                                │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

<strong><a href="https://plcrex.readthedocs.io/en">Explore the docs »</a></strong>

Usage: ``python -m plcrex --help``

<!--- <img src="https://github.com/marwern/PLCreX/assets/92115516/1afecd73-a1b0-4c84-98e5-53086f684483" width=650> --->


Analysis & Validation
=====================

| Description         | Script     | Version |
|---------------------|------------|---------|
| IEC-Checker         | ieccheck   | 2.0.0   |
| I/O-Impact Analysis | fbdia      | 2.0.0   |
| ST-Parser           | stp        | 2.0.0   |
| Test-Case-Generator | tcgen      | 4.0.0   |
| XML-Validator       | xmlval     | 2.0.0   |


Transformation & Simplification
===============================

| Description          | Script  | Version | 
|----------------------|---------|---------|
| FBD-to-ST            | fbd2st  | 2.0.0   | 
| FBD-to-ST (extended) | fbd2st  | 2.0.0   |
| FBD-to-SCCharts      | fbd2x   | 2.0.0   | 
| ST-to-Quartz         | st2qrz  | 1.0.0   |
| ST-to-SCL            | st2scl  | 1.0.0   |
| ST-to-SCCharts       | st2scl  | 1.0.0   |


Models
======

The translations of the models are based on PLCreX's intermediate model ``*.pim``:

| Package           | Description                         | Version |
|-------------------|-------------------------------------|---------|
| ``st``            | Structured Text                     | 1.0.2  |
| ``qrz``           | Quartz Model                        | 1.0.1   |
| ``scl``           | Sequentially Constructive Language  | 1.0.2   |


Licenses
========
PLCreX and its dependencies are licensed as follows:

| Tool        | Version    | License                      |
|-------------|------------|------------------------------|
| PLCreX      | 2.0.0      | GPLv3                        |
| IEC-Checker | 0.4        | LGPL v3.0                    |
| NuSMV       | 2.6.0      | LGPL v2.1                    |
| KIELER      | 122798884  | Eclipse Public License (EPL) | 


Acknowledgments
===============
Inspiration, code snippets, etc.

* blark [[v0.5.0](https://github.com/klauer/blark/releases/tag/v0.5.0)]
* IEC-Checker [[v0.4](https://github.com/jubnzv/iec-checker/releases/tag/v0.4)]