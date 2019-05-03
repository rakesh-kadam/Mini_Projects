import time
import webbrowser

total_break = 3
break_count = 0

print("This program started on " + time.ctime())
while( break_count < total_break):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=hC8CH0Z3L54&list=RDhC8CH0Z3L54&start_radio=1")ech
    break_count = break_count +1