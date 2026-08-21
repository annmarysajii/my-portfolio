import subprocess
out = subprocess.check_output(["git", "show", "HEAD~1:project.html"], encoding="utf-8")
printing = False
for line in out.splitlines():
    if "main.innerHTML =" in line:
        printing = True
    if printing:
        print(line.rstrip())
        if "</header>" in line:
            break
