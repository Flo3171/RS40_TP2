# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""
from src.tools.core import Configuration, generate_private_key, generate_public_key, sign_csr

RESOURCES_DIR = "resources/"
CA_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "ca-private-key.pem"
CA_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "ca-public-key.pem"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_CSR_FILENAME = RESOURCES_DIR + "server-csr.pem"
SERVER_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "server-public-key.pem"
CA_PASSWORD = "La RS40 c'est trop génial"
SERVER_PASSWORD = "La RS40 c'est trop génial"


class CertificateAuthority:

    def __init__(self, config: Configuration, password: str, private_key_filename: str, public_key_filename: str):
        self._config = config
        self._private_key = generate_private_key(CA_PRIVATE_KEY_FILENAME, CA_PASSWORD)
        self._public_key = generate_public_key(self._private_key, CA_PUBLIC_KEY_FILENAME, self._config)
        self._private_key_filename = private_key_filename
        self._public_key_filename = public_key_filename
        self._password = password

    def sign(self, csr, certificate_filename: str):
        sign_csr(csr, self._public_key, self._private_key, SERVER_CSR_FILENAME)
