#! /usr/bin/env python3

import requests, sys


class objAPI():
    def __init__(self,token):
        self.apikey = token
        self.headers = {'x-cisco-meraki-api-key': self.apikey, 'content-type': "application/json"}

    def get(self,api):
        try:
            url = 'https://dashboard.meraki.com/api/v0/{}'.format(api)
            resp = requests.get(url,headers=self.headers)
            resp.raise_for_status()
            return resp
        except:
            print("Something wrong to GET /", api)
            sys.exit()

    def get2(self,api,params):
        try:
            url = 'https://dashboard.meraki.com/api/v0/{}'.format(api)
            resp = requests.get(url,headers=self.headers,params=params)
            resp.raise_for_status()
            return resp
        except:
            print("Something wrong to GET /", api)
            sys.exit()


