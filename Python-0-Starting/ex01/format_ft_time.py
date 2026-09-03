import time
from datetime import datetime

timestamp = time.time()

print("Seconds since January 1, 1970: ", end="")
print(f"{timestamp:,.4f} or {timestamp:.2e} in scientific notation")

date = datetime.fromtimestamp(timestamp)
print(date.strftime("%b %d %Y"))
