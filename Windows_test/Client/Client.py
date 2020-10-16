#!/usr/bin/env python3
import socket
import sys
import argparse
import os

#Create function to neatly send data to the server to be hashed
def filesend(hostname, portnumber, hash_type, filename):

    #create a TCP socket using IPv4
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Assign desired destination hostname and portnumber from passed in value from function.
    host = hostname
    port = portnumber

    #Use the connect function of the socket object to connect to remote server
    s.connect((host, port))

    #Determine size of the file using os function
    filesize = os.path.getsize(filename)

    #Use an understood separator to pass data in to single header
    separator = " "
    
    #Desired hashtype passed in through the function
    hashtype = hash_type

    #Use the socket object to send the header, comprised of the file size, file name, and hashtype to the server.
    s.send(f"{filesize}{separator}{filename}{separator}{hashtype}".encode()) 

    #Open the actual file in the same path in binary read mode, pass that data to the
    #sendfile function to send to the server. 
    data = open(filename, 'rb')
    s.sendfile(data)

    #Take data received from the server and place it into a variable.
    hashdata = s.recv(1024).decode()
    
    #Print the hashdata and filename.
    print(f"{hashdata}  {filename}")

    s.close()

if __name__ == "__main__":
    #import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('ip_address', type=str, help='Destination IP Address')
    parser.add_argument('-p', type=int, nargs='?', default=2345, help='Destination Port')
    parser.add_argument('hash_algorithm', type=str, help='Desired hashing algorithm')
    parser.add_argument('filename', type=str, nargs='+', help='Files to be hashed')
    args = parser.parse_args()
    
    print(f"Connecting to {args.ip_address}:{args.p}")

    #In main method, execute filesend() function i amount of times, with i being the amount of files
    #passed in as arguments at command line. 
    for i in range(0, len(args.filename)):
        filesend(args.ip_address, args.p, args.hash_algorithm, args.filename[i])
