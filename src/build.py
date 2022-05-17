# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

from tools.core import Configuration
from ca.core import CertificateAuthority
from server.core import Server
import print_pems as pems  #a été ajouté pour l'impression

RESOURCES_DIR = "resources/"
CA_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "ca-private-key.pem"
CA_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "ca-public-key.pem"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_CSR_FILENAME = RESOURCES_DIR + "server-csr.pem"
SERVER_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "server-public-key.pem"
CA_PASSWORD = "Comment est votre blanquette ?"
SERVER_PASSWORD = "Elle est bonne."

CA_CONFIGURATION = Configuration("FR", "Territoire de Belfort", "Sevenans", "UTBM_CA", "localhost") 
SERVER_CONFIGURATION = Configuration("FR", "Territoire de Belfort", "Sevenans", "UTBM_SER", "localhost") 

# Création de l'autorité de certification
certificate_authority = CertificateAuthority(CA_CONFIGURATION, CA_PASSWORD, CA_PRIVATE_KEY_FILENAME, CA_PUBLIC_KEY_FILENAME)
    # regardez en haut et ca/core.py

# Création du server
server =Server(SERVER_CONFIGURATION, SERVER_PASSWORD, SERVER_PRIVATE_KEY_FILENAME, SERVER_CSR_FILENAME)
    # regardez en haut et server/core.py

# Signature du certificat par l'autorité de certification
signed_certificate = certificate_authority.sign(server.get_csr(), SERVER_PUBLIC_KEY_FILENAME)
# A compléter regardez ca/core.py et server/core.py

#impression des certificats à compléter regardez #print_pems
print("CA Private Key:")
pems.print_perms("ca-private-key.pem")
print("CA Public Key:")
pems.print_perms("ca-public-key.pem")
print("Server Private Key:")
pems.print_perms("server-private-key.pem")
print("Server CRS:")
pems.print_perms("server-csr.pem")
print("Server Public Key:")
pems.print_perms("server-public-key.pem")
print("Signed Certificate:")
pems.print_perms(signed_certificate)




print("finished ...")
