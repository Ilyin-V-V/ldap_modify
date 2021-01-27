#!/usr/bin/env python
from time import sleep
import sys
import help
import cfg
import logger
import ldap

class Core(object):
 def __init__(self):
  self.name = "Core"
  self.num_param = len(sys.argv)
  self.action = ""
  self.key_u = "-u"
  self.user = ""
  self.key_n = "-n"
  self.number = ""
  self.file = "-f"
  self.help_param = 2
  self.work_param = 4
  self.stop = False

 def initialization_param(self,num_param,action,key_key,user_number_file):
  obj_initialization,obj_log = cfg.Configuration(),logger.Logger()
  if num_param == self.help_param and action == "-h":
  #help() method
   obj_initialization = help.Help(action)
   obj_initialization.view_help()
  elif num_param == self.work_param:
  #show(), edit(), all() method
  if action == "--show" or action == "--edit" or action == "--all":
   if key_key == "-u" or key_key == "-n":
    return action,key_key,user_number_file,self.stop
   else:
    self.stop=True
    obj_log.loglogged("Not parameter in "+action+
     " run with the -h key for help")
    print "Not parameter in",action," run with the -h key for help"
    return action,key_key,user_number_file,self.stop
  else:
   self.stop=True
   obj_log.loglogged("Not find action "+action+
    " run with the -h key for help")
   print "Not find action",action," run with the -h key for help"
   return action,key_key,user_number_file,self.stop

if __name__ == "__main__":
 obj_scripts,obj_conf,obj_log = Core(),cfg.Configuration(),logger.Logger()
 if (obj_scripts.num_param == obj_scripts.help_param):
  help_show = Core()
  help_show.action=str(sys.argv[1])
  key_key=user_number_file=None
  load_param = help_show.initialization_param(obj_scripts.num_param,
   help_show.action,key_key,user_number_file)
 elif (obj_scripts.num_param == obj_scripts.work_param):
  work_show_set = Core()
  work_show_set.action=str(sys.argv[1])
  work_show_set.key_key=str(sys.argv[2])
  work_show_set.user_number_file=str(sys.argv[3])
  action,key,user_number_file,stop = work_show_set.initialization_param(
   obj_scripts.num_param,work_show_set.action,
   work_show_set.key_key,work_show_set.user_number_file)
 if stop: exit()
  obj_ldap = ldap.Ldap(
  obj_conf.ldap_host,
  obj_conf.ldap_port,
  obj_conf.ldap_user,
  obj_conf.ldap_password,
  obj_conf.ldap_dc,
  obj_conf.ldap_ou,
  obj_conf.filter_number,
  obj_conf.filter_name,
  obj_conf.ldapsearch,
  obj_conf.ldapmodify,
  obj_conf.grep,
  obj_conf.ldap_set)
 if action == "--show":
  search = obj_ldap.search(key,user_number_file)
 if action == "--edit":
  modify = obj_ldap.modify(key,user_number_file)
 if action == "--all":
  modify = obj_ldap.modify_cicle(key,user_number_file)
 else:
  obj_log.loglogged('Not parameter, run with the -h key for help')
  print 'Not parameter, run with the -h key for help'
