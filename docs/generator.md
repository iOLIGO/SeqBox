
## generator

sequence generator

### usage
<details>
    <summary>SeqTools generator</summary>

    usage: SeqTools generator [-h] [-out OUT] [-od OUT_DIR]
                          [-gt {random,norepeat,distance}] [-gn GNUMBER]
                          [-gts GTIMES] [-gc GCHAR] [-gd GDISTANCE] [-gl GLEN]

    optional arguments:
    -h, --help            show this help message and exit
    -out OUT, --out_file OUT
                            sequence out file with TSV format
    -od OUT_DIR, --out_dir OUT_DIR
                            out direction
    -gt {random,norepeat,distance}, --gtype {random,norepeat,distance}
    -gn GNUMBER, --gnumber GNUMBER
                            sequence number
    -gts GTIMES, --gtimes GTIMES
                            Number of runs
    -gc GCHAR, --gchar GCHAR
                            generator charset, like: ATCG
    -gd GDISTANCE, --gdistance GDISTANCE
                            distance
    -gl GLEN, --glen GLEN
                            generator sequence length
</details>


### random

Randomly generated sequence, possible repetitions.

#### API

```python
from seqtools import SEQ
seq = SEQ(name="test")
seq.name
# 'test'
Grandom = seq.Gseq_random(seq_len=35)
n = 0
while n <= 10:
    seq = next(Grandom)
    print(seq)
    n = n + 1
#2024-05-21 15:16:40.176 | WARNING  | seqtools.seq:Gseq_random:150 - not found params char_set, use 'ATCG' with default
#CATCGTGCATAACTCGGTAGACAGGCAAGGCAACG
#CACTCGGTCTTGCCATGTGTCCTGTAGGTGACTAA
#AGGAACCCCCGTAGTAGCCCGACAGCAAGGTTCAT
#AGTGTGGATAAAAGAGCACCCACAGAGGACCAAAA
#CAAAACGTATGGCACGCTAACCATTTTCTAAACCG
#GATTTAAGCACAAGACCCTTGTTGGAAAGCAATTC
#AGGTCAACGGGCATTTAGTTCAGTTCCAGTGACCC
#ATGACAGGGAGTGTCATCTGAAAGTGCCAACGGGG
#TAGACTCACTATTATGCCTTCCATTCTCGGAGGTG
#CCTCACCGTTTCGCGGAACGTTTCAACCAAACTAA
#TGAGGGTCTACGATAGCTGTCAAGGAAGACCACTT

seq = SEQ(name="test")
Grandom_RNA = seq.Gseq_random(seq_len=35, char_set="AUCG")
n = 0
while n <= 10:
    seq = next(Grandom_RNA)
    print(seq)
    n = n + 1
#UGAGGACGAGGGCGGUGAUAGGCAUUUUAAUUUGG
#UUGUUUAUCUAGUCCUCCAGCCUCGGAACCGGAAC
#GCUACAUUGUCUGCGGGUUUGACAACGACACGGAU
#CACUGAAGGCUGUUCCCUACUGACUUCGAGGCGCA
#CGAGACUCUUGAAUGUAUAAAAGGUAAGAUAUAUC
#GCCUUUUUUCGGGAGUUACUUCGAGUUGUUCAAUC
#AAGUGUUCCGACCUGAUCCUGCCUCCUGAUCACGU
#GGGGUGGAUUCUGGUAUAGGUGAGGCUAAUCAGUU
#CCUAGCACGACCAAGUUCAAUAGAACGAUCAGAGG
#CGAAUGUACGAGAUCGUCAGGCGGGCCGAUGUUGG
#AUCUGACCUAGGCCUUGGGAGGGUACCCACAAAAG
```

#### CLI

The main parameters include the length(`-gl` or `--glen`) and number(`-gn` or `-gnumber`) of generated sequences.

```shell

SeqTools generator -gt random -gn 100 -gl 35 -out test_random

```
<details>
    <summary>output: test_random.tsv</summary>

    #generator_random:seq_len:35;char_set:ATCG
    GGTCCGACCTCATCTGGATGCTCCAATGTGGGCTG
    AGGCATATGGATCGCCGACACCCGTGCTACAGTTA
    TCAAGCGCGAACCGGGTACCTGCCGAAACCGTATA
    AACAGTGTTGCGCAGTGCCTGCACTTAAACAAATC
    GATATAGGGTCTCGTTAGTACGACGATTTCGCGAG
    CCCACAGGTCGCAGACTCCGCTGTTGCTTGAAGGC
    CGTTAAAGCTCAATCATCAACCCGATACGTTGTCT
    GAGAGCCTAGAACAAGGTACACCGAAGACGAGACG
    GCGCGGCTGTCCTTAGATATAGGTAGCAATACTGA
    ...
    CGTACTGATCAAATAACCCCGCAGACGGGTAATGC
