import subprocess
import sys 

result = subprocess.run(["python", "--version"], capture_output=True, text=True)

print(result)
print(type(result.stdout.strip()))


# Installer un librairieif 
#subprocess.run(["python", "-m", "pip","install","torch"])

subprocess.run([sys.executable, '-m', 'pip', 'uninstall', 'torch'])