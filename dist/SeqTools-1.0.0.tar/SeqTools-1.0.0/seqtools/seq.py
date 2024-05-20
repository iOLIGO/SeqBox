import random
from loguru import logger
import Levenshtein
import numpy as np

class SEQ:
    """
    seq tools
    """
    def __init__(self, seq=None, name=None, stype=None):
        self.seq = seq
        self.stype = stype
        self.dict_base = {}
        if name:
            self.name = name
        else:
            logger.warning("not found params name, use 'name' with default")
            self.name = "name"
        
        if stype:
            if stype == "DNA":
                self.stype = stype
                self.dict_base = {
                        "A":"T",
                        "C":"G",
                        "T":"A",
                        "G":"C",
                        "a":"t",
                        "c":"g",
                        "t":"a",
                        "g":"c"
                    }
            elif stype == "RNA":
                self.stype = stype
                self.dict_base = {
                        "A":"U",
                        "C":"G",
                        "U":"A",
                        "G":"C",
                        "a":"u",
                        "c":"g",
                        "u":"a",
                        "g":"c"
                    }
            else:
                logger.error("params stype err, please check!!!")
                raise ValueError("params stype err, please check!!!")
    
    def reverse_complement(self, dict_base=None, seq=None, stype=None):
        if len(dict_base) == 0:
            logger.warning("not found params dict_base, use default dict_base")
        else:
            self.dict_base = dict_base
        
        if seq:
            if self.seq:
                logger.warning("the seq attribute is updated, using the newly provided seq!")
                self.seq = seq
            else:
                self.seq = seq
        else:
            if self.seq:
                pass
            else:
                logger.error("no seq, please check!!!")
                raise ValueError("no seq, please check!!!")
        
        if stype:
            if stype == "DNA":
                self.dict_base = {
                            "A":"T",
                            "C":"G",
                            "T":"A",
                            "G":"C",
                            "a":"t",
                            "c":"g",
                            "t":"a",
                            "g":"c"
                        }
            elif stype == "RNA":
                self.dict_base = {
                            "A":"U",
                            "C":"G",
                            "U":"A",
                            "G":"C",
                            "a":"u",
                            "c":"g",
                            "u":"a",
                            "g":"c"
                        }
            else:
                logger.error("params stype err, please check!!!")
                raise ValueError("params stype err, please check!!!")
            if self.stype:
                logger.warning("the stype attribute is updated, using the newly provided stype!")
                self.stype = stype
        else:
            if self.stype:
                pass
            else:
                logger.error("no stype, please check!!!")
                raise ValueError("no stype, please check!!!")
                

        list_seq_ = []
        for base in self.seq[::-1]:
            list_seq_.append(self.dict_base[base])
        
        seq_ = "".join(list_seq_)

        return seq_
    
    
    def variation(self, replaces, seq=None, dict_variation=None):
        if len(dict_variation) == 0:
            logger.warning("not found params dict_base, use default dict_base")
            dict_var = {"0":"", "00":"","000":"","0000":"","00000":"","00001":"","00002":"","00003":"","00004":"","00005":"","00006":"","00007":"","00008":"","00009":"","000010":"","000011":"",
                            "0001":"A","001":"A","01":"A","1":"A","0002":"T","002":"T","02":"T","2":"T","0003":"C","003":"C","03":"C","3":"C","04":"G","004":"G","0004":"G","4":"G",
                            "5":"AA","6":"AT","7":"AC","8":"AG","9":"TA","10":"TT","11":"TC","12":"TG","13":"CA","14":"CT","15":"CC","16":"CG","17":"GA","18":"GT","19":"GC","20":"GG"}
        else:
            dict_var = dict_variation
        
        list_replace = [int(l_replace) for l_replace in replaces.split(",")]

        list_seq_ = []
        for l_replace in list_replace:
            sample_list = range(len(seq))
            sample_number = list(np.random.choice(sample_list, size=l_replace, replace=False))
            replace_number = list(np.random.choice(list(dict_var.keys()), size=l_replace))
            dict_sample = {}
            for number in range(l_replace):
                dict_sample[sample_number[number]] = replace_number[number]
            seq_ = ""
            for n in sample_list:
                if n in dict_sample:
                    base = dict_var[dict_sample[n]]
                else:
                    base = seq[n]
                seq_ = seq_ + base
            list_seq_.append(seq_)

        return ",".join(list_seq_)


    def Gseq_random(self, seq_len, char_set=None, times=None):
        if char_set:
            pass
        else:
            char_set="ATCG"
            logger.warning("not found params char_set, use 'ATCG' with default")

        if times:
            times_ = 0
            while times_ <= times:
                times_ += 1
                random_seq_list = []
                for base in range(seq_len):
                    char = random.choice(char_set)
                    random_seq_list.append(char)
                seq = "".join(random_seq_list)
                yield seq
        else:
            while True:
                random_seq_list = []
                for base in range(seq_len):
                    char = random.choice(char_set)
                    random_seq_list.append(char)
                seq = "".join(random_seq_list)
                yield seq


    def Gseq_norepeat(self, seq_len, char_set=None, times=None):
        if char_set:
            pass
        else:
            char_set="ATCG"
            logger.warning("not found params char_set, use 'ATCG' with default")

        seq_set = set()
        if times:
            times_ = 0
            while times_ <= times:
                times_ += 1
                random_seq_list = []
                for base in range(seq_len):
                    char = random.choice(char_set)
                    random_seq_list.append(char)
                seq = "".join(random_seq_list)
                if seq not in seq_set:
                    seq_set.add(seq)
                    yield seq
        else:
            while True:
                random_seq_list = []
                for base in range(seq_len):
                    char = random.choice(char_set)
                    random_seq_list.append(char)
                seq = "".join(random_seq_list)
                if seq not in seq_set:
                    seq_set.add(seq)
                    yield seq
    
    def Gseq_distance(self, seq_len, distance, char_set=None, times=None):
        seq_generator = self.Gseq_random(seq_len, char_set, times)
        seq_set = set()
        for seq in seq_generator:
            if len(seq_set):
                seq_copy_set = seq_set.copy()
                filter_true = 0
                for seq_filt in seq_copy_set:
                    if Levenshtein.distance(seq, seq_filt) < distance:
                        filter_true = filter_true + 1
                        break
                if filter_true == 0:
                    seq_set.add(seq)
                    yield seq
            else:
                seq_set.add(seq)
                yield seq

