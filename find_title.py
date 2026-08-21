import subprocess
out = subprocess.check_output(["git", "show", "HEAD:project.html"], encoding="utf-8")
for line in out.splitlines():
    if "ph-title" in line:
        print(line)
        break
