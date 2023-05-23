Setup
=====

.. setup:

1. Download or clone `PLCreX <https://github.com/marwern/PLCreX>`_ repository
2. Install `Python <https://www.python.org/downloads/>`_ (version 3.10 needed)
3. Download IEC-Checker (.exe) from last `PLCreX Release <https://github.com/marwern/PLCreX/tags>`_ or official `IEC Checker repository <https://github.com/jubnzv/iec-checker>`_ and change ``IEC_Checker_exe`` path in ``./config.ini`` according to your local path

    .. code-block:: console

        [IEC-Checker]
        IEC_Checker_exe = .\bin\iec_checker_Windows_x86_64_v0.4.exe

3. Create a virtual environment in the project root directory:

    .. code-block:: console

        C:\Python\plcrex_project>python -m venv venv

4. Activate virtual environment:

   .. code-block:: console

        C:\Python\plcrex_project>venv\Scripts\activate.bat

5. Install the dependencies (``requirements.txt``):

   .. code-block:: console

        (venv) C:\Python\plcrex_project>python -m pip install -r requirements.txt

.. note::
    Run ``install.bat`` to automatically create a virtual environment and install the dependencies.

.. warning::
    If no IEC Checker (.exe) is available, ``test_iec_checker.py`` will fail.
