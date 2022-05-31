# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

from flask import Flask

HTTPS_MODE = True

# définir le message secret

SECRET_MESSAGE = "La RS40 c'est trop génial"  # A modifier
app = Flask(__name__)


@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE


if __name__ == "__main__":
    if HTTPS_MODE == False:
        # HTTP version
        app.run(debug=True, host="0.0.0.0", port=8081)
    else :
        # HTTPS version
        # A compléter  : nécessité de déplacer les bons fichiers vers ce répertoire
        context = ("resources/server-public-key.pem", "resources/server-private-key.pem")
        app.run(debug=True, host="0.0.0.0", port=8081, ssl_context=("resources/server-public-key.pem", "resources/server-private-key.pem"))
