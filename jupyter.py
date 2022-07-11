import os
import sys
import subprocess

base = 'D:\\Pyenv'
jupyter_dir = os.path.join(base,'.jupyter')
if not os.path.exists(jupyter_dir):
  os.mkdir(jupyter_dir)
_dir = ""

dirs = {'JUPYTER_CONFIG_DIR' : jupyter_dir, 'JUPYTER_RUNTIME_DIR' : os.path.join(jupyter_dir,'runtime'),'JUPYTER_DATA_DIR' : os.path.join(jupyter_dir,'data')}

if sys.version_info < (3, 5):
	for k,v in dirs.iteritems():
		if not os.path.exists(v):
			os.mkdir(v)
		os.environ[k] = v
	_dir = "D:\\Pyenv\\py2\\Scripts\\jupyter-notebook.exe"
else:
	for k,v in dirs.items():
		if not os.path.exists(v):
			os.mkdir(v)
		os.environ[k] = v
	_dir = "D:\\Pyenv\\ml3\\Scripts\\jupyter-notebook.exe"

ipython_dir = os.path.join(base,'.ipython')
os.environ['IPYTHONDIR'] = ipython_dir

subprocess.call([_dir])