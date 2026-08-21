gitignore = """
# Backups and temp files
backup-clean-*/
*.fixed
*.test
*.badchars.txt
*.fixed2
garbage.txt
__pycache__/
*.pyc
Portfolio_Content_Organizer.*
"""
with open('.gitignore', 'w', encoding='utf-8') as f:
    f.write(gitignore.strip())
print("Fixed .gitignore")
