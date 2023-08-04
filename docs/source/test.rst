Test
====

.. test:

If PLCreX has been installed via GitHub, tests can be performed locally.

1. Run the following command for local tests

.. code:: console

    >coverage run -m pytest ./tests/ --verbose

2. Run the following command to check test results

.. code:: console

    >coverage report -m

.. warning::
    IEC Checker must be stored in ``./bin/iec_checker_Windows_x86_64_v0.4.exe``. Otherwise, ``test_iec_checker.py`` will fail.