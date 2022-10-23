from pathlib import Path
import xmlschema

def validate(xml_file: Path, validation_file:str):
    xsd_file = fr".\data\{validation_file}"

    # create validation scheme
    scheme = xmlschema.XMLSchema(xsd_file)

    # validate PLCopen xml file
    scheme.validate(xml_file)
    return