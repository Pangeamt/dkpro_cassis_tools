import copy
import re
from dkpro_cassis_tools.ns import SENTENCE_NS
from cassis import Cas


def restore_cas_segmentation_by_newline(cas: Cas) -> Cas:
    cas = copy.deepcopy(cas)

    # Remove sentence annotation
    for sentence in list(cas.select(SENTENCE_NS)):
        cas.remove_annotation(sentence)

    # Create new sentence annotations
    for sofa in cas.sofas:
        idx = 0
        separator = re.compile('((?:\r?)\n)')
        for item in re.compile(separator).split(sofa.sofaString):
            start = idx
            if re.match(separator, item):
                idx += len(item)
            elif len(item):
                idx += len(item)
                annotation = cas.typesystem.get_type(SENTENCE_NS)(begin=start, end=idx, sofa=sofa.sofaNum)
                cas.add_annotation(annotation)
    return cas

