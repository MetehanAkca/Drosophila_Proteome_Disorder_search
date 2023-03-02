if __name__ == '__main__':
    import os
    os.system('conda env list')
    netsurf_path = '/home/metehan/Desktop/droso/tools/' \
                   'netsurfp-3.0.Linux/NetSurfP-3.0_standalone'
    fastas_path = '/home/metehan/Desktop'
    os.system(f'conda env create --file {netsurf_path}/environment.yml')
    os.system(f'conda activate nsp3')
    os.system(f'python {netsurf_path}/setup.py install')
    os.system(f'pip3 install -r {netsurf_path}/requirements.txt')