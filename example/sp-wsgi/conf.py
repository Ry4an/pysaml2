from saml2.entity_category.edugain import COC
from saml2 import BINDING_HTTP_REDIRECT
from saml2 import BINDING_HTTP_POST
from saml2.saml import NAME_FORMAT_URI

try:
    from saml2.sigver import get_xmlsec_binary
except ImportError:
    get_xmlsec_binary = None


if get_xmlsec_binary:
    xmlsec_path = get_xmlsec_binary(["/opt/local/bin","/usr/local/bin"])
else:
    xmlsec_path = '/usr/local/bin/xmlsec1'

# Make sure the same port number appear in service_conf.py
BASE = "http://localhost:8087"

CONFIG = {
    "entityid": "%s/%ssp.xml" % (BASE, ""),
    'entity_category': [COC],
    "description": "Example SP",
    "service": {
        "sp": {
            "endpoints": {
                "assertion_consumer_service": [
                    ("%s/acs/redirect" % BASE, BINDING_HTTP_REDIRECT),
                    ("%s/acs/post" % BASE, BINDING_HTTP_POST)
                ],
            }
        },
    },
    "key_file": "pki/mykey.pem",
    "cert_file": "pki/mycert.pem",
    "xmlsec_binary": xmlsec_path,
    "metadata": {"local": ["../idp2/idp.xml"]},
    #"metadata": {"mdfile": ["./swamid2.md"]},
    #"metadata": {"local": ["./swamid-2.0.xml"]},
    "name_form": NAME_FORMAT_URI,
}
