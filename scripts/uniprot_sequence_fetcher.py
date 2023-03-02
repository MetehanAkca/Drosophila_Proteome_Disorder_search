from rdflib import Graph

"""fasta_path_1 = '/home/metehan/Desktop/droso/tools/netsurfp-3.0.Linux/' \
               'NetSurfP-3.0_standalone/qc_fastas/uniprot_ids.txt'

with open(fasta_path_1,'r') as fl:
    id_s = (fl.readlines())
    with open('rdf_data','w') as fl_2:
        for id in id_s:
            print(id)
            g = Graph()
            # read id in RDF/XML format
            g.parse(f"https://www.uniprot.org/uniprot/{id}.rdf")
            fasta = g.serialize(format="turtle")
            print(fasta,file = fl_2)



    PREFIX foaf: <http://xmlns.com/foaf/0.1/>

    SELECT ?name
    WHERE {
        ?p rdf:type foaf:Person .

        ?p foaf:name ?name .
    }
"""
import requests
fasta_path_1 = '/home/metehan/Desktop/droso/tools/netsurfp-3.0.Linux/' \
               'NetSurfP-3.0_standalone/qc_fastas/uniprot_ids.txt'

with open(fasta_path_1,'r') as fl:
    id_s = (fl.readlines())
    with open('rdf_data','w') as fl_2:
        for id in id_s:
            api_url = f'http://www.ebi.ac.uk/proteins/api/proteins/{id.strip()}'
            response = requests.get(api_url)
            print(response.json()['sequence']['sequence'])