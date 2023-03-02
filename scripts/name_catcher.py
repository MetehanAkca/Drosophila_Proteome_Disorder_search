import os
import paths
with open(paths.names_path,'r') as fl:
    for item in fl.readlines():
        name = item.strip('\t').strip('\n').strip().replace('/','-')
        print(name)
        os.system( f'cd {paths.fasta_path_1}&& touch "{name}".txt'
                   f'')
