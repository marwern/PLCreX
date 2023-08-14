PLCreX - Analysis of IEC 61131-3 Programmable Logic Controllers
===============================================================

<!-- -->
<!-- [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) -->
<!-- [![made-with-sphinx-doc](https://img.shields.io/badge/Made%20with-Sphinx-1f425f.svg)](https://www.sphinx-doc.org/) -->
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Windows](https://badgen.net/badge/icon/windows?icon=windows&label)](https://microsoft.com/windows/)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Tests](https://img.shields.io/badge/Tests-passed-<COLOR>.svg)](https://shields.io/)
[![Coverage](https://img.shields.io/badge/coverage-98%25-<COLOR>.svg)](https://shields.io/)
[![Documentation Status](https://readthedocs.org/projects/plcrex/badge/?version=latest)](https://plcrex.readthedocs.io/en/latest/?badge=latest)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

<br />
<div align="center">
  <img src="https://github.com/marwern/PLCreX/assets/92115516/3645a682-6bc8-45d1-aeb6-39cd7ded3b63" width=650> <!-- width=250 -->

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
    <a href="#license">License</a>
    ·
    <a href="#acknowledgments">Acknowledgments</a>
  </p>
</div>

---


Quick Start
===========
<strong><a href="https://plcrex.readthedocs.io/en">Explore the docs »</a></strong>

* Download IEC-Checker via IEC-Checker's GitHub releases [[.url](https://github.com/jubnzv/iec-checker/releases/tag/v0.4)]
* Install PLCreX via PyPI: ``pip install plcrex`` or
* Install PLCreX via PLCreX's GitHub repository: ``install-windows.bat``
     * [optional] Run local tests: ``coverage run -m pytest ./tests/ --verbose``
     * Activate virtual environment (venv): ``run.bat``

Key Features
============

<strong><a href="https://plcrex.readthedocs.io/en">Explore the docs »</a></strong>

Usage: ``(venv) C:\Tools\PLCreX>python -m plcrex --help``

<img src="https://github.com/marwern/PLCreX/assets/92115516/55946c88-a062-4e03-b1f1-5c2cea07d58e" width=650> <!-- width=250 -->

| Feature             | Usage                                                      | Version |
|---------------------|------------------------------------------------------------|---------|
| FBD-to-ST Compiler  | ``plcrex fbd-to-st [OPTIONS] SOURCE EXPORT FILENAME``| 1.3.0   |
| IEC-Checker         | ``plcrex iec-checker [OPTIONS] SOURCE EXE``                 | 0.4     |
| I/O-Impact Analysis | ``plcrex impact-analysis [OPTIONS] SOURCE EXPORT FILENAME`` | 1.3.1   |
| ST-Parser           | ``plcrex st-parser [OPTIONS] SOURCE EXPORT FILENAME``      | main    |
| Test-Case-Generator | ``plcrex test-case-gen [OPTIONS] FORMULA``| 2.0.0   |
| XML-Validator       | ``plcrex xml-validator [OPTIONS] SOURCE``| main    |

> **_NOTE:_**  Use the "--help" option to see feature details

License
=======
This project is licensed under the GPLv3 License - see the LICENSE file for details

Acknowledgments
===============
Inspiration, code snippets, etc.

* blark [[.url](https://github.com/klauer/blark/releases/tag/v0.5.0)]
* IEC-Checker [[.url](https://github.com/jubnzv/iec-checker/releases/tag/v0.4)]