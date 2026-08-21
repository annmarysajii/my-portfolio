with open("diff.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if "ph-title" in line:
        for j in range(max(0, i-10), min(len(lines), i+10)):
            print(lines[j].rstrip())
        print("---")
