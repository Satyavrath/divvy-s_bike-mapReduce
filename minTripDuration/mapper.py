import re
x = open("Divvy_Trips_2018_Q1.txt", 'r')

y = open("Mapperoutput.txt","w")
for line in x:
   a = re.search('.*(\".*\").*',line)
   if a:
    old = a.group(1)
      
    newA = a.group(1).replace(",", "")
    newB = newA.replace("\"", "")
    line = line.replace(old, newB)
   data = line.split(",")
   if len(data) == 12:
           trip_id,start_time,end_time,bikeid,tripduration,from_station_id,from_station_name,to_station_id,to_station_name,usertype,gender,birthyear = data
           y.write("{0}\t{1}\n".format(usertype,tripduration))
           print("{0}\t{1}\n".format(usertype,tripduration))
x.close()
y.close()