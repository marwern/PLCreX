Equivalence Class / Test Case Generator
=====

.. test_case_gen:

The FBD-to-ST Transpiler translates FBDs stored in PLCopen XML format into ST POUs.
The user can additionally run a static code analysis with IEC Checker. Print help of
FBD-to-ST Transpiler with ``COMMAND`` ``test-case-gen`` and
``[OPTIONS]`` ``--help`` to see all features and usage:

.. code-block:: console

    (venv) C:\Python\plcrex_project>python -m plcrex test-case-gen --help
    Usage: PLCreX test-case-gen [OPTIONS] FORMULA

    Arguments:
      FORMULA  [required]

    Options:
      --help  Show this message and exit.

The Equivalence and Test Case Generator feature is designed to streamline the software testing process.
By utilizing the powerful SMT theorem prover, Z3, this feature automatically generates possible equivalence classes and test cases based on a given input string.
There are two main features: (1) Automatic Equivalence Class Generation: The tool efficiently identifies and creates equivalence classes derived from the input string, allowing for a more thorough and systematic testing approach.
(2) Test Case Creation: Utilizing the Z3 SMT theorem prover, the generator swiftly constructs test cases for each identified equivalence class, ensuring a wide range of scenarios are covered during testing.


.. tc_example_1:

Example: "x1 & x2"
----

.. code-block:: console

    (venv) C:\Python\plcrex_project>python -m plcrex test-case-gen "x1 & x2"
    --------------------------------------------------
    -- PLCreX's SMT-based Test Case Generator --

    Author: Marcel Werner
    Version: 1.0

    Script started at 00:15:21 on 2023-04-10
    --------------------------------------------------

    Original formula:
    ==================================
    x1&x2

    (Abstract) Syntax Tree:
    ==================================
    start
      and
        variable    x1
        variable    x2


    SMT formula (s-expression notation):
    ==================================
    (and x1 x2)

    Number of Equivalence Classes / Test Cases:
    ==================================
    1

    Equivalence Classes (s-expression notation):
    ==================================
    1: (and x2 x1)

    Test Cases:
    ==================================
    1: x2 = True, x1 = True

    SMT Proof (must be unsat):
    ==================================
    unsat

    --- 0.959 seconds ---


.. tc_example_2:

Example: "(A & B) | (C == (D & E))"
----

.. code-block:: console

    (venv) C:\Python\plcrex_project>python -m plcrex test-case-gen "(A & B) | (C == (D & E))"
    --------------------------------------------------
    -- PLCreX's SMT-based Test Case Generator --

    Author: Marcel Werner
    Version: 1.0

    Script started at 00:16:55 on 2023-04-10
    --------------------------------------------------

    Original formula:
    ==================================
    (A & B) | (C == (D & E))

    (Abstract) Syntax Tree:
    ==================================
    start
      or
        and
          variable  A
          variable  B
        equality
          variable  C
          and
            variable        D
            variable        E


    SMT formula (s-expression notation):
    ==================================
    (or (and A B) (= C (and D E)))

    Number of Equivalence Classes / Test Cases:
    ==================================
    11

    Equivalence Classes (s-expression notation):
    ==================================
    1: (and A (not D) B C (not E))
    2: (and (not B) (not E) (not C))
    3: (and (not D) E (not C))
    4: (and (not A) B (not E) (not C))
    5: (and A B (not E) (not C))
    6: (and D B E C)
    7: (and D (not A) (not B) E C)
    8: (and D A (not B) E C)
    9: (and D A B E (not C))
    10: (and D A B (not E) C)
    11: (and (not D) A B E C)

    Test Cases:
    ==================================
    1: A = True, D = False, B = True, C = True, E = False
    2: B = False, E = False, C = False
    3: D = False, E = True, C = False
    4: A = False, B = True, E = False, C = False
    5: A = True, B = True, E = False, C = False
    6: D = True, B = True, E = True, C = True
    7: D = True, A = False, B = False, E = True, C = True
    8: D = True, A = True, B = False, E = True, C = True
    9: D = True, A = True, B = True, E = True, C = False
    10: D = True, A = True, B = True, E = False, C = True
    11: D = False, A = True, B = True, E = True, C = True

    SMT Proof (must be unsat):
    ==================================
    unsat

    --- 2.983 seconds ---