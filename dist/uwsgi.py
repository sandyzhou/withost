import os

def setup(dist, conf, apps):
	os.system('pip install uwsgi')

	#print 'generating %s (%s) ...' % (site_root, backend or 'UWSGI')
	#pwd = os.getcwd()
	#os.chdir(os.path.dirname(site_root))
	#os.system('django-admin.py startproject ' + main)
	#os.rename(main, os.path.basename(site_root))
	#os.chdir(pwd)

def remove(dist, conf, apps):
	pass
