Setup
=====

.. setup:


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

