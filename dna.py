# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 18:29:40 2020

@author: Lulock
"""
import random

"""
    The information in DNA is stored as a code made up of four chemical bases: adenine (A), guanine (G), cytosine (C), and thymine (T). Human DNA consists of about 3 billion bases, and more than 99 percent of those bases are the same in all people.
"""

bases = ["A","T","C","G","U"]

base_dict = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
    }

def base_pair(base):
    """
    Function returning complementary base to DNA chemical base
    
    Parameters
    ----------
    base : single letter of type String, one of four chemical bases adenine (A), guanine (G), cytosine (C), and thymine (T).

    Returns
    -------
    single letter of type String, complementary base, one of adenine (A), guanine (G), cytosine (C), and thymine (T).

    """
    if base not in base_dict.keys():
        print("Only one of A,T,G,C is accepted. x is returned to mark the anomaly")
        return "x"
    else:
        return base_dict[base]
    
    
def complementary(sequence):
    """
    Function returning complementary strand of single DNA strand 
    
    Parameters
    ----------
    base : String of single letter bases, should be made up of one of four chemical bases adenine (A), guanine (G), cytosine (C), and thymine (T).

    Returns
    -------
    String of single letter bases, equal in length and complementary strand to that which was provided as input. If unexpected letter encountered, x is return to mark anomoly

    """
    complement = ""
    for base in sequence:
        complement += base_pair(base)
        
    return complement


def synthesise_sequence(length):
    """
    Function synthesising a random sequence of DNA bases of specified length
    
    Parameters
    ----------
    length : int determining length of the sequence

    Returns
    -------
    string of DNA bases with specified length
    """
    strand=""
    len=0
    try:
        len=int(length)
    except:
        print("in order to synthesise a sequence, numeric value for length is required")
    
    for i in range(0,len):
        strand += bases[random.randint(0,3)]
    return strand


def print_dna(strand,complement):
    """
    Function prints a given sequence of DNA bases and its complement
    
    Parameters
    ----------
    strand : string
    complement : string

    Returns
    -------
    none
    """
    link="'"*len(strand)
    print(f"{strand}\n{link}\n{complement}")


strand=synthesise_sequence(6.3)
print_dna(strand,complementary(strand))
