import paths
with open(f'{paths.proteome}','r') as fl:
    lines = fl.readlines()

    for line in lines:
        if line[0] == '>':
            primary_id = line.split(' ')[0].split('|')[1]
            sequence = ''
        else:
            sequence += line
            try:
                if lines[lines.index(line)+1][0] == '>':
                    with open(f'{paths.split_proteome}/{primary_id}.fasta', 'w') as pl:
                        print (f'>{primary_id}',sequence,file= pl,sep="\n")
            except:
                with open(f'{paths.split_proteome}/{primary_id}.fasta', 'w') as pl:
                    print(f'>{primary_id}', sequence, file=pl,sep="\n")
