PLCopen XML Validator
=====

.. xml_checker:

The `PLCopen <https://plcopen.org/technical-activities/xml-exchange>`_ XML Validator validates on
basis of ``tc6_xml_v201.xsd`` and ``tc6_xml_v10.xsd`` whether the PLCopen XML exchange format meets the
PLCopen specification. Print help of PLCopen XML Validator with ``COMMAND`` ``xml-checker`` and
``[OPTIONS]`` ``--help`` to see all features and usage:

.. code-block:: console

    (venv) C:\Python\plcrex_project>python -m plcrex xml-checker --help

    Usage: plcrex xml-checker [OPTIONS] SRC

    Arguments:
      SRC  [required]

    Options:
      --v201 / --no-v201  use tc6_xml_v201.xsd  [default: False]
      --help              Show this message and exit.


.. xml_passed:

Example (passed): TC001.xml
----
Command and Result:

.. code-block:: console

    (venv) C:\Python\plcrex_project>python -m plcrex xml-checker --v201 ".\tests\plcopen_examples\TC001.xml"

    Success!

.. xml_failed:

Example (failed): TC001_failed.xml
----
Command and Result:

.. code-block:: console

    (venv) C:\Python\plcrex_project>python -m plcrex xml-checker --v201 ".\tests\plcopen_examples\TC001_failed.xml"

    Traceback (most recent call last):
    ...
    xmlschema.validators.exceptions.XMLSchemaDecodeError: failed validating '2022-09-01 22:53:16' with XsdAtomicBuiltin(name='xs:dateTime'):
    Reason: attribute modificationDateTime='2022-09-01 22:53:16': Invalid datetime string '2022-09-01 22:53:16' for <class 'elementpath.datatypes.datetime.DateTime10'>

    Schema:
      <xs:simpleType xmlns:hfp="http://www.w3.org/2001/XMLSchema-hasFacetAndProperty" xmlns:xs="http://www.w3.org/2001/XMLSchema" name="dateTime" id="dateTime">
            ...
