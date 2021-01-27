#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Configuration:
 def __init__(self):
  self.path = " "
  self.ldap_host = "host.domain.ru"
  self.ldap_port = "389"
  self.ldap_user = "dirman"
  self.ldap_password = "password"
  self.ldap_dc = "dc=domain,dc=ru"
  self.ldap_ou = "People"
  self.filter_number = "employeeNumber"
  self.filter_name = "DovecotAllowNets"
  self.ldapsearch = "/usr/bin/ldapsearch"
  self.ldapmodify = "/usr/bin/ldapmodify"
  self.grep = "/bin/grep"
  self.ldap_set = "ip and networks"
