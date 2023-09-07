Installation
============

.. install:

Prerequisites
-------------

* Python v3.11 [`.url <https://www.python.org/downloads/>`_]
* Operating System: Windows

PLCreX Installation via PyPI
----------------------------
Run the following command to get the latest PLCreX from PyPI.org [`.url <https://pypi.org/project/plcrex/>`_]

.. code:: console

    pip install plcrex

PLCreX Installation via GitHub
------------------------------
1. Download or clone PLCreX's GitHub repository [`.url <https://github.com/marwern/PLCreX>`_]
2. Run the following batch script to automatically create a virtual environment (venv) and install dependencies

.. code:: console

    install-windows.bat

External tools called by PLCreX
-------------------------------
1. IEC-Checker - Static analysis of IEC 61131-3 programs
    - Download v0.4 via GitHub [`.url <https://github.com/jubnzv/iec-checker/releases/tag/v0.4/>`_]
2. NuSMV - Symbolic Model Checker
    - Download v2.6.0 via NuSMV's homepage [`.url <https://nusmv.fbk.eu//>`_]