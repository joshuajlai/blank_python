from datetime import datetime, timedelta
import time

seconds = 10
print("Waiting {} seconds".format(seconds))
start_time = datetime.now()

while (datetime.now() < start_time + timedelta(seconds=seconds)):
    print("waiting...")
    time.sleep(seconds/4)
print("Finished waiting")
