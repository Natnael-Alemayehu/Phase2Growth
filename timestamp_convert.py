from datetime import datetime

def convert_timestamp_to_datetime(timestamp_seconds):

    # Divide the timestamp by 1000 to convert it to seconds
    # timestamp_seconds /= 1000
    
    # Convert the timestamp to a datetime object
    date_time = datetime.fromtimestamp(timestamp_seconds)
    
    # Return the formatted date and time
    return date_time.strftime('%Y-%m-%d %H:%M:%S')

# print("From :" + convert_timestamp_to_datetime(1592409758 ))
# print("To :"+convert_timestamp_to_datetime(1592496567 ))



def convert_datetime_to_timestamp(year, month, day, hour, minute, second):
  date_time = datetime( year, month, day, hour, minute, second)
  # Get the timestamp as seconds
  timestamp_seconds = date_time.timestamp()
  # Return the timestamp
  return int(timestamp_seconds)

# print(convert_datetime_to_timestamp(year=2023,month=1,day=2,hour=00,minute=00,second=00))
# print(convert_datetime_to_timestamp(year=2023,month=12,day=31,hour=23,minute=59,second=59))


# print(f"Timestamp start: {timestamp_start}")
# print(f"Timestamp end: {timestamp_end}")
