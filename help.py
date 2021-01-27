#!/usr/bin/env python
class Help():
 def __init__(self,key):
  self.name = "Help"
  self.key = key
  self.message = '========================================================================================== \n'+\
                 'Application show, modify, ldap attribute. \n'+\
                 '========================================================================================== \n'+\
                 'Parameters attribute and set value are set in the cfg file \n'+\
                 "\n"+\
                 '1) Show attribute by login \n'+\
                 'Example syntax: script --show -u user \n'+\
                 'script --show -u user \n'+\
                 "\n"+\
                 '2) Show attribute by number \n'+\
                 'Example syntax: script --show -n number \n'+\
                 'script --show -n id \n'+\
                 "\n"+\
                 '3) Modify attribute by login \n'+\
                 'Example syntax: script --edit -u user \n'+\
                 'script --edit -u user \n'+\
                 "\n"+\
                 '4) Modify attribute by number \n'+\
                 'Example syntax: script --edit -n number \n'+\
                 'script --edit -n number \n'+\
                 "\n"+\
                 '5) Modifying the attributes of all users by login or number file \n'+\
                 'Example syntax: script --all -u -n file \n'+\
                 'script --all -u file \n'+\
                 'script --all -n file \n'+\
                 "\n"
 def view_help(self):
  if self.key: print self.message
