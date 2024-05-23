# SeqBox
seq process tools box

## install

### pip

```
pip install SeqBox
```

## Attributes

- `name`: sequence name, If not defined, the default is 'name'

- `seq`: base sequence

- `stype`: 'DNA' or 'RNA'

- `dict_base`:  The principle of complementary base pairing of DNA and RNA. 
    - `dict_base_DNA` = {"A":"T", "C":"G", "T":"A", "G":"C", "a":"t", "c":"g", "t":"a", "g":"c"}; 
    - `dict_base_RNA` = {"A":"U", "C":"G", "U":"A", "G":"C", "a":"u", "c":"g", "u":"a", "g":"c"}

more info: the three parameters are all optional and can be defined later when using the function.

## functions

- [generator](./generator.md): sequence generator
    - [`random`](./generator.md#random)：randomly generated sequence, possible repetitions.
    - [`norepeat`](./generator.md#norepeat)：randomly generate non-repeating sequences.
    - [`distance`](./generator.md#distance)：randomly generate sequences with [edit distances](https://github.com/ztane/python-Levenshtein) between sequences greater than a fixed value.
- [variation](./variation.md)：random transformation of sequences, including deletions, additions and mutations.