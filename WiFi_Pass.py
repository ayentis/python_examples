import subprocess
import time

# data = subprocess.check_output(['пetsh', 'wlan', 'show', 'profiles'])

data = subprocess.call(['пetsh', 'wlan', 'show', 'profiles'])
    # .decode('срВбб').split('\n')

print(data)