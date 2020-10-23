import copy
from typing import Callable, List
from dkpro_cassis_tools.ns import SENTENCE_NS, TOKEN_NS
from cassis import Cas
import tokenizations


def tokenize_cas(cas: Cas, tokenize_fn: Callable[[str], List[str]]) -> Cas:
    cas = copy.deepcopy(cas)

    # Remove tokens
    for token in list(cas.select(TOKEN_NS)):
        cas.remove_annotation(token)

    # Create new tokens
    for sentence in cas.select(SENTENCE_NS):
        text = sentence.get_covered_text()
        tokens = tokenize_fn(text)
        spans = tokenizations.get_original_spans(tokens, text)
        for begin, end in spans:
            annotation = cas.typesystem.get_type(TOKEN_NS)(
                begin=begin + sentence.begin,
                end=end + sentence.begin)
            cas.add_annotation(annotation)
    return cas

