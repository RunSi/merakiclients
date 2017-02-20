#! /usr/bin/env python3
__author__ = 'sihart'
import json, getmeraki, netaddr, getmacaddr
import datetime
from flask import Flask
from flask import make_response
from flask import render_template
from flask import request
from configparser import ConfigParser

app = Flask(__name__)

conf = ConfigParser()
conf.read('meraki_ini.cnf')
token = conf.get('section_one','meraki_token')
network_id = conf.get('section_one', 'network_id')

api = '/networks/{}/devices'.format(network_id)

ipurl = '/devices/{}/clients'
DAYS = list(range(1,31))


@app.route("/")
def home():
    clients = request.args.get('clients')
    if not clients:
        clients = 'MR16'

    days = request.args.get('days')
    if not days:
        days = 1
    else:
        days = int(days)

    tspan= days*86400

    alldevices, keys = getdata(api)

    ip = getips(clients, alldevices, tspan)

    return render_template("home.html", device=clients, clients=alldevices, ip = ip, days=DAYS, time=days)


def getips(client, alldevices,tspan):
    merakiobj = getmeraki.objAPI(token)

    clientips = merakiobj.get2(ipurl.format(alldevices[client]), params={"timespan": tspan}).json()

    ipclient = {}
    macobj = getmacaddr.objAPI()
    for i, n in enumerate(clientips):
        r_ip = netaddr.IPNetwork(clientips[i]['ip'])
        r_mac = clientips[i]['mac']
        macadd = macobj.get(r_mac)
        if macadd == 'none':
            ipclient[(r_ip.value)] = [clientips[i]['description'], 'none']
        else:
            ipclient[(r_ip.value)] = [clientips[i]['description'], macadd.text]
    client = ipclient

    mylist = []
    allips = []

    for i in sorted(client):

        myip = [str(netaddr.IPAddress(i))]


        myclient = client[i]


        mylist.append(myip + myclient)



    return mylist



def getdata(api):
    merakiobj = getmeraki.objAPI(token)

    devices = merakiobj.get(api).json()

    alldevices =['ALL']
    serial = []
    devicedict={}

    for i, name in enumerate(devices):

        devicedict[devices[i]['model']]=devices[i]['serial']
    return devicedict, devicedict.keys()





if __name__ =="__main__":
    app.run(port=5000, debug=True)




