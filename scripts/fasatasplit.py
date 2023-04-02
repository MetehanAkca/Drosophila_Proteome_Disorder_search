import paths
prots = {}
with open(f'{paths.proteome}','r') as fl:
    for line in fl.readlines():
        sequence = ''
        if line[0] =='>':
            primary_id = line.split('|')[1]
            prots[primary_id] = sequence
        else:
            prots[primary_id] +=line.strip('\n').strip('\t').strip()
for key in prots.keys():
    with open(f"{paths.split_proteome}/{key}.fasta","w") as fl:
        print(f'>{key},{prots[key]},',sep="\n",file=fl)