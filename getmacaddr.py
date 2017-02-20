#! /usr/bin/env python3
__author__ = 'sihart'

import requests, sys, json


class objAPI():
    def __init__(self):
        self.name = __author__


    def get(self,mac):
        try:
            url = 'http://api.macvendors.com/'+mac
            resp = requests.get(url)
            resp.raise_for_status()
            return resp
        except:
            return 'none'


