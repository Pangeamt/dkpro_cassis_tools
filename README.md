# Dkpro cassis tools

Toolkit for managing uima cas xmi files. 

## Install

```BASH
pip install dkpro-cassis-tools
```

## Load cas from a zip file
```python
from dkpro_cassis_tools import load_cas_from_zip_file
with open('cas.zip', 'rb') as f:
    cas = load_cas_from_zip_file(f)
```

## Save cas to a zip file
```python
from dkpro_cassis_tools import dump_cas_to_zip_file


with open('cas.zip', 'rb') as f:
    dump_cas_to_zip_file(cas, f)
```

## Restore cas segmentation by newline
```python
from dkpro_cassis_tools import load_cas_from_zip_file
from dkpro_cassis_tools import restore_cas_segmentation_by_newline
from dkpro_cassis_tools import dump_cas_to_zip_file


# Open the cas
with open('cas.zip', 'rb') as f:
    cas = load_cas_from_zip_file(f)

# Restore segmentation  
re_segmented_cas = restore_cas_segmentation_by_newline(cas)

# Save it
with open('re_segmented_cas.zip', 'rb') as f:
    dump_cas_to_zip_file(cas, f)    
```

## Combine sentences from one or more cas
```python
from dkpro_cassis_tools import load_cas_from_zip_file
from dkpro_cassis_tools import dump_cas_to_zip_file
from dkpro_cassis_tools import create_cas_from_sentences
from dkpro_cassis_tools import SENTENCE_NS


sentences = []

# Extract some sentences from cas1 
with open('cas1.zip', 'rb') as f:
    cas1 = load_cas_from_zip_file(f)
for sentence in cas1.select(SENTENCE_NS):
    if len(sentence.get_covered_text())>10:
        sentences.append((cas1, sentence))

# Extract some sentences from cas2 
with open('cas2.zip', 'rb') as f:
    cas2 = load_cas_from_zip_file(f)
for sentence in cas2.select(SENTENCE_NS):
    if len(sentence.get_covered_text())>10:
        sentences.append((cas2, sentence))

# Create the new cas
new_cas = create_cas_from_sentences(sentences) 

# Save it
with open('new_cas.zip', 'rb') as f:
    dump_cas_to_zip_file(new_cas, f)
```

## Tokenize cas
```python
from dkpro_cassis_tools import load_cas_from_zip_file
from dkpro_cassis_tools import tokenize_cas


wakati = MeCab.Tagger("-Owakati")

def tokenize(text: str) -> List[str]:
    return wakati.parse(text).split()

with open('data/cas_tokenize.zip', 'rb') as f:
    cas = load_cas_from_zip_file(f)
    mecab_tokenized_cas = tokenize_cas(cas, tokenize)


```

