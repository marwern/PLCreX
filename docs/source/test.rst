Test
=====

.. test:

Run the following command for some local tests:

.. code-block:: console

    (venv) C:\Python\plcrex_project>python -m pytest ./tests/

Run the following commands for some local tests and coverage report:

.. code-block:: console

    (venv) C:\Python\plcrex_project>coverage run -m pytest ./tests/
    (venv) C:\Python\plcrex_project>coverage report -m

Results:

.. code-block:: console

    Name                        Stmts   Miss  Cover   Missing
    ---------------------------------------------------------
    docs\source\__init__.py         0      0   100%
    docs\source\conf.py            22      0   100%
    plcrex\__init__.py              0      0   100%
    plcrex\_fbd2st.py             275      0   100%
    plcrex\_iec_checker.py         11      1    91%   33
    plcrex\_st2tree.py             14      0   100%
    plcrex\_xml_checker.py          7      0   100%
    plcrex\cli.py                  53      1    98%   91
    tests\__init__.py               0      0   100%
    tests\test_fbd2st.py           93      0   100%
    tests\test_help.py              6      0   100%
    tests\test_iec_checker.py      29      0   100%
    tests\test_st2tree.py          21      0   100%
    tests\test_version.py          12      0   100%
    tests\test_xml_checker.py      19      0   100%
    ---------------------------------------------------------
    TOTAL                         562      2    99%

.. warning::
    If no IEC Checker (.exe) is available, ``test_iec_checker.py`` will fail. The test must be excluded accordingly.
