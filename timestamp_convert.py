from datetime import datetime

def convert_timestamp_to_datetime(timestamp_seconds):

    # Divide the timestamp by 1000 to convert it to seconds
    timestamp_seconds /= 1000
    
    # Convert the timestamp to a datetime object
    date_time = datetime.fromtimestamp(timestamp_seconds)
    
    # Return the formatted date and time
    return date_time.strftime('%Y-%m-%d %H:%M:%S')

print("Created at :" + convert_timestamp_to_datetime(1700210095800 ))
# print("Seen at :"+convert_timestamp_to_datetime(1655737569880 ))