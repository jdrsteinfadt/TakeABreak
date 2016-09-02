import webbrowser
import time

total_breaks = 3
break_time = 2

print("This program started on "+time.ctime())

for i in range(1,total_breaks+1):
    time.sleep(break_time*60*60)
    print("Break number "+str(i)+" at "+time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=ZnHmskwqCCQ")
