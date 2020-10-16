#!/usr/bin/env python3
import socketserver
import sys
import os
import hashlib
import argparse

#Define handler class for server, inheriting from the StreamRequestHandler for use of file read/write
class TCPHandler(socketserver.StreamRequestHandler):
       
    #Implement functionality of handle to retrieve data and create a hash of the data
    def handle(self):
        sep = " "

        #place file information in header variable so server knows how much data to expect
        #and what hash algorithm to use
        self.header = self.request.recv(2048).strip().decode()

        #Split the header object and place the appropriate data in its categories
        self.filesize, self.filename, self.hashtype = self.header.split(sep)
        print(f"Filesize: {self.filesize} Filename: {self.filename} Hashtype: {self.hashtype}")

        #Create new hashlibrary of user specified hash
        h = hashlib.new(self.hashtype)

        #Receive data from the client, specifying the size of the file retrieved from the header.
        self.data = self.rfile.read(int(self.filesize))
            
        #Create hash of data using the hashlibrary object
        h.update(self.data)

        #Place the value of the filehash in new property of the self object
        self.filehash = h.hexdigest()
        #print(f"{self.client_address[0]} wrote: {self.filehash}")

        #Send the filehash back to the client.
        self.wfile.write(self.filehash.encode())
        

if __name__ == "__main__":
    import argparse
    import socket
    
    #Create parser object to retrieve commandline arguments
    parser = argparse.ArgumentParser()
    #Create optional argument for port number, default 2345 for server
    parser.add_argument('-p', type=int, nargs='?', default=2345, help='Destination Port')
    args = parser.parse_args()

    #set host and port number to localhost and argument specified port number
    HOST = "localhost"
    PORT = args.p

    print(f"Starting server as {HOST}:{PORT}")
    #create TCPServer object using the handler defined above. Serve forever or until interrupted with CTRL^C
    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        server.serve_forever()