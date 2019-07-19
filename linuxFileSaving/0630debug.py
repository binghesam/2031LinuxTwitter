# 0630 simple test
import os
import sys
import time
python=sys.executable

# while True:
# 	print("restart")
# 	#os.execl(python,"python","OSDebugThreadFileSaveDirctoryTokenUpdateByHourEveryPeriodSavingStreamingAPIbyChangyiMaInOutPutAllShell.py","1")
# 	os.execl(python,"python","testPrintFOrOSDebug.py")
# 	print("*****currently out of the os.execl in the True while loop for testing****")
# 	#break


while True:
	print("restart")
	#buf=os.system(python+" "+"testPrintFOrOSDebug.py")
	buf=os.system(python+" "+"OSDebugThreadFileSaveDirctoryTokenUpdateByHourEveryPeriodSavingStreamingAPIbyChangyiMaInOutPutAllShell.py"+" "+str(sys.argv[1]))
	#time.sleep(1)
	print(buf)
	print("*****currently out of the os.execl in the True while loop for testing****")