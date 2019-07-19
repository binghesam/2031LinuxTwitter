# # 0630 simple test
# import os
# import sys
# import time
# python=sys.executable

# # while True:
# # 	print("restart")
# # 	#os.execl(python,"python","OSDebugThreadFileSaveDirctoryTokenUpdateByHourEveryPeriodSavingStreamingAPIbyChangyiMaInOutPutAllShell.py","1")
# # 	os.execl(python,"python","testPrintFOrOSDebug.py")
# # 	print("*****currently out of the os.execl in the True while loop for testing****")
# # 	#break


# while True:
# 	print("restart")
# 	#buf=os.system(python+" "+"testPrintFOrOSDebug.py")
# 	buf=os.system(python+" "+"KillProcessOSDebugThreadFileSaveDirctoryTokenUpdateByHourEveryPeriodSavingStreamingAPIbyChangyiMaInOutPutAllShell.py"+" "+str(sys.argv[1]))
# 	#time.sleep(1)
# 	print(buf)
# 	print("*****currently out of the os.execl in the True while loop for testing****")

import os
import sys
import time
import subprocess
import signal


# ###########in windows testing for the whole file
# while True: 
# 	print("restart")
# 	argument=str(sys.argv[1])
# 	print("1")
# 	#proc=subprocess.Popen(['python', "testPrintFOrOSDebug.py", argument], shell=True)
# 	proc=subprocess.Popen(['python', "KillProcessOSDebugThreadFileSaveDirctoryTokenUpdateByHourEveryPeriodSavingStreamingAPIbyChangyiMaInOutPutAllShell.py", argument], shell=True)
# 	print("*****currently out of the os.execl in the True while loop for testing****")
	
# 	#use the terminate to stop the process
# 	time.sleep(10)	
# 	print("2")
# 	#proc.terminate() #use it cannot stop the processing in testing
# 	#proc.kill() #i use it but, seems like that,it cannot kill the process.

# 	subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=proc.pid)) ##thsi file test successfully in the windows.
# 	#form the stack over flow reading ,we can get this .https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true
# 	# the commend is still running,then ,we should try another.

# 	#use the kill to stop something
# 	# time.sleep(15)
# 	# print("2")
# 	# pid=proc.pid
# 	# os.system("kill -9 {0}".format(pid))


# 	####debugging final showing
# 	print("finish termination")

########### this is in linux file
while True: 
	print("restart")
	argument=str(sys.argv[1])
	print("1")
	#proc=subprocess.Popen(['python', "testPrintFOrOSDebug.py", argument], shell=True)
	#proc=subprocess.Popen(['python', "KillProcessOSDebugThreadFileSaveDirctoryTokenUpdateByHourEveryPeriodSavingStreamingAPIbyChangyiMaInOutPutAllShell.py", argument], shell=True)
	# The os.setsid() is passed in the argument preexec_fn so
	# it's run after the fork() and before  exec() to run the shell.
	#python=sys.executable
	#cmd=[python, "python","KillProcessOSDebugThreadFileSaveDirctoryTokenUpdateByHourEveryPeriodSavingStreamingAPIbyChangyiMaInOutPutAllShell.py", argument]
	pro = subprocess.Popen('python'+" "+"KillProcessOSDebugThreadFileSaveDirctoryTokenUpdateByHourEveryPeriodSavingStreamingAPIbyChangyiMaInOutPutAllShell.py"+" "+argument, stdout=subprocess.PIPE, 
                       shell=True, preexec_fn=os.setsid) 

	print("*****currently out of the os.execl in the True while loop for testing****")
	
	#use the terminate to stop the process
	time.sleep(60)	
	print("2")
	os.killpg(os.getpgid(pro.pid), signal.SIGTERM)  # Send the signal to all the process groups
	#proc.terminate() #use it cannot stop the processing in testing
	#proc.kill() #i use it but, seems like that,it cannot kill the process.

	#use the kill to stop something
	# time.sleep(15)
	# print("2")
	# pid=proc.pid
	# os.system("kill -9 {0}".format(pid))


	####debugging final showing
	print("finish termination")