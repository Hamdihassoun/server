import subprocess
result = subprocess.run("dir *.py",shell=True,capture_output=True,universal_newlines=True)
print(result.stdout)