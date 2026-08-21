import subprocess
out = subprocess.check_output(["git", "show", "HEAD:project.html"], encoding="utf-8")
printing = False
for line in out.splitlines():
    if "main.innerHTML =" in line:
        printing = True
    if printing:
        print(line.rstrip())
        if "</div>" in line and "proj-header" not in line and "dynamic-gallery" in line:
            break
