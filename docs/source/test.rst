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

        Name                                                 Stmts   Miss  Cover   Missing
        ----------------------------------------------------------------------------------
        plcrex\__init__.py                                       4      0   100%
        plcrex\add.py                                           37      0   100%
        plcrex\cli.py                                           59      0   100%
        plcrex\tools\__init__.py                                 0      0   100%
        plcrex\tools\ds2ts\__init__.py                           0      0   100%
        plcrex\tools\ds2ts\_ds2ts.py                            12      0   100%
        plcrex\tools\fbd2st\__init__.py                          0      0   100%
        plcrex\tools\fbd2st\_fbd2st.py                          13      0   100%
        plcrex\tools\iec_checker\__init__.py                     0      0   100%
        plcrex\tools\iec_checker\_iec_checker.py                25      0   100%
        plcrex\tools\iec_checker\tag\iec_checker_R1_2_0.py       8      0   100%
        plcrex\tools\st2ast\__init__.py                          0      0   100%
        plcrex\tools\st2ast\_st2ast.py                          12      0   100%
        plcrex\tools\st2ast\tag\st2ast_R1_2_0.py                20      0   100%
        plcrex\tools\st2ia\__init__.py                           0      0   100%
        plcrex\tools\st2ia\_st2ia.py                            15      0   100%
        plcrex\tools\st2x\__init__.py                            0      0   100%
        plcrex\tools\st2x\_st2x.py                              15      0   100%
        plcrex\tools\xml_val\__init__.py                         0      0   100%
        plcrex\tools\xml_val\_xml_val.py                        12      0   100%
        plcrex\tools\xml_val\tag\xml_val_R1_2_0.py              11      0   100%
        tests\__init__.py                                        0      0   100%
        tests\test_ds2ts.py                                     10      0   100%
        tests\test_fbd2st.py                                    56      0   100%
        tests\test_help.py                                       6      0   100%
        tests\test_iec_checker.py                               32      0   100%
        tests\test_st2ast.py                                    25      0   100%
        tests\test_st2ia.py                                     13      0   100%
        tests\test_st2x.py                                      45      0   100%
        tests\test_version.py                                    8      0   100%
        tests\test_xml_val.py                                   19      0   100%
        ----------------------------------------------------------------------------------
        TOTAL                                                  457      0   100%


.. warning::
    IEC-Checker must be stored in ``./bin/iec_checker_Windows_x86_64_v0.4.exe``. Otherwise, ``test_iec_checker.py`` will fail. NuSMV must be stored in ``./bin/NuSMV.exe``. Otherwise, ``test_st2x.py`` will fail.

