import os
import requests, sys
import lxml.etree



with open('/home/metehan/Desktop/droso/tools/netsurfp-3.0.Linux/'
          'NetSurfP-3.0_standalone/qc_fastas/uniprot_ids.txt','r') as fl:
    for item in fl:

        requestURL = f"https://www.ebi.ac.uk/proteins/api/proteins?offset=0&size=100&accession={item.strip()}"

        r = requests.get(requestURL, headers={"Accept": "application/xml"})

        if not r.ok:
            r.raise_for_status()
            sys.exit()

        responseBody = r.text.encode('ascii')
        q = lxml.etree.fromstring(responseBody)
        print(q.findall('.//sequence'))

#Todo Fix lxml parser