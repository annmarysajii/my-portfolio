import subprocess
out = subprocess.check_output(["git", "show", "HEAD:project.html"], encoding="utf-8")
for i, line in enumerate(out.splitlines()):
    if "p.tools" in line or "tools" in line:
        if "main.innerHTML" in line or "innerHTML" in out.splitlines()[i-2:i+2]:
            continue
        print(line.strip())
