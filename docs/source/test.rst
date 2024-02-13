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

    tests/test_fbd2st.py::test_help PASSED                                                   [  1%]
    tests/test_fbd2st.py::test_wrong_file PASSED                                             [  3%]
    tests/test_fbd2st.py::test_nobwd_noformal1 PASSED                                        [  4%]
    tests/test_fbd2st.py::test_nobwd_noformal2 PASSED                                        [  6%]
    tests/test_fbd2st.py::test_nobwd_noformal3 PASSED                                        [  7%]
    tests/test_fbd2st.py::test_nobwd_noformal4 PASSED                                        [  9%]
    tests/test_fbd2st.py::test_nobwd_formal1 PASSED                                          [ 10%]
    tests/test_fbd2st.py::test_nobwd_formal2 PASSED                                          [ 12%]
    tests/test_fbd2st.py::test_bwd_noformal1 PASSED                                          [ 14%]
    tests/test_fbd2st.py::test_bwd_noformal2 PASSED                                          [ 15%]
    tests/test_fbd2st.py::test_bwd_formal1 PASSED                                            [ 17%]
    tests/test_fbd2st.py::test_bwd_formal2 PASSED                                            [ 18%]
    tests/test_fbd2st.py::test_bwd_noformal_st2ast PASSED                                    [ 20%]
    tests/test_fbd2x.py::test_help1 PASSED                                                   [ 21%]
    tests/test_fbd2x.py::test_help2 PASSED                                                   [ 23%]
    tests/test_fbd2x.py::test_wrong_file1 PASSED                                             [ 25%]
    tests/test_fbd2x.py::test_wrong_file2 PASSED                                             [ 26%]
    tests/test_fbd2x.py::test_edge_opt1_st PASSED                                            [ 28%]
    tests/test_fbd2x.py::test_edge_opt1_sctx PASSED                                          [ 29%]
    tests/test_fbd2x.py::test_edge_opt2_st PASSED                                            [ 31%]
    tests/test_fbd2x.py::test_edge_opt2_sctx PASSED                                          [ 32%]
    tests/test_fbd2x.py::test_edge_opt3_st PASSED                                            [ 34%]
    tests/test_fbd2x.py::test_edge_opt3_sctx PASSED                                          [ 35%]
    tests/test_fbd2x.py::test_edge_opt4_st PASSED                                            [ 37%]
    tests/test_fbd2x.py::test_edge_opt4_sctx PASSED                                          [ 39%]
    tests/test_fbd2x.py::test_var_opt_st PASSED                                              [ 40%]
    tests/test_fbd2x.py::test_var_opt_sctx PASSED                                            [ 42%]
    tests/test_fbd2x.py::test_op_opt_st PASSED                                               [ 43%]
    tests/test_fbd2x.py::test_op_opt_sctx PASSED                                             [ 45%]
    tests/test_fbdia.py::test_help PASSED                                                    [ 46%]
    tests/test_fbdia.py::test_wrong_file PASSED                                              [ 48%]
    tests/test_fbdia.py::test_bwd_noformal_io_analysis PASSED                                [ 50%]
    tests/test_help.py::test_help PASSED                                                     [ 51%]
    tests/test_ieccheck.py::test_help PASSED                                                 [ 53%]
    tests/test_ieccheck.py::test_help_iec_checker PASSED                                     [ 54%]
    tests/test_ieccheck.py::test_verbose_st PASSED                                           [ 56%]
    tests/test_ieccheck.py::test_quiet_st PASSED                                             [ 57%]
    tests/test_ieccheck.py::test_wrong_file PASSED                                           [ 59%]
    tests/test_ieccheck.py::test_verbose_xml PASSED                                          [ 60%]
    tests/test_ieccheck.py::test_quiet_xml PASSED                                            [ 62%]
    tests/test_ieccheck.py::test_wrong_exe PASSED                                            [ 64%]
    tests/test_st2qrz.py::test_help1 PASSED                                                  [ 65%]
    tests/test_st2qrz.py::test_tc01_22 PASSED                                                [ 67%]
    tests/test_st2scl.py::test_help1 PASSED                                                  [ 68%]
    tests/test_st2scl.py::test_help2 PASSED                                                  [ 70%]
    tests/test_st2scl.py::test_tc01_22_scl PASSED                                            [ 71%]
    tests/test_st2scl.py::test_tc01_22_sctx PASSED                                           [ 73%]
    tests/test_stp.py::test_help PASSED                                                      [ 75%]
    tests/test_stp.py::test_dot_txt PASSED                                                   [ 76%]
    tests/test_stp.py::test_dot PASSED                                                       [ 78%]
    tests/test_stp.py::test_txt PASSED                                                       [ 79%]
    tests/test_stp.py::test_beckhoff_txt_dot PASSED                                          [ 81%]
    tests/test_stp.py::test_wrong_file PASSED                                                [ 82%]
    tests/test_tcgen.py::test_help PASSED                                                    [ 84%]
    tests/test_tcgen.py::test_ds2ts_001 PASSED                                               [ 85%]
    tests/test_tcgen.py::test_ds2ts_002 PASSED                                               [ 87%]
    tests/test_tcgen.py::test_ds2ts_003 PASSED                                               [ 89%]
    tests/test_tcgen.py::test_ds2ts_004 PASSED                                               [ 90%]
    tests/test_version.py::test_version_1 PASSED                                             [ 92%]
    tests/test_xmlval.py::test_help PASSED                                                   [ 93%]
    tests/test_xmlval.py::test_v201_passed PASSED                                            [ 95%]
    tests/test_xmlval.py::test_v201_failed PASSED                                            [ 96%]
    tests/test_xmlval.py::test_v10_failed PASSED                                             [ 98%]
    tests/test_xmlval.py::test_wrong_file PASSED                                             [100%]

    =============================== 64 passed in 151.38s (0:02:31) ================================


.. warning::
    IEC-Checker must be located in ``./bin/iec_checker_Windows_x86_64_v0.4.exe``. Otherwise ``test_iec_checker.py`` will fail.
    Also, NuSMV must be located in ``./bin/NuSMV.exe``. Otherwise ``test_st2x.py`` will fail.
    In addition, kicodia must be placed in ``./bin/kicodia-win.bat``. Otherwise ``test_st2scl.py`` will fail.

