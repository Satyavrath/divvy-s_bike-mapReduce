input_mapper = open("../data/Divvy_Trips_2018_Q1.txt","r") 
output_mapper = open("output_mapper.txt","w")
for line in input_mapper:
    data = line.strip().split(',')
    if (len(data) == 12):
        trip_id, start_time, end_time, bikeid, tripduration, from_station_id, from_station_name, to_station_id, to_station_name, usertype, gender, birthyear = data
        output_mapper.write(usertype+","+birthyear+"\n")
        print(usertype+","+birthyear+"\n")
input_mapper.close()
output_mapper.close()