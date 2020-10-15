import zipfile
from typing import BinaryIO
from cassis import Cas, load_typesystem, load_cas_from_xmi


def load_cas_from_zip_file(f: BinaryIO) -> Cas:
    archive = zipfile.ZipFile(f)

    # Type system
    type_system_file = list(filter(
        lambda f: f.filename.endswith('.xml'),
        archive.infolist()))[0]
    with archive.open(type_system_file, 'r') as f:
        type_system = load_typesystem(f)

    # Xmi
    xmi_file = list(filter(
        lambda f: f.filename.endswith('.xmi'),
        archive.infolist()))[0]
    with archive.open(xmi_file, 'r') as f:
        cas = load_cas_from_xmi(f, typesystem=type_system)

    return cas

