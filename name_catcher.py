import os
with open('/home/metehan/Desktop/droso/tools/netsurfp-3.0.Linux/NetSurfP-3.0_standalone/qc_fastas/names.txt','r') as fl:
    for item in fl.readlines():
        name = item.strip('\t').strip('\n').strip().replace('/','-')
        print(name)
        os.system( f'cd /home/metehan/Desktop/droso/tools/netsurfp-3.0.Linux/NetSurfP-3.0_standalone/qc_fastas'
                   f'&& touch "{name}".txt')
