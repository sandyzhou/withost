#!/usr/bin/python

import os
import shutil

def setup(dist, apps, conf):
	src = '/etc/samba/smb.conf'
	dst = '/tmp/smb.conf'
	pub = conf['pub.path']

	# if os.path.exists(pub):
	# 	os.mkdirs(pub)

	fsrc = open(src)
	fdst = open(dst, 'w+')

	for line in fsrc:
		entry = line.split('=')
		if entry[0].strip() == '[pub]':
			#print src + ' leave unchanged'
			fsrc.close()
			fdst.close()
			return

		fdst.write(line)

	fdst.write('\n[pub]\n')
	for (key, value) in [('comment', 'Public Stuff'), ('path', pub), ('public', 'yes'), ('writable', 'no'), ('browseable', 'yes')]:
		fdst.write('\t%s = %s\n' % (key, value))

	fsrc.close()
	fdst.close()

	shutil.copyfile(dst, src)
