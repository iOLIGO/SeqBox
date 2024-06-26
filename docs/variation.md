## variation

random transformation of sequences, including deletions, additions and mutations.


### usage

<details>
    <summary>SeqBox variation</summary>

    usage: SeqBox variation [-h] [-out OUT] [-od OUT_DIR] [-vi VIN] [-vr VREPLACE]
                            [-vd VDICT]

    optional arguments:
    -h, --help            show this help message and exit
    -out OUT, --out_file OUT
                            sequence out file with TSV format
    -od OUT_DIR, --out_dir OUT_DIR
                            out direction
    -vi VIN, --vinfile VIN
    -vr VREPLACE, --vreplace VREPLACE
                            replace base number, like: 1,2,3
    -vd VDICT, --vdict VDICT
                            variation dict, like: '1:A-2:T-3:C-4:G'

</details>


### API

```python

from seqbox import SEQ
seq = SEQ(name="test")
seq.name
#'test'
seq.variation(replaces="1,2,3", seq="ATCGTCGTAGTCGTAGCTAGTCGTAGTAGCTAGT")
#2024-05-21 16:44:48.188 | WARNING  | seqbox.seq:variation:118 - not found params dict_base, use default dict_base
#'ATCGTCGTAGTCGTAGCTAGTCGTAGTAGCTAGT,ACGTCGTAGTCGTACTAGTCGTAGTAGCTAGT,ATCGTCGTAGTGTAGTAGTCGTAGTAGCTAT'

```

### CLI

The main parameters are base variation length(`-vr` or `--vreplace`), input file(`-vi` or `--vinfile`), and variation encoding(`-vd` or `--vdict`).

```shell

SeqBox variation -vi test.tsv -out test_variation -vr 1,2,3

```


<details>
    <summary>input: test.tsv</summary>

    #seq
    ACCATTAGCACCAACAGGCAAGCTCCTGCACGGTA
    GTGCAGGCCCAACTTTCCCCACCTATAGGCTACGG
    GACCGGGCGGGACTTTCGCCCAATCATCACATACC
    AACCGGTAGTCGATGAGCGCTCATTAACACGAAGC
    GTTCTGGTCATTTATCCTCCCTCAGGTACGGATTT
    TTGCCGCTCAATTGAAAGGTACTGCCAGGAGTGTC
    AGGCCAGAACGGATATACTAGTTGCTCCAACCTGA
    ATTGACAGCAGGCGCAAGACATGCCCTAAGCCCTA
    GTAACTATCCCGAGTCGACGCAGATTGTGCTTCGG
    CGTAGCCTAGGCGTGGGATTATAACTCTCCGGTAA

</details>



<details>
    <summary>output: test_variation.tsv</summary>

    seq_raw	seq_var1	seq_var2	seq_var3
    ACCATTAGCACCAACAGGCAAGCTCCTGCACGGTA	ACCATAGCACCAACAGGCAAGCTCCTGCACGGTA	ACCATTAGCACCTACAGGCAGCTCCTGCACGGTA	ACCATTAGCACCAACAGGCAAGCTCCCGCCGGA
    GTGCAGGCCCAACTTTCCCCACCTATAGGCTACGG	GTGCAGGCCCAACTTTCCCCACCTATAGGATACGG	GTCAAGGCCCAACTTTCCCCACCTATAGGCTACGG	GTGCAGCCAACTTTCCCACCTATAGGCTACGG
    GACCGGGCGGGACTTTCGCCCAATCATCACATACC	GACCGCGGCGGGACTTTCGCCCAATCATCACATACC	GACCGGGCGGGACTTTCCCCAATGGATCACATACC	GACCGGGCGGGACTTTCGGCCAATCATCACATACA
    AACCGGTAGTCGATGAGCGCTCATTAACACGAAGC	AACCGGTAGTCGATAGCGCTCATTAACACGAAGC	AACCGGTAGTATGATGAGCGCTCATTAACACTAAGC	AACCGGTGTCGATGAGCGCTTCATTAACACGAAGC
    GTTCTGGTCATTTATCCTCCCTCAGGTACGGATTT	GTTCTGGTCATTTATCCTCCCTCAGGTACGGATTA	GTTCTGGTCATTTATCTCCCTCAGGTACGGATT	GTTCTGGTCATTATCCTCTTGTTCAGGTACGGATTT
    TTGCCGCTCAATTGAAAGGTACTGCCAGGAGTGTC	TTGCCGCTCAATTGAAAGGTACTGCCAGGAGTGTC	TTGCCGCTCAATTAAAGGTACTGCAGGAGTGTC	TTGCCGCTCAATTGTGGAAGGTACTGCCAGGCGTGTC
    AGGCCAGAACGGATATACTAGTTGCTCCAACCTGA	AGGCCAGAACGGATATACTAGTTGCTCCAACCTTA	AGGCCAGAACGCTATAAAACTAGTTGCTCCAACCTGA	AGGCACAACGGATATACTAGTGCTCCAACCTGA
    ATTGACAGCAGGCGCAAGACATGCCCTAAGCCCTA	ATTGACAGCAGGCGCAAACACATGCCCTAAGCCCTA	ATTGACAGCAGGCGCAAAACATGCCCTAAGCCTA	ATTGATGAGCAGGCGCAATACATGCCCTAGCCCTA
    GTAACTATCCCGAGTCGACGCAGATTGTGCTTCGG	GTAACTATCCCGAGTCGACGCAGATTGTGCTCGG	GTAACTATCCCGAGTCACGCAGATTGGAGCTTCGG	GTAACTATCCCGATCGACGCAGATTGTCCCTTCGG
    CGTAGCCTAGGCGTGGGATTATAACTCTCCGGTAA	CGTAGCCTAGGCGTGGGATATAACTCTCCGGTAA	CGTAAGCCTAGGCGTGGGATATAACTCTCCGGTAA	CGTAGCCGAAGCGTGGGATATAACTCTCCGGTAA

</details>


### vdict

default variation dict: deletions, mutations, and additions, the ratio of the three mutation types is 1:1:1. Customize using parameters(`-vd` or `-vdict`), like: `0- ;00- ;1-A;2-T`.

```python
dict_var = {"0":"", "00":"","000":"","0000":"","00000":"","00001":"","00002":"","00003":"","00004":"","00005":"","00006":"","00007":"","00008":"","00009":"","000010":"","000011":"",
"0001":"A","001":"A","01":"A","1":"A","0002":"T","002":"T","02":"T","2":"T","0003":"C","003":"C","03":"C","3":"C","04":"G","004":"G","0004":"G","4":"G",
"5":"AA","6":"AT","7":"AC","8":"AG","9":"TA","10":"TT","11":"TC","12":"TG","13":"CA","14":"CT","15":"CC","16":"CG","17":"GA","18":"GT","19":"GC","20":"GG"}
```

