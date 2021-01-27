#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import check_output, CalledProcessError, STDOUT
import os
import cfg
import logger
import re

class Ldap():
        def __init__(self,host,port,user,password,dc,ou,filter_number,filter_name,ldapsearch,ldapmodify,grep,set):
                self.name = "Ldap"
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.dc = dc
		self.ou = ou
		self.filter_number = filter_number
		self.filter_name = filter_name
		self.ldapsearch = ldapsearch
		self.ldapmodify = ldapmodify
		self.grep = grep
		self.set = set
		self.file = 'modify.ldif'

	def search(self,key,user_number_file):
		obj_log = logger.Logger()
		obj_execude = Ldap(self.host,self.port,self.user,self.password,
			self.dc,self.ou,self.filter_number,self.filter_name,
			self.ldapsearch,self.ldapmodify,self.grep,self.set)
		if key == "-u":
			obj_execude.show_user(key,user_number_file)
		if key == "-n":
			obj_execude.show_number(key,user_number_file)

	def modify(self,key,user_number_file):
		obj_log = logger.Logger()
		obj_execude = Ldap(self.host,self.port,self.user,self.password,
                        self.dc,self.ou,self.filter_number,self.filter_name,
                        self.ldapsearch,self.ldapmodify,self.grep,self.set)
                if key == "-u":
                        obj_execude.modify_user(key,user_number_file)
                if key == "-n":
                        obj_execude.modify_number(key,user_number_file)

	def modify_cicle(self,key,user_number_file):
                obj_log = logger.Logger()
		obj_execude = Ldap(self.host,self.port,self.user,self.password,
                        self.dc,self.ou,self.filter_number,self.filter_name,
                        self.ldapsearch,self.ldapmodify,self.grep,self.set)
		os.system(r' >report')
		f = open(user_number_file)
		for line in f.readlines():
    			user_number_file = line.rstrip('\n')
			if key == "-u":
				str = re.findall(r"\D*",user_number_file)
				if str[0] != '':
                        		result = obj_execude.modify_user(key,user_number_file)
					obj_execude.report(user_number_file+' - '+result[0]+' - '+result[1])
				else:
					print(user_number_file+' invalid string format file')
                        		obj_log.loglogged(user_number_file+' invalid string format file')
					obj_execude.report(user_number_file+' - invalid string format file')
			if key == "-n":
				str = re.findall(r"\d*",user_number_file)
                                if str[0] != '':
                                        result = obj_execude.modify_number(key,user_number_file)
					print result
					obj_execude.report(user_number_file+' - '+result[0]+' - '+result[1])
                                else:
                                        print(user_number_file+' invalid string format file')
                                        obj_log.loglogged(user_number_file+' invalid string format file')
					obj_execude.report(user_number_file+' - invalid string format file')
		f.close()

	def show_user(self,key,user_number_file):
		obj_log = logger.Logger()
		host=port=user=password=dc=ou=filter_number=filter_name=ldapsearch=ldapmodify=grep=set="0"
                obj_execude = Ldap(host,port,user,password,dc,ou,filter_number,filter_name,ldapsearch,ldapmodify,grep,set)
		command=self.ldapsearch+' -w '+self.password+' -p '+self.port+' -h '+self.host+\
                                ' -b '+'"uid='+user_number_file+',ou='+self.ou+','+self.dc+'\"'+\
                                ' -s sub -x '+'\"('+self.filter_name+'=*)\"'+' '+self.filter_name
                success,output = obj_execude.command_execude(command)
                obj_log.loglogged(output)
                if success:
                	login = output[3].split(',')
                	login = login[0].split('=')
                	login = login[1]
                	index,atribut=10,''
                	obj_log.loglogged(login)
                	print('Results method show: '+user_number_file)
                	obj_log.loglogged('Results method show: ')
                        print(login)
                        while index<len(output):
                        	atribut = atribut+output[index]
                               	if output[index] == '':
                                	index=len(output)
                                index+=1
                       	check = obj_execude.atribute(self.filter_name,atribut)
			return check
                else:
                	print(output[10],output[11]+' Error connection ldap service')
                	obj_log.loglogged(output[10]+' Error connection ldap service')

	def show_number(self,key,user_number_file):
		obj_log = logger.Logger()
		obj_execude = Ldap(self.host,self.port,self.user,self.password,
                        self.dc,self.ou,self.filter_number,self.filter_name,
                        self.ldapsearch,self.ldapmodify,self.grep,self.set)
                command=self.ldapsearch+' -w '+self.password+' -p '+self.port+' -h '+self.host+\
                                ' -b '+'"ou='+self.ou+','+self.dc+'\"'+\
                                ' -s sub -x '+'\"('+self.filter_number+'='+user_number_file+')\"'+' '+self.filter_name
                success,output = obj_execude.command_execude(command)
                if success:
			output = output[9].split(',')
			uid = re.findall(r"dn: uid=",output[0])
			if not uid:
				print(user_number_file+' uid does not exist')
				obj_log.loglogged(user_number_file+' uid does not exist')
			elif uid[0] == "dn: uid=":
                        	login = re.findall(r"uid=(.*)",output[0])
				obj_execude.show_user('-u',login[0])
				return login[0]
                else:
                	print('Error connection ldap service')
                	obj_log.loglogged('Error connection ldap service')

	def modify_user(self,key,user_number_file):
                obj_log = logger.Logger()
		obj_execude = Ldap(self.host,self.port,self.user,self.password,
                        self.dc,self.ou,self.filter_number,self.filter_name,
                        self.ldapsearch,self.ldapmodify,self.grep,self.set)
		file = 'dn: uid='+user_number_file+','+'ou='+self.ou+','+self.dc+'\n'+\
			'changetype: modify'+'\n'+\
			'replace: '+self.filter_name+'\n'+\
			self.filter_name+': '+self.set
                command=self.ldapmodify+' -c -x -D cn='+self.user+' -w '+self.password+' -p '+self.port+' -h '+self.host+' -f '+self.file
		obj_execude.ldif(file)
                success,output = obj_execude.command_execude(command)
                if success:
                        print('Results method edit: ')
			print(output)
                        obj_log.loglogged('Results method edit: ')
			obj_log.loglogged(output)
			check = obj_execude.show_user(key,user_number_file)
			if check == self.set:
				print 'verification completed successfully'
				obj_log.loglogged('verification completed successfully')
				output[1] = 'verification completed successfully'
			return output
                else:
			print('Error connection ldap service')
			print(output[0],output[2])
                        obj_log.loglogged('Error connection ldap service '+output[0]+' '+output[2])
			alert = ['problem modify_user','verification failed']
			return alert

	def modify_number(self,key,user_number_file):
                obj_log = logger.Logger()
		obj_execude = Ldap(self.host,self.port,self.user,self.password,
                        self.dc,self.ou,self.filter_number,self.filter_name,
                        self.ldapsearch,self.ldapmodify,self.grep,self.set)
		login = obj_execude.show_number(key,user_number_file)
		if login == None:
			alert = ['uid does not exist','verification failed']
                        return alert
		if login != None:
			result = obj_execude.modify_user(key,login)
			return result

	def atribute(self,filter,atribut):
		obj_log = logger.Logger()
		atribut = atribut.split('\n')
		if filter == "DovecotAllowNets":
                	attr = re.findall(r"DovecotAllowNets",atribut[0])
                	if attr:
                		atribut = re.findall(r"DovecotAllowNets:(.*)$",atribut[0])
                        	atribut = atribut[0].split()
                        	atribut = ''.join(atribut)
				check = atribut
                        	atribut = atribut.split(',')
				print atribut
                        	obj_log.loglogged(atribut)
				return check
                	else:
                		print('no attribute')
                        	obj_log.loglogged('no attribute')
		else:
			print('attribute not supported')
                        obj_log.loglogged('attribute not supported')

	def command_execude(self,command):
                obj_log = logger.Logger()
                obj_log.loglogged('command_execude'+command)
                try:
                        output = check_output(command,stderr=STDOUT,shell=True)
                        success = True
                except CalledProcessError as err:
                        output = err.output
                        success = False
                output = output.split('\n')
                return success,output

	def ldif(self,code):
                obj_ldif = cfg.Configuration()
                file_path = obj_ldif.path+"/modify.ldif"
                file = open(file_path, 'w')
                data = str(code)
                file.write(data +"\n")
                file.close()

	def report(self,code):
		obj_rep = cfg.Configuration()
                file_path = obj_rep.path+"/report"
                file = open(file_path, 'a')
                data = str(code)
                file.write(data +"\n")
                file.close()
