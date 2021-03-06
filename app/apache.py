#!/usr/bin/python

import os
from dist import website

def setup(dist, apps, conf):
	owner = os.getlogin()

	for site in conf['web.site'].split():
		site_info = site.split('@')
		server_name = site_info[0]
		if len(site_info) > 1:
			backend = site_info[1]
		else:
			backend = None
		website.add_site(dist, 'apache', server_name, owner, backend)
		print

def remove(dist, apps, conf):
	for site in conf['web.site'].split():
		server_name = site.split('@')[0]
		website.del_site(dist, 'apache', server_name)
