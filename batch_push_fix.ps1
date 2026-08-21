git config --global user.name "Annmary Saji"
git config --global user.email "annie10302004@gmail.com"

git add .gitignore
git commit -m "Fix .gitignore corruption"
git push origin main

$folders = Get-ChildItem -Path "assets/portfolio-data" -Directory
foreach ($folder in $folders) {
    Write-Host "Pushing $($folder.Name)..."
    git add "assets/portfolio-data/$($folder.Name)"
    git commit -m "Upload asset batch: $($folder.Name)"
    git push origin main
}
Write-Host "All batches pushed successfully."
