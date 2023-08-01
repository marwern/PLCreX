🛠 Getting Started
=====

.. setup:

Prerequisites
----

* `Python <https://www.python.org/downloads/>`_ v3.11
* Operating System: Windows
* [optional] Download `iec-checker <https://github.com/jubnzv/iec-checker/releases/tag/v0.4/>`_ (static analysis of IEC 61131-3 programs)

Installation via PyPI
----
Run ``pip install plcrex`` to get PLCreX using `PyPI <https://pypi.org/project/plcrex//>`_

Installation via Github
----
1. Download or clone `PLCreX <https://github.com/marwern/PLCreX>`_ GitHub repository
2. Run ``install-windows.bat`` to automatically create a virtual environment (venv) and installation of dependencies
3. [optional] Run ``coverage run -m pytest ./tests/ --verbose`` for local tests
4. [optional] Run ``coverage report -m`` to check test results

.. warning::
    If no IEC Checker (.exe) is available, ``test_iec_checker.py`` will fail.