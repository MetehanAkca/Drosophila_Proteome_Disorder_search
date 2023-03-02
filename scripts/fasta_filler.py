import requests
import paths
with open(f'{paths.fasta_path_1}/uniprot_ids.txt','r') as fl:
    id_s = (fl.readlines())
    for id in id_s:
            api_url = f'http://www.ebi.ac.uk/proteins/api/proteins/{id.strip()}'
            response = requests.get(api_url)
            sequence = response.json()['sequence']['sequence']
            try:
                name =(response.json())['protein']['recommendedName']['fullName']['value']
            except:
                name = (response.json()['protein']['submittedName'][0]['fullName']['value'])
            finally:
                with open(f'{paths.fasta_path_1}/{name}.txt','w') as fl_2:
                    print(sequence,file=fl_2)