</details>

### norepeat

randomly generate non-repeating sequences.

#### API

```python

from seqtools import SEQ
seq = SEQ(name="test")
seq.name
#'test'
Gnorepeat = seq.Gseq_norepeat(seq_len=35)
n = 0
while n <= 10:
    seq = next(Gnorepeat)
    print(seq)
    n = n + 1
#2024-05-21 16:08:06.289 | WARNING  | seqtools.seq:Gseq_norepeat:177 - not found params char_set, use 'ATCG' with default
#GGTTGTAACAGCGATAACACGGTTTAACGGACCAG
#GTTAACTCTAACATATACCTCCTTTCTTCGCCACA
#GCGTCGGATATAGAAGCTTGCGCCCTAATGTTATA
#AATGCCTTGCTCGATTCAATTAGCTCCCAAACTTT
#TTGAGAGAGGTCCTGTCGTTCTTATCCTTTCCTAA
#CGTAACATATAGGATACTTACACGCAGGAGAGTAT
#CCCACCCTACGCATCCGCCGTCGGTCTGTCGCTAT
#AACGCGATGTCTAGAAGACCATGTTTCACCTAACT
#CGGCGGTGGTTATGGGATATGGGGCTCTGAGTGAG
#GTGCAGCCACGTGAATTTACGTCCTTCGCCGATCC
#CGGCAAATACTCTTGGATAGAGATTAGCAGCGAGC

seq = SEQ(name="test")
Gnorepeat_RNA = seq.Gseq_random(seq_len=35, char_set="AUCG")
n = 0
while n <= 10:
    seq = next(Gnorepeat_RNA)
    print(seq)
    n = n + 1
#CGUCUUAAUUAAACCUCGAAUUGGGAGUUGGCUUG
#CCCAAUCUUCCACUUCUAUAGCGGUAACAUUAAAU
#UCACAUGCAACUCCACGGAACCAAUUAAACCAGGA
#GUGGAAAACCACUUCCAGACUGUAAAGCCAAUGGU
#CUGGACCUACGAUCGCAAAGAUAUAGCUCCUGUAG
#GAGUUUGGCUAGCAGUAUGAGGAGAUUGCAAAUCU
#UCGCUCACGGCGAAACAAUUCUGUAUUUGAGAAGG
#UUAUUCACGAUAUCGGCGGACAGCGAAGGAGUUAU
#AGGACCCUACAUGACGCACAGAGACCAGGUAUCGG
#AGUGUGGGCGUCUCCCGAAACGAAUCGCAUUGUUC
#UUCGUACCGAAGGUUUAGUGGAAUAGGUGGAGAGU
```

#### CLI

The main parameters include the length(`-gl` or `--glen`) and number(`-gn` or `-gnumber`) of generated sequences.

```shell

SeqTools generator -gt norepeat -gn 100 -gl 35 -out test_norepeat

```

<details>
    <summary>output: test_norepeat.tsv</summary>

    #generator_norepeat:seq_len:35;char_set:ATCG
    ACTAGATTTTGATTTGGTCCGGAGTTAGAGATCGT
    GGGATCGAAAGGGGTCGCCTCTCTTGAGAGCATTG
    GCTATTTATTCAAATAGACTATATACAACAGTACA
    GGACCTGTAGCGGCGTAGAATGTGCTGTGATACGA
    CCTTGGACAGTGGGGTATAACCTATGGTGTGAGTA
    TCACCTTTATTCAGGCGTATCTACGGTACTATCAA
    GTAGGGTTTCTACCGTTTGAGCATGTAGATGCCAT
    GCTTAAGTGATGTAAGGTGGCTTACCATCATCGAA
    ...
    CATACCACGTAACAACCCGTAGGTTCGCGTTAGGT
</details>


### distance

