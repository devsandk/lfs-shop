import os,sys
import django.core.handlers.wsgi
apache_configuration = os.path.dirname(__file__)
lfs_project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(lfs_project)
sys.path.append(workspace)
sys.path.append('/usr/lib/python2.7/dist-packages/')
sys.path.append('/home/arkusc/lfs-installer/lfs_project')
os.environ['DJANGO_SETTINGS_MODULE']='lfs_project.settings'
application = django.core.handlers.wsgi.WSGIHandler()
