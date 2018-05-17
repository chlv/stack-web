from ldap3 import Server, Connection, Tls, ALL
import ssl


def authorize(ntaccount, password):
    tls_configuration = Tls(version=ssl.PROTOCOL_TLSv1)
    server = Server("atlldap.amd.com:636", use_ssl=True, tls=tls_configuration, get_info=ALL)
    try:
        conn = Connection(server, user="AMD\\{0}".format(ntaccount), password=password, auto_bind=True)
        if conn.result["description"] == "success":
            print("Auth Pass")
        else:
            print("Auth Fail")
    except Exception as e:
        print("Exception Found!")



authorize("chlv", "!!!111qqq")

