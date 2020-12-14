import os
import uuid
from OpenSSL import crypto
import requests
import jwt
import json
from datetime import datetime, timedelta

from swagger_client import Customer, ApiClient, CustomerApi, BusinessRelationApi


class ApiConnection:

    def __init__(self, client_id, audience, api_base_url):
        self.client_id = client_id
        self.audience = audience
        self.base_url = api_base_url

        self.create_jwt_token(self.read_certificate(os.getenv("certPath"), str.encode(os.getenv("password"))))
        self.get_access_token()
        self.api_get_company_info()
        self.create_api_client()

    # Reads the certificate which must be in p12-format, and sets the private key of the certificate.
    # The private key of the sertificate is used to sign the jwt token, which will prove we have the
    # private key of the certificate. This authenticates us to create the access token to connect
    # to the API.
    #
    # Input:
    #   - Path to certificate (string)
    #   - Certificate password (string)
    #
    # Output:
    #   - Nothing, sets the certificate private key as a class variable.
    def read_certificate(self, path, cert_password):
        with open(path, 'rb') as pkcs12_file:
            pkcs12_data = pkcs12_file.read()
        cert_data = crypto.load_pkcs12(pkcs12_data, cert_password)

        return crypto.dump_privatekey(crypto.FILETYPE_PEM, cert_data.get_privatekey())

    # Creates the jwt token used to request the access token.
    #
    # Needs (All are set in the initialization method):
    #   - The certificate private key
    #   - The client id
    #   - The audience
    #
    # Output:
    #   - Nothing, sets the jwt token as a class variable.
    def create_jwt_token(self, cert_priv_key):
        issue_time = datetime.utcnow()
        exp_time = issue_time + timedelta(minutes=1)

        encoded_jwt = jwt.encode(
            {
                'jti': str(uuid.uuid4()),
                'sub': self.client_id,
                'iat': issue_time,
                'nbf': issue_time,
                'exp': exp_time,
                'iss': self.client_id,
                'aud': self.audience
            },
            cert_priv_key,
            algorithm='RS256'
        )

        self.jwt_token_encoded = encoded_jwt

    # Requests the access token needed to communicate with the API.
    #
    # Needs (All are set in the initialization method):
    #   - The client id
    #   - The jwt token, signed with the private key of the certificate.
    #   - The audience (which is the url to request access token from)
    #
    # Output:
    #   - Nothing, sets the access token as a class variable.
    def get_access_token(self):
        data = {
            'grant_type':'client_credentials',
            'scope':'AppFramework.All',
            'client_id':self.client_id,
            'client_assertion_type':'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
            'client_assertion':self.jwt_token_encoded
        }

        res = requests.post(
            self.audience,
            data=data
        )

        self.access_token = res.json()["access_token"]

    # Gets information about the companies you have access to, you ned the company key for the company
    # you want to perform actions against.
    #
    # Needs (All are set in the initialization method):
    #   - Valid access token
    #
    # Output:
    #   - Nothing, sets the company key as a class variable.
    def api_get_company_info(self):
        try:
            headers = {"Authorization": "Bearer "+self.access_token}
            res = requests.get(r"https://test.softrig.com/api/init/companies", headers=headers)

            if res.status_code == 200:
                self.company_key = res.json()[0]["Key"]
            else:
                raise Exception("Problemer med å koble til API, har du riktig access token?")
        except Exception as err:
            print(err)

    def create_api_client(self):
        headers = {"Authorization": "Bearer " + self.access_token, "CompanyKey": self.company_key}
        self.apiClient = ApiClient()
        for headerName in headers.keys():
            self.apiClient.set_default_header(headerName, headers[headerName])

    # Method used to perform GET requests to the API.
    #
    # Input:
    #   - Valid GET API endpoint
    #
    # Output:
    #   - Result of the request formated as JSON, or -1 if the status code is not 200.
    def api_get_request(self, endpoint):
        try:
            headers = {"Authorization": "Bearer "+self.access_token, "CompanyKey":self.company_key}
            res = requests.get(r"https://test.softrig.com/api/"+endpoint, headers=headers)

            if res.status_code == 200:
                return res.json()
            else:
                raise Exception("Problemer med å koble til API, har du riktig access token?")
        except Exception as err:
            print(err)
            print(res.status_code)
            return -1

    # Method used to perform POST requests to the API.
    #
    # Input:
    #   - Valid POST API endpoint
    #   - POST body data in the form of a dictionary
    #
    # Output:
    #   - The resulting response code, or -1 if the response code is not 200.
    def api_post_request(self, endpoint, data):
        try:
            headers = {"Authorization": "Bearer "+self.access_token, "CompanyKey":self.company_key}
            res = requests.post(r"https://test.softrig.com/api/"+endpoint, json=data, headers=headers)

            if res.status_code == 200:
                return res.json()
            else:
                raise Exception("Problemer med å koble til API, har du riktig access token?")
        except Exception as err:
            print(err)
            print(res.status_code)
            return -1

    # Method used to perform DELETE requests to the API.
    #
    # Input:
    #   - Valid DELETE API endpoint
    #   - DELETE body data in the form of a dictionary
    #
    # Output:
    #   - The resulting response code, or -1 if the response code is not 204.
    def api_delete_request(self, endpoint, data):
        try:
            headers = {"Authorization": "Bearer "+self.access_token, "CompanyKey":self.company_key}
            res = requests.delete(r"https://test.softrig.com/api/"+endpoint, json=data, headers=headers)

            if res.status_code == 204:
                return res.status_code
            else:
                raise Exception("Problemer med å koble til API, har du riktig access token?")
        except Exception as err:
            print(err)
            print(res.status_code)
            return -1

    # Method used to perform DELETE requests to the API.
    #
    # Input:
    #   - Valid PUT API endpoint
    #   - PUT body data in the form of a dictionary
    #
    # Output:
    #   - The resulting response code, or -1 if the response code does not indicate success (200 = success).
    def api_put_request(self, endpoint, data):
        try:
            headers = {"Authorization": "Bearer "+self.access_token, "CompanyKey":self.company_key}
            res = requests.put(r"https://test.softrig.com/api/"+endpoint, json=data, headers=headers)

            if res.status_code == 200:
                return res.status_code
            else:
                raise Exception("Problemer med å koble til API, har du riktig access token?")
        except Exception as err:
            print(err)
            print(res.status_code)
            return -1

    # Methods used to verify the above API calls work as intended.
    # Examples of valid uses of the methods:
    # - res = conn.create_customer("Anders Tester6", 123762624347)
    # - conn.change_customer_info(res["ID"], {"ID":res["ID"], "AvtaleGiro": "true"})
    # - print(conn.get_customers())
    # - conn.delete_customer(str(res["ID"]))
    def create_customer(self, company_name, *args):
        data = {"Info": {"Name":company_name},"OrgNumber":args[0]}

        return self.api_post_request(r"biz/customers", data)

    def delete_customer(self, customer_id):
        self.api_delete_request(r"biz/customers/"+customer_id, None)

    def get_customers(self):
        return json.dumps(conn.api_get_request(r"biz/customers"),indent=4, sort_keys=True)

    def change_customer_info(self, id, data):
        self.api_put_request(r"biz/customers/"+str(id), data)

    def create_customer_new(self, company_name, *id):
        data = {"Info": {"Name": company_name}, "OrgNumber": id[0]}
        customerApi = CustomerApi(self.apiClient)
        res = customerApi.customers_post(data)
        return res

    def get_customers_new(self,*args):
        customerApi = CustomerApi(self.apiClient)
        if not args:
            return customerApi.customers_get()
        else:
            customer = customerApi.customers_id_get(args[0])  #type: Customer
            cust_br = BusinessRelationApi(self.apiClient).business_relations_id_get(customer.business_relation_id)
            return customer, cust_br

    def delete_customer_new(self, customer_id):
        customerApi = CustomerApi(self.apiClient)
        result = customerApi.customers_id_delete(customer_id)

    def update_customer_new(self, customer_id, data):
        customerApi = CustomerApi(self.apiClient)
        res = customerApi.customers_id_put(data, customer_id)
        return res

if __name__ == '__main__':

    client_id = "3a726a33-0f53-44a7-8415-a44dff248d77"
    audience = r"https://test-login.softrig.com/connect/token"
    api_base_url = r"https://test.softrig.com/api/init/"

    conn = ApiConnection(client_id, audience, api_base_url)

    #print(conn.access_token)
    customers = conn.get_customers_new()
    new_customer = conn.create_customer_new("Anders ny-testing", 1256363516)
    print(new_customer.org_number)
    print(new_customer.avtale_giro)
    new_customer.avtale_giro = True
    chg = conn.update_customer_new(new_customer.id, new_customer)
    # NB!: Må sende in kunde-objekt med oppdaterte verdier, ikke bare en dictionary med de verdiene du ønsker å endre
    updated_customer,br = conn.get_customers_new(new_customer.id)
    print(updated_customer.org_number)
    print(br.name)
    print(updated_customer.avtale_giro)
    rem = conn.delete_customer_new(new_customer.id)
