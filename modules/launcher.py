import subprocess

def launch(profile_dir, osc, slot):
    cmd = [
      r'D:\SteamLibrary\steamapps\common\VRChat\launch.exe',
      '--no-vr',
      f'--appdata={profile_dir}',
      f'--osc={osc}',
      f'--profile={slot}'
    ]
    return subprocess.Popen(cmd)