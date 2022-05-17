# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

from flask import Flask

# définir le message secret
from src.build import SERVER_CSR_FILENAME, SERVER_PUBLIC_KEY_FILENAME

SECRET_MESSAGE = "La RS40 c'est trop génial"  # A modifier
app = Flask(__name__)


@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE


if __name__ == "__main__":
    # HTTP version
    # app.run(debug=True, host="0.0.0.0", port=8081)
    # HTTPS version
    # A compléter  : nécessité de déplacer les bons fichiers vers ce répertoire
    app.run(ssl_context=(SERVER_CSR_FILENAME, SERVER_PUBLIC_KEY_FILENAME))
