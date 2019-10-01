mapinput = open("Divvy_Trips_2018_Q1.txt","r")  
# open and read contents of this file
mapoutput = open("PreethamMapperOutput.txt","w")
 # open and write into this file
for line in mapinput:  
    data = line.strip().split(",") 
    if len(data)>12:
        if ".00" in data[5]:
            data[4]=int(float((data[4][1:]+data[5][:-1])))
            del data[5]
            
        elif ".00" in data[6]:
            data[4]=int(float((data[4][1:]+data[5]+data[6][:-1])))
            del data[5]
            del data[5]
       
    
    trip_id,start_time,end_time,bikeid,tripduration,from_station_id,from_station_name,to_station_id,to_station_name,usertype,gender,birthyear = data
    mapoutput.write("{0}\t{1}\n".format(usertype,(tripduration)))
    # print("{0}\t{1}\n".format(usertype,(tripduration)))
mapinput.close()
mapoutput.close()
# Closing both the read only and write files.