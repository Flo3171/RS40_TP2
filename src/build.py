# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

from tools.core import Configuration
from ca.core import CertificateAuthority
from server.core import Server
import print_pems as pems  #a été ajouté pour l'impression

RESOURCES_DIR = "src/resources/"
CA_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "ca-private-key.pem"
CA_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "ca-public-key.pem"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_CSR_FILENAME = RESOURCES_DIR + "server-csr.pem"
SERVER_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "server-public-key.pem"
CA_PASSWORD = "La RS40 c'est trop génial"
SERVER_PASSWORD = "La RS40 c'est trop génial"

CA_CONFIGURATION = Configuration("FR", "Territoire de Belfort", "Sevenans", "UTBM_CA", "localhost") 
SERVER_CONFIGURATION = Configuration("FR", "Territoire de Belfort", "Sevenans", "UTBM_SER", "localhost") 

# Création de l'autorité de certification
certificate_authority = CertificateAuthority(CA_CONFIGURATION, CA_PASSWORD, CA_PRIVATE_KEY_FILENAME, CA_PUBLIC_KEY_FILENAME)
    # regardez en haut et ca/core.py

# Création du server
#server = Server(SERVER_CONFIGURATION, SERVER_PASSWORD, SERVER_PRIVATE_KEY_FILENAME, SERVER_PUBLIC_KEY_FILENAME)
server = Server(SERVER_CONFIGURATION, SERVER_PASSWORD, SERVER_PRIVATE_KEY_FILENAME, SERVER_CSR_FILENAME)
    # regardez en haut et server/core.py

# Signature du certificat par l'autorité de certification
#signed_certificate = server.get_csr()

signed_certificate = certificate_authority.sign(server.get_csr(), server._csr_filename)

# A compléter regardez ca/core.py et server/core.py

#impression des certificats à compléter regardez #print_pems

pems.print_pems(CA_PUBLIC_KEY_FILENAME)
pems.print_pems(CA_PRIVATE_KEY_FILENAME)
pems.print_pems(SERVER_CSR_FILENAME)



print("finished ...")
