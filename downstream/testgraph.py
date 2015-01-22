import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import json
import datetime

TIMEFORMAT = "%Y-%m"

def main():
    fh = open("/Users/khigaki/massive-spice/data/output.json")
    totalData = json.load(fh)
    fh.close()
    includedStatus = {
        #'Negotiation/Review' : True,
        #'Interested Prospect' : True, 
        #'Stalled' : True, 
        #'Evaluation' : True, 
        #'Discovery' : True, 
        #'Prospecting' : True, 
        #'Initial_Opportunity' : True, 
        #'Solution' : True, 
        #'Contract' : True, 
        #'Value Proposition/Quote' : True, 
        #'Proposal_Development' : True, 
        #'Qualification' : True, 
        #'Negotiation' : True, 
        #'Verbal' : True, 
        #'Demo' : True, 
        #'Value Match' : True, 
        #'Proposal/Price Quote' : True
        #'Sales Ops Closed' : True, 
        #'Finance Closed' : True, 
        'Closed Won' : True, 
        'Closed Lost' : True, 
    }
    #countColumns = ["opportunity_type", "campaign_id", "lead_source", "currency_id", "next_step", "commit_stage"]
    #dateColumns = ["date_entered", "date_modified", "date_closed"]
    countColumns = ["campaign_id", "lead_source"]
    dateColumns = ["date_closed"]
    for status in totalData:
        try:
            includedStatus[status]
        except KeyError:
            continue
        count = totalData[status]['count']
        for column in countColumns:
            myData = totalData[status][column]
            processCount(status, column, myData, count)
        for column in dateColumns:
            myData = totalData[status][column]
#           processDate(status, column, myData, count)
            processCount(status, column, myData, count)

def processCount(status, column, myData, count):
    labels = []
    values = []
    i = 0
    for result in myData:
        if i >= 10:
            break
        labels.append(result[0])
        values.append(result[1])
        i += 1
    y_pos = range(len(labels))
    plt.barh(y_pos, values, align='center', alpha=0.4)
    plt.yticks(y_pos, labels)
    plt.xlabel('Count')
    plt.title('%s, %s top 10 counts. Total: %s' % (status, column, count))
    plt.show()

"""
def processDate(status, column, myData, count):
    minDate = myData[0][0]
    maxDate = myData[len(myData)-1][0]
    i = 0
    date = datetime.datetime.strptime(minDate, TIMEFORMAT)
    month = date.month
    year = date.year
    newDates = []
    newValues = []
    strDate = "%d-%s" % (year, str(month).zfill(2))
    while strDate != maxDate:
        strDate = "%d-%s" % (year, str(month).zfill(2))
        newDates.append(strDate)
        if myData[i][0] == strDate:
            newValues.append(myData[i][1])
            i += 1
        else:
            newValues.append(0)
        month += 1
        if month == 13:
            year += 1
            month = 1

    y_pos = range(len(newDates))
    plt.barh(y_pos, newValues, align='center', alpha=0.4)
    plt.yticks(y_pos, newDates)
    plt.xlabel('Count')
    plt.title('%s, %s datecount. Total: %s' % (status, column, count))
    plt.show()
"""

if __name__ == "__main__":
    main()
