XML-Validator
=============

.. xml_validator:

The PLCopen XML-Validator feature uses ``tc6_xml_v201.xsd`` and ``tc6_xml_v10.xsd`` to validate that the PLCopen XML exchange format conforms to the PLCopen specification [`.url <https://plcopen.org/technical-activities/xml-exchange>`_].


**Usage**

.. code-block:: console

    python -m plcrex xml-validator --help

.. code:: console

         Usage: plcrex xml-validator [OPTIONS] SOURCE

         XML-Validator                           *.xml → stdout

        ╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────╮
        │ *    source      PATH  source path [default: None] [required]                                │
        ╰──────────────────────────────────────────────────────────────────────────────────────────────╯
        ╭─ Options ────────────────────────────────────────────────────────────────────────────────────╮
        │ --v201    --no-v201      use tc6_xml_v201.xsd [default: no-v201]                             │
        │ --help                   Show this message and exit.                                         │
        ╰──────────────────────────────────────────────────────────────────────────────────────────────╯


..
    .. figure:: ../fig/xml_validator_demo.png
        :align: center
        :width: 600px

|

Example 1: ``--v201`` (PASSED)
------------------------------

**Command**

.. code-block:: console

    python -m plcrex xml-validator --v201 ".\tests\plcopen_examples\TC001.xml"


**Results**

.. code-block:: console

    Success!


Example 2: ``--v201`` (FAILED)
------------------------------

**Command**

.. code-block:: console

    python -m plcrex xml-validator --v201 ".\tests\plcopen_examples\TC001_failed.xml"


**Results**

.. code-block:: console

    ...
    XMLSchemaDecodeError: failed validating '2022-09-01 14:53:16' with
    XsdAtomicBuiltin(name='xs:dateTime'):

    Reason: attribute modificationDateTime='2022-09-01 14:53:16': Invalid datetime string '2022-09-01
    14:53:16' for <class 'elementpath.datatypes.datetime.DateTime10'>

    Schema:

      <xs:simpleType xmlns:hfp="http://www.w3.org/2001/XMLSchema-hasFacetAndProperty"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" name="dateTime" id="dateTime">
        <xs:annotation>
        <xs:appinfo>
            <hfp:hasFacet name="pattern" />
    ...