import paths
import os

fastas = [i for i in (os.listdir(paths.fasta_path_1)) if '.fasta' in i]
#with open('merged_qc.fasta','w') as fl:
with open('merged_qc.fasta','w') as fl:
    for item in fastas:
        with open(f'{paths.fasta_path_1}/{item}','r') as fs:
            for line in fs.readlines():
                print(line,file = fl,end = '\n')
