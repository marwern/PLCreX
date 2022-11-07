Usage
=====

.. setup:
Setup
------------

1. Download or clone PLCreX repository
2. Download IEC-Checker (.exe) from last `PLCreX Release <https://github.com/marwern/PLCreX/tags>`_ or official `IEC Checker repository <https://github.com/jubnzv/iec-checker>`_
3. Change ``IEC_Checker_exe`` path in ``./config.ini`` according to your local path

.. code-block:: console

    [IEC-Checker]
    IEC_Checker_exe = .\bin\iec_checker_Windows_x86_64_v0.4.exe
	
4. Create a virtual environment in the project root directory:

.. code-block:: bash

    C:\Python\plcrex_project>python -m venv venv
	
5. Activate virtual environment:

.. code-block:: bash

    C:\Python\plcrex_project>venv\Scripts\activate.bat
	
6. Install the dependencies (``requirements.txt``):

.. code-block:: bash

    (venv) C:\Python\plcrex_project>python -m pip install -r requirements.txt

.. note::
	Step 2 and 3 are optional, but the tests and some of the PLCreX features will not work without IEC Checker.
   

.. test:
Test
----------------

Run the following command for some local tests:

.. code-block:: bash

	(venv) C:\Python\plcrex_project>python -m pytest ./tests/

Run the following commands for some local tests and coverage report:

.. code-block:: bash

	(venv) C:\Python\plcrex_project>coverage run -m pytest ./tests/
	(venv) C:\Python\plcrex_project>coverage report -m

.. code-block:: console

	Name                        Stmts   Miss  Cover   Missing
	---------------------------------------------------------
	plcrex\__init__.py              2      0   100%
	plcrex\_fbd2st.py             261      0   100%
	plcrex\_iec_checker.py         11      1    91%   33
	plcrex\_st2tree.py             14      0   100%
	plcrex\_xml_checker.py          7      0   100%
	plcrex\cli.py                  54      1    98%   93
	tests\__init__.py               0      0   100%
	tests\test_fbd2st.py           41      0   100%
	tests\test_help.py              6      0   100%
	tests\test_iec_checker.py      33      0   100%
	tests\test_st2tree.py          21      0   100%
	tests\test_version.py          11      0   100%
	tests\test_xml_checker.py      19      0   100%
	---------------------------------------------------------
	TOTAL                         480      2    99%
