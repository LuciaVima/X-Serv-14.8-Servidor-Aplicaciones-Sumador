#!/usr/bin/python
# -*- coding: utf-8 -*-
#Lucia Villa Martinez

import socket
import sys

class webApp:

	def parse(self, request):
		return None
	def process(self, parsedRequest):
		return ("200 OK", "<html><body><h1> It works! </h1></body></hmtl>")
	def __init__(self, hostname, port):
		mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		mySocket.bind((hostname, port))
		mySocket.listen(5)
		sumandouno = True
		while True:
			print 'Waiting for connections'
			(recvSocket, address) = mySocket.accept()
			print 'HTTP request received (going to parse ald process):'
			request = recvSocket.recv(2048)
			if sumandouno == True:
				sumandouno = False
				parsedRequest1 = self.parse(request)
				(returnCode, htmlAnswer) = self.process1(parsedRequest1)
			else:
				sumandouno = True
				segundo = self.parse(request)
				try:
					parsedRequest2 = int(parsedRequest1) + int(segundo)
				except ValueError:
					recvSocket.send("HTTP/1.1 200 OK\r\n\r\n")
					recvSocket.send("<html><body><h1> Reinicie la calculadora e introduzca numeros. Gracias. ")
					recvSocket.send("</h1></body></html>")
					recvSocket.send("\r\n")
					sys.exit(1)
				(returnCode, htmlAnswer) = self.process2(parsedRequest2)
			print 'Answering back...'
			recvSocket.send("HTTP/1.1" + returnCode + " \r\n\r\n" + htmlAnswer + "\r\n")
			recvSocket.close()

class calcuApp(webApp):

	def parse(self, request):
		numero = request.split()[1][1:]
		return numero

	def process1 (self, parsedRequest1):
		respuesta = '<html><body><h1>' + "Introduzca segundo sumando" + '</h1></body></html>'
		return ("200 OK", respuesta)

	def process2 (self, parsedRequest2):
		respuesta = '<html><body><h1>' + str(parsedRequest2) + '</h1></body></html>'
		return ("200 OK", respuesta)
	

if __name__ == "__main__":
	testWebApp = calcuApp("localhost", 1234)
