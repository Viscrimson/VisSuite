import os, subprocess

def ensure_link(src, dst):
    if not os.path.islink(src):
        subprocess.run(['rmdir','/s','/q', src], shell=True)
        subprocess.run(['mklink','/J', src, dst], shell=True)