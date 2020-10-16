# Simple Python Hashing Socket Server/Client



# Introduction

This program is written to establish a server with the purpose of creating a hash of all received files, and subsequently send that
back to the client. 

This program was written and tested using python 3.7 on Windows 10 WSL (Windows Subsystem for Linux) Ubuntu and Ubuntu 18.04 LTS.

# Orientation

Within the directory exists 3 folders --
1. Client -- Client contains hashclient.py, used to send files to the server for hashing.
	a. 3 random test files are located in the directory. Feel free to delete these and use your own.
	b. If you desire to create random files for testing purposes, use the command "dd if=/dev/urandom of=file.bin bs=100000 count=100", changing the name of 
	   the output file "of" and the size in bytes "bs" to change the parameters of the file. The files present in the directory were made in this manner. 

2. Server -- Server contains 2 folders -- Localhost_Server and LAN_Server
	a. Localhost_Server is the most basic funtionality of this program, and can be used to establish a connection over "localhost" or 127.0.0.1. 
	b. LAN_Server contains two different implementations of the server
		1. hashserver1.py uses a socket implementation to retrieve the local ip address of the machine hosting the server, in order to serve functionality on a LAN.
		2. hashserver2.py will assign the ip address on the interface "eth0" as the ip address of the server, in order to serve functionality on a LAN.
			a. This can be changed by editing "eth0" to whatever Linux-based interface is desired by issuing the command "ip addr" at the terminal. 
			b. **NOTE** Before using this, it will be necessary to check what your default interface is and to edit the file to reflect **NOTE**
			
3. Windows_test - This directory contains files developed to be used at WSL and for other testing purposes, but contain the same functionality as other folders. The files in this folder 
		  retain the Windows-style return carriages and new lines (\r\n) that are absent in Linux (\n).


# Instructions


1. Start a server at the terminal (Server folder) by executing hashserver.py: "./hashserver.py"
	a. This takes an optional parameter (-p) used to specify a port number other than the default 2345.

2. Place the files desired for hash computation in the Client directory. Once all desired files are in the directory, open a new terminal window and execute 
   ./hashclient.py <ip address> (optional -p <port number>) <hash type> <files>...
	a. Required parameters are ip address, hash type, and one or more files separated by spaces in the Client directory.
	b. Port number is optional, and defaults to port 2345.
	c. Supported hash algorithms are sha1, md5, sha256, and sha512. 
	d. An example for the Localhost_Server is as follows:
		"./hashserver.py 127.0.0.1 md5 file1.bin file2.bin foo.bin"

3. The client will connect with the server, send all files and return the hashes followed by the file name of all files. 


# Troubleshooting 

1. Unable to execute file:
	a. If you are unable to execute the file, change permissions of the file to "chmod u+x <filename>"

2. Error reading newlines:
	a. If an error displays regarding the first line of the program displaying "cannot read #!/usr/bin/env python3\r", 2 options:
		1. Run an optional Linux package "dos2unix" on the file to set the appropriate formatting.
		2. open the file in vi, and in command mode, enter ":set ff=unix", followed by ":wq"

3. Error connecting:
	a. Occasionally, the server may not receive the files in the appropriate error during transmission. The easiest fix is to input CTRL^C to stop the server, and restart it. 


# Optional Linux Packages
1. dos2unix (for troubleshooting, not required)