randomly generate sequences with [edit distances](https://github.com/ztane/python-Levenshtein) between sequences greater than a fixed value.

#### API

```python

from seqtools import SEQ
seq = SEQ(name="test")
seq.name
#'test'
Gdistance = seq.Gseq_distance(seq_len=35, distance=5)
n = 0
while n <= 10:
    seq = next(Gdistance)
    print(seq)
    n = n + 1
#2024-05-21 16:13:45.385 | WARNING  | seqtools.seq:Gseq_random:150 - not found params char_set, use 'ATCG' with default
#CCGAGATAAGATACCGCCGCGGGCAACAGCAACCT
#TGAACGTACTTTTCGTCCTGGCGTCATGGGCTAGC
#ACTTAATCTTTGTTTCGACTGTGAGTCACCTATGT
#ACTGTTTCTCCGAGCACTGTCCAATCGTCTTCCCT
#CCTTACGTCCCGTTGTGCGTGTCCATTCGGCAACG
#TAGATTAACTAGCTTGCCGATCGATCAGTTAATTC
#GGAGACCTCAGCAAAGTTCCGCCTCTAAACAGGTA
#CCTCTTTAACATATTGCCTAATCACCGTGGGATAT
#TCGTTAGGAATGTGGACATTTTGAATGGCCAACCT
#TGAAGTAATATTAATCGAAGTTTATTGAGCTAACC
#AGTTGACATTAGCACGTGTGGGATGCGGTCCGAAT

seq = SEQ(name="test")
Gdistance_RNA = seq.Gseq_distance(seq_len=35, char_set="AUCG", distance=5)
n = 0
while n <= 10:
    seq = next(Gdistance_RNA)
    print(seq)
    n = n + 1
#UGUGGCUCCGCACACUGGGCGCUGCCGUGAUGAGA
#ACUAGCAACGACGUAAUAGGUGCUAAUUUACAGUU
#CCUCAACGUAGUAGGGAUUCCAGCUCUACGCAUGA
#CCGCAGACCCAUAGUUAUAUAGCUUCCACUUUUUA
#CAGAGGUUCUUGCGUCUAAUCUCAUUGCAAGUAAU
#GCCCAUGGGGUACUCUUGCCCGAUGUUUGACUGUG
#UCUCCUUCGGGUAGGUGCCACACCGAGCCUUGAGU
#AACCAGAGAGUGACCAUUUGACAACGCACUACCUU
#UCACGUCAAGUUAAGCGAGCAAGAGGGCGCGUCGU
#UAACCUAUGUUCUACUCUUCACUUCUAAGUUAAGG
#CUUCGACCUCUACAUGAAGGCAAGCUUUGAAGUAU


seq = SEQ(name="test")
# When the distance is relatively large, it takes too long to obtain a sufficient number of entries. 
# At this time, set the times parameter to control the number of attempts and avoid too long loops.
Gdistance = seq.Gseq_distance(seq_len=35, distance=35, times=10)
n = 0
while n < 10:
    seq = next(Gdistance)
    print(seq)
    n = n + 1
#2024-05-21 16:31:31.828 | WARNING  | seqtools.seq:Gseq_random:150 - not found params char_set, use 'ATCG' with default
#GGAATATAGCGTTATTCAGACCTAGTAGACAATTC
#---------------------------------------------------------------------------
#StopIteration                             Traceback (most recent call last)
#Cell In[14], line 3
#      1 n = 0
#      2 while n < 10:
#----> 3     seq = next(Gdistance)
#      4     print(seq)
#      5     n = n + 1
#
#StopIteration: 
```


#### CLI

The main parameters include the length(`-gl` or `--glen`), number(`-gn` or `-gnumber`), distance(`-gd` or `--gdistance`) and try_times(`-gts` or `gtimes`) of generated sequences.

```shell

SeqTools generator -gt distance -gn 100 -gl 35 -gd 5 -out test_distance

```

<details>
    <summary>output: test_norepeat.tsv</summary>

    #generator_distance:seq_len:35;char_set:ATCG;distance:5
    ACCATTAGCACCAACAGGCAAGCTCCTGCACGGTA
    GTGCAGGCCCAACTTTCCCCACCTATAGGCTACGG
    GACCGGGCGGGACTTTCGCCCAATCATCACATACC
    AACCGGTAGTCGATGAGCGCTCATTAACACGAAGC
    GTTCTGGTCATTTATCCTCCCTCAGGTACGGATTT
    TTGCCGCTCAATTGAAAGGTACTGCCAGGAGTGTC
    AGGCCAGAACGGATATACTAGTTGCTCCAACCTGA
    ATTGACAGCAGGCGCAAGACATGCCCTAAGCCCTA
    GTAACTATCCCGAGTCGACGCAGATTGTGCTTCGG
</details>

