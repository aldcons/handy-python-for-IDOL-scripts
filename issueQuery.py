#!/usr/local/bin/python3
#Script with function to issue a query and read the XML response

import urllib, urllib2
from xml.dom.minidom import parse, parseString
from StringIO import StringIO

queryHost = "HostName" #IDOL Query DAH port
queryPort = "9200" #IDOL query port number
secString= "If you use secrity info string to run queries enter in ere"

def query(host, port, action):
#Runs query and returns string
    try:
        fileIn = urllib.urlopen("http//" + host + ":" + port + "/action=" action)
    except:
        data = "Failed To Connect"
        message = "Host connection to " + host + ":"  + port + " has failed. Will Exit"
        print (message)
        exit()
    else:
        data = fileIn.read()
        fileIn.close()
    return data    

def buildQuery(host, port):
#Query Builder. Use this secion to build the required query
    action = "query&" + \
        "text=*&" + \
        "TotalResults=true&" + \
        "maxresults=10000&" + \
        "printfields=DREREFERENCE,FieldOne,FieldTwo&" + \
        "securityInfo=" + secString
    response = query(host, port, action)
    return response

if __name_ == '__main__':
    respString = buildQuery((queryHost, queryPort)
    domListResults = parseString(respString)
    hits = domListResults.getElementsByTagName('autn:totalhits')[0].firstChild.nodeValue
    print ("Found event count: %s", string(hits))
    
    
    
