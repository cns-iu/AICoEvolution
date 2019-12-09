import csv

wosYears = {}
wosCitations = {}
AItoROB = {}
IOTtoAI = {}
ROBtoIOT = {}
ROBtoAI = {}
AItoIOT = {}
IOTtoROB = {}

Nodes = []
NodeDict = {}
Edges = []

with open('wos-keyword-author-year-tc-ALL-haici.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        wosID = str(row[0])
        year = str(row[3])
        wosYears[wosID] = year

with open('citation-alldata-limited.csv') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        if str(row[0]) != 'edge_id':
            #has_key is deprecated, switch to 'in' statements
            AIsource = int(row[5])
            AItarget = int(row[8])
            ROBsource = int(row[7])
            ROBtarget = int(row[10])
            IOTsource = int(row[6])
            IOTtarget = int(row[9])
            srcYear = wosYears[str(row[1])]
            trgYear = wosYears[str(row[2])]
            if ((AIsource == 1 and ROBtarget == 1)):
                if AItoROB.has_key((srcYear, trgYear)):
                    AItoROB[(srcYear, trgYear)] += 1
                else: AItoROB[(srcYear, trgYear)] = 1
            if ((ROBsource == 1 and IOTtarget == 1)):
                if ROBtoIOT.has_key((srcYear, trgYear)):
                    ROBtoIOT[(srcYear, trgYear)] += 1
                else: ROBtoIOT[(srcYear, trgYear)] = 1
            if ((IOTsource == 1 and AItarget == 1)):
                if IOTtoAI.has_key((srcYear, trgYear)):
                    IOTtoAI[(srcYear, trgYear)] += 1
                else: IOTtoAI[(srcYear, trgYear)] = 1
            if (ROBsource == 1 and AItarget == 1):
                if ROBtoAI.has_key((srcYear, trgYear)):
                    ROBtoAI[(srcYear, trgYear)] += 1
                else: ROBtoAI[(srcYear, trgYear)] = 1
            if (AIsource == 1 and IOTtarget == 1):
                if AItoIOT.has_key((srcYear, trgYear)):
                    AItoIOT[(srcYear, trgYear)] += 1
                else: AItoIOT[(srcYear, trgYear)] = 1
            if (IOTsource == 1 and ROBtarget == 1):
                if IOTtoROB.has_key((srcYear, trgYear)):
                    IOTtoROB[(srcYear, trgYear)] += 1
                else: IOTtoROB[(srcYear, trgYear)] = 1

for key, value in ROBtoIOT.iteritems():
    srcLon = (int(key[0]) - 1998) * 10
    trgLon = (int(key[1]) - 1998) * 10
    Nodes.append([len(Nodes) + 1, int(key[0]), 40, srcLon]) #Robot row
    Nodes.append([len(Nodes) + 1, int(key[1]), 20, trgLon]) #IoT row
    Edges.append([len(Nodes) - 1, len(Nodes), value])
for key, value in IOTtoROB.iteritems():
    srcLon = (int(key[0]) - 1998) * 10
    trgLon = (int(key[1]) - 1998) * 10
    Nodes.append([len(Nodes) + 1, int(key[0]), 20, srcLon]) #IoT row
    Nodes.append([len(Nodes) + 1, int(key[1]), 40, trgLon]) #ROB row
    Edges.append([len(Nodes) - 1, len(Nodes), value])
for key, value in AItoIOT.iteritems():
    srcLon = (int(key[0]) - 1998) * 10
    trgLon = (int(key[1]) - 1998) * 10
    Nodes.append([len(Nodes) + 1, int(key[0]), 60, srcLon]) #AI row
    Nodes.append([len(Nodes) + 1, int(key[1]), 20, trgLon]) #IoT row
    Edges.append([len(Nodes) - 1, len(Nodes), value])
for key, value in IOTtoAI.iteritems():
    srcLon = (int(key[0]) - 1998) * 10
    trgLon = (int(key[1]) - 1998) * 10
    Nodes.append([len(Nodes) + 1, int(key[0]), 20, srcLon]) #IoT row
    Nodes.append([len(Nodes) + 1, int(key[1]), 60, trgLon]) #AI row
    Edges.append([len(Nodes) - 1, len(Nodes), value])
for key, value in AItoROB.iteritems():
    srcLon = (int(key[0]) - 1998) * 10
    trgLon = (int(key[1]) - 1998) * 10
    Nodes.append([len(Nodes) + 1, int(key[0]), 60, srcLon]) #AI row
    Nodes.append([len(Nodes) + 1, int(key[1]), 40, trgLon]) #ROB row
    Edges.append([len(Nodes) - 1, len(Nodes), value])
for key, value in ROBtoAI.iteritems():
    srcLon = (int(key[0]) - 1998) * 10
    trgLon = (int(key[1]) - 1998) * 10
    Nodes.append([len(Nodes) + 1, int(key[0]), 40, srcLon]) #Robot row
    Nodes.append([len(Nodes) + 1, int(key[1]), 60, trgLon]) #AI row
    Edges.append([len(Nodes) - 1, len(Nodes), value])

for node in Nodes:
    NodeDict[node[0]] = node[2] # create dictionary of ID-Latitude pairs

with open('WOS_convergence_edges.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["source", "target", "weight", "cat"])
    for edge in Edges:
        if (NodeDict[edge[0]] == 20): # IoT
            edge.append(0)
            writer.writerow(edge)
        elif (NodeDict[edge[0]] == 40): # Robotics
            edge.append(1)
            writer.writerow(edge)
        else:                          # AI
            edge.append(2)
            writer.writerow(edge)

with open('WOS_convergence_nodes.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id", "label", "lat", "lon"])
    for node in Nodes:
        writer.writerow(node)


# print("AI->ROB: " + str(AItoROB))
# print("ROB->IOT: " + str(ROBtoIOT))
# print("IOT->AI: " + str(IOTtoAI))
# print("ROB->AI: " + str(ROBtoAI))
# print("AI->IOT: " + str(AItoIOT))
# print("IOT->ROB : " + str(IOTtoROB))
        
