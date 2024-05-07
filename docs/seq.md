# seq

## API

### Attributes

- `seq`: base sequence

- `stype`: 'DNA' or 'RNA'

- `dict_base`:  The principle of complementary base pairing of DNA and RNA. `dict_base_DNA` = {"A":"T", "C":"G", "T":"A", "G":"C", "a":"t", "c":"g", "t":"a", "g":"c"}; `dict_base_RNA` = {"A":"U", "C":"G", "U":"A", "G":"C", "a":"u", "c":"g", "u":"a", "g":"c"}

more info: the three parameters are all optional and can be defined later when using the function.

### functions

#### reverse_complement

```python

from seqtools import SEQ

seq = SEQ()
seq.name
# 
sequence = "ATCGGTACCGATTACG"
stype = "DNA"

seq.reverse_complement(seq=sequence, stype=stype)
# ''

seq.stype
#
seq.dict_base
#
```