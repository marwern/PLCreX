# PLCreX - a modular IEC 61131-3 PLC analysis CLI application

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-passed-<COLOR>.svg)](https://shields.io/)
[![Coverage](https://img.shields.io/badge/coverage-99%25-<COLOR>.svg)](https://shields.io/)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

PLCreX is a modular command-line interface (CLI) application tailored for IEC 61131-3 Programmable Logic Controllers ([PLCs](https://en.wikipedia.org/wiki/Programmable_logic_controller)). It's designed with a focus on issues such as **re**view, **re**design, **re**use, and **re**liability, among others. This project is driven by our ongoing research and we're committed to progressively integrating new features. PLCreX serves as a comprehensive suite of analysis and reuse capabilities for existing IEC 61131-3 Program Organization Units ([POUs](https://en.wikipedia.org/wiki/IEC_61131-3#Program_organization_unit_(POU))) implemented in Function Block Diagrams (FBDs) or Structured Text (ST).

![diagram-20230730](https://github.com/marwern/PLCreX/assets/92115516/05e44b6c-d023-48f8-b6fa-2a18ccfcea06)

## Quick links

<!-- [📄 PLCreX’s documentation](https://plcrex.readthedocs.io/en/latest/) [![Documentation Status](https://readthedocs.org/projects/plcrex/badge/?version=latest)](https://plcrex.readthedocs.io/en/latest/?badge=latest) -->

* [📄 PLCreX Wiki](https://github.com/marwern/PLCreX/wiki)
* [🛠 Getting Started](#-getting-started)
* [💻 Commands](#-commands)
* [📜 Publications](#-publications)
* [ℹ️ Licenses](#-licenses)
---

## 🛠 Getting Started

### Prerequisites
* [Python](https://www.python.org/downloads/): 3.11
* Operating System: Windows
* [optional] Download [iec-checker](https://github.com/jubnzv/iec-checker/releases/tag/v0.4) (static analysis of IEC 61131-3 programs)

###  Installation via PyPI
Run ``pip install plcrex`` to get PLCreX using PyPI

### Installation via GitHub
1. Download or clone PLCreX repository
2. Run ``install-windows.bat`` to automatically create a virtual environment (venv) and installation of dependencies
3. [optional] Run ``coverage run -m pytest ./tests/ --verbose`` for local tests
4. [optional] Run ``coverage report -m`` to check test results

         Name                                       Stmts   Miss  Cover   Missing
         ------------------------------------------------------------------------
         plcrex\__init__.py                             4      0   100%          
         plcrex\cli.py                                 73      1    99%   122    
         plcrex\tools\__init__.py                       0      0   100%          
         plcrex\tools\ds2ts\__init__.py                 0      0   100%          
         plcrex\tools\ds2ts\_ds2ts.py                   3      0   100%          
         plcrex\tools\fbd2ia\__init__.py                0      0   100%
         plcrex\tools\fbd2ia\_fbd2ia.py                 4      0   100%
         plcrex\tools\fbd-to-st\__init__.py             0      0   100%
         plcrex\tools\fbd-to-st\_fbd2st.py              4      0   100%
         plcrex\tools\iec_checker\__init__.py           0      0   100%
         plcrex\tools\iec_checker\_iec_checker.py       4      0   100%
         plcrex\tools\st2ast\__init__.py                0      0   100%
         plcrex\tools\st2ast\_st2ast.py                34      0   100%
         plcrex\tools\xmlval\__init__.py                0      0   100%
         plcrex\tools\xmlval\_xmlval.py                16      0   100%
         tests\__init__.py                              0      0   100%
         tests\test_ds2ts.py                           10      0   100%
         tests\test_fbd2st.py                          69      0   100%
         tests\test_fbd_io_checker.py                   7      0   100%
         tests\test_help.py                             6      0   100%
         tests\test_iec_checker.py                     32      0   100%
         tests\test_st2tree.py                         25      0   100%
         tests\test_version.py                         12      0   100%
         tests\test_xml_checker.py                     19      0   100%
         ------------------------------------------------------------------------
         TOTAL                                        322      1    99%

| ⚠ If no IEC Checker (.exe) is available, ``test_iec_checker.py`` will fail. |
|-----------------------------------------------------------------------------|

## 💻 Commands

Usage: ``python -m plcrex [OPTIONS] COMMAND [ARGS]``  

<img src="https://github.com/marwern/PLCreX/assets/92115516/fc3e338c-a4c1-4acf-b2e9-03fe2370da6a"  width="400">


<table>
<tr>
   <td><b>Usage</b></td>
   <td><b>OPTIONS</b></td>
   <td><b>COMMAND/ARGS</b></td>
</tr>
<tr>
   <td>
      python -m plcrex [OPTIONS] COMMAND</td>
   <td>
      -v,--version: show author and version<br>
      --help: show details<br><br>
   </td>
   <td>
      --fbd-to-st: call FBD-to-ST-Compiler<br>
	  --iec-checker: call iec-checker<br>
	  --impact-analysis: call FBD I/O impact analysis<br>
      --st-parser: call ST-Parser<br>
      --test-case-gen: call Test-Case-Generator<br>
      --xml-validator: call XML-Validator<br>
      
   </td>
</tr>
<tr>
    <td>python -m plcrex fbd-to-st [OPTIONS] SRC EXPORT</td>
   <td>
     --bwd: use backward translation<br>
     --formal: use formal parameter list<br>
     --st-parser: run ST parser with exports<br>
     --help: show details<br><br>
   </td>
   <td>
      SRC: source path<br>
      EXPORT: export directory path<br>
   </td>
</tr>
<tr>
    <td>
      python -m plcrex iec-checker [OPTIONS] SRC EXE</td>
    <td>
      --help_iec_checker: call iec-checker help <br>
      --help: show details<br><br>
    </td>
   <td>
      SRC: source path<br>
      EXE: iec-checker path (*.exe)
   </td>
</tr>
<tr>
    <td>
      python -m plcrex impact-analysis [OPTIONS] SRC EXPORT</td>
    <td>
		--help: show details<br><br>
    </td>
   <td>
      SRC: source path<br>
      EXPORT: export directory path<br>
   </td>
</tr>
<tr>
    <td>python -m plcrex st-parser [OPTIONS] SRC EXPORT</td>
    <td>
        --no-txt: no tree export as *.txt<br>
        --no-dot: no tree export as *.dot<br>
        --beckhoff: use Beckhoff TwinCAT ST grammar<br>
        --help: show details<br><br>
    </td>
   <td>
      SRC: source path<br>
      EXPORT: export directory path<br>
   </td>
</tr>
<tr>
    <td>
      python -m plcrex test-case-gen [OPTIONS] FORMULA</td>
    <td>
      --help: show details<br><br>
    </td>
   <td>
      FORMULA: formula in ST syntax<br>
   </td>
</tr>
<tr>
    <td>
      python -m plcrex xml-validator [OPTIONS] SRC</td>
    <td>
      --v201: use tc6_xml_v201.xsd<br>
      --help: show details<br><br>
    </td>
   <td>
      SRC: source path<br>
   </td>
</tr>

</table>


## ℹ️ Licenses
<table>
   <tr>
      <td>
         Description
      </td>
      <td>
         Version
      </td>
      <td>
         License
      </td>
   </tr>
   <tr>
      <td>
         PLCreX
      </td>
      <td>
         -
      </td>
      <td>
         GPLv3
      </td>
   </tr>
   <tr>
      <td>
         STgrammar_Beckhoff.lark <a href="https://github.com/klauer/blark">(🔗 Blark)</a>
      </td>
      <td>
         0.5.0
      </td>
      <td>
         GPLv2
      </td>
   </tr>
   <tr>
      <td>
         ds2ts_R1_2_0.cp311-win_amd64.pyd
      </td>
      <td>
         1.2.0
      </td>
      <td>
         -
      </td>
   </tr>
   <tr>
      <td>
         fbd2ia_R1_2_0.cp311-win_amd64.pyd
      </td>
      <td>
         1.2.0
      </td>
      <td>
         -
      </td>
   </tr>
   <tr>
      <td>
         fbd2st_R1_2_0.cp311-win_amd64.pyd
      </td>
      <td>
         1.2.0
      </td>
      <td>
         -
      </td>
   </tr>
</table>