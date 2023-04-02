import os
import paths
with open(f'{paths.proteome}','r') as fl:
    primary_ids = [line.split(' ')[0].split('|')[1] for line in fl.readlines() if line[0] == '>']
with open(f'{paths.split_proteome}/1.txt','r') as fl:
    files = fl.readlines()

    files = [file.strip('\n').strip('.fasta') for file in files]

    files.sort()
    primary_ids.sort()
    print(len(primary_ids),len(files))
    print(files == primary_ids)
    for p in primary_ids:
        if p not in files:
            print(p)