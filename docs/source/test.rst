Test
====

.. test:

1. Run the following command for local tests

.. code:: console

    coverage run -m pytest ./tests/ --verbose

2. Run the following command to check test results

.. code:: console

    coverage report -m

.. code:: console

         Name                                       Stmts   Miss  Cover   Missing
         ------------------------------------------------------------------------
         plcrex\__init__.py                             4      0   100%
         plcrex\cli.py                                 89      1    99%   161
         plcrex\tools\__init__.py                       0      0   100%
         plcrex\tools\ds2ts\__init__.py                 0      0   100%
         plcrex\tools\ds2ts\_ds2ts.py                   3      0   100%
         plcrex\tools\fbd2ia\__init__.py                0      0   100%
         plcrex\tools\fbd2ia\_fbd2ia.py                 4      0   100%
         plcrex\tools\fbd2st\__init__.py                0      0   100%
         plcrex\tools\fbd2st\_fbd2st.py                 4      0   100%
         plcrex\tools\iec_checker\__init__.py           0      0   100%
         plcrex\tools\iec_checker\_iec_checker.py       4      0   100%
         plcrex\tools\st2ast\__init__.py                0      0   100%
         plcrex\tools\st2ast\_st2ast.py                32      4    88%   53-56
         plcrex\tools\xmlval\__init__.py                0      0   100%
         plcrex\tools\xmlval\_xmlval.py                21      2    90%   43-44
         tests\__init__.py                              0      0   100%
         tests\test_ds2ts.py                           10      0   100%
         tests\test_fbd2st.py                          56      0   100%
         tests\test_fbd_io_checker.py                  13      0   100%
         tests\test_help.py                             6      0   100%
         tests\test_iec_checker.py                     32      0   100%
         tests\test_st2tree.py                         25      0   100%
         tests\test_version.py                         12      0   100%
         tests\test_xml_checker.py                     19      0   100%
         ------------------------------------------------------------------------
         TOTAL                                        334      7    98%


.. warning::
    IEC Checker must be stored in ``./bin/iec_checker_Windows_x86_64_v0.4.exe``. Otherwise, ``test_iec_checker.py`` will fail.