#!/usr/bin/env python
# encoding: utf-8
"""
GenerateSequenceChunks.py

Created by Nikolaus Sonnenschein on 2010-10-25.
Copyright (c) 2010 Jacobs University of Bremen. All rights reserved.

Reads a list of genbank and fasta files and constructs a fasta file of random
sequence chunks from them ...

"""

import sys
import os
import random
import uuid
from Bio import SeqIO
from Bio.Seq import Seq, SeqRecord

USAGE = """Usage:

python GenerateSequenceChunks numChunks chunkSize seqFile1 seqFile2 ... outputFile
"""

def dict2tsv(d):
    """docstring for dict2tsv"""
    return '\n'.join(tuple(['\t'.join((k,v)) for k, v in d.items()]))

def readSequenceFiles(paths2seq):
    """Read in a bunch of sequence files. Try to guess the format ..."""
    sequences = list()
    for path in paths2seq:
        fextension = path.split('.')[-1]
        if fextension[0] == 'f':
            ftype = 'fasta'
        elif fextension[0] == 'g':
            ftype = 'genbank'
        else:
            print "Cannot guess filetype. Trying fasta ..."
            ftype = 'fasta'
        try:
            handle = open(path)
            seq = SeqIO.read(handle, ftype)
        except IOError, msg:
            print "The file " + path + " does not exist!"
            print msg
            sys.exit()
        # print "Successfully read", seq.id
        sequences.append(seq)
    return sequences

def constructRandomChunks(sequences, numChunks=10, chunksize=1000):
    """Construct random sequ"""
    rndChunks = list()
    mapping = dict()
    for s in sequences:
        for c in range(numChunks):
            rndPos = random.randint(0, len(s) - chunksize)
            rndSeq = s.seq[rndPos:rndPos+chunksize]
            rndID = str(uuid.uuid1())
            rndChunks.append(SeqRecord(rndSeq, rndID))
            mapping[rndID] = s.description
    random.shuffle(rndChunks)
    return rndChunks, mapping

def main(paths2seq, outputPath, mappingPath, numChunks=10, chunksize=1000):
    sequences = readSequenceFiles(paths2seq)
    rndChunks, mapping = constructRandomChunks(sequences, numChunks=numChunks, chunksize=chunksize)
    handle = open(outputPath, 'w')
    SeqIO.write(rndChunks, handle, 'fasta')
    handle.close()
    handle = open(mappingPath, 'w')
    handle.write(dict2tsv(mapping))
    handle.close()
    

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print USAGE
        sys.exit()
    main(sys.argv[3:-2], sys.argv[-2], sys.argv[-1], numChunks=int(sys.argv[1]), chunksize=int(sys.argv[2]))

