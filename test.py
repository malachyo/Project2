#! /usr/bin/env python3
# Make an api call

######### install the needed modules ################################
import json, requests


########## url vars ################################################
def apiData(2018-11-1, 2018-11-1):
    api_token = "WPJuKHe98cuGr9O0O4u8V30CEjrT6sZoBFmfBpFs"
    url = "https://api.nasa.gov/neo/rest/v1/feed?"+start_date+"&"+end_date+"&api_key=WPJuKHe98cuGr9O0O4u8V30CEjrT6sZoBFmfBpFs"
    ########## call data ###############################################
    return url


#create an array of your parsed data variables

def apiCall(url):
    data = requests.get(url).json()
    information = data['near_earth_objects']['2018-11-01']

    dataArray = []
    for x in information:
      dataArray.append(x['name'])

    for x in information:
      dataArray.append(x['id'])

    for x in information:
        dataArray.append(x['is_potentially_hazardous_asteroid'])

    for x in information:
        dataArray.append(x['nasa_jpl_url'])


    # read out the data in your array

    ## Use string interpolation to create a unnique message #############
    msgName = dataArray[0]
    msgURL = dataArray[24]
    msgID = dataArray[8]
    msgDanger = dataArray[16]
    if msgDanger == True:
        msgDanger = "does"
    else:
        msgDanger = "doesn't"

    for parenth in '()':
        msgName = msgName.replace(parenth,'')

    print ("The name of the overhead asteroid is",msgName,"and has an ID number of",msgID,".")
    print (msgName,msgDanger,"pose an immediate threat.\n")

    learnMore = input("Would you like to learn more about the asteroid? (Y/N)\n")
    if learnMore == "Y":
        print(msgURL)
    else:
        print("Thank you for your time.")

apiData(symbol)
apiCall(url)


# print("Asteroid")
