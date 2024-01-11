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


# # Define a datetime object
# date_time_start = datetime(year=2023, month= 1, day=1, hour=00, minute=00, second=00)
# date_time_end = datetime(year=2024, month=1, day=1, hour=00, minute=00, second=00)

# # Convert to timestamp
# timestamp_start = convert_datetime_to_timestamp(year=2023, month= 1, day=1, hour=00, minute=00, second=00)
# timestamp_end = convert_datetime_to_timestamp(year=2024, month=1, day=1, hour=00, minute=00, second=00)

# print(f"Timestamp start: {timestamp_start}")
# print(f"Timestamp end: {timestamp_end}")
