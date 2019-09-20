# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:28:02 2019

@author: Brianzhu
"""

import jenkins

jenkins_server_url='http://jenkins.hub520.com:11880'
user_id='admin'
api_token='dec7fa94ca3941025947fb9e8edd4b9e'
server = jenkins.Jenkins(jenkins_server_url, user_id, api_token)
user = server.get_whoami()
version = server.get_version()

print 'Hello %s from Jenkins %s' % (user['fullName'], version)