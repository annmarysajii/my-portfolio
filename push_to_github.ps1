Write-Host "Starting batch upload to GitHub..."

git config --global user.name "Annmary Saji"
git config --global user.email "annie10302004@gmail.com"

# Push any existing commits first
git push origin main

$folders = Get-ChildItem -Path "assets/portfolio-data" -Directory
foreach ($folder in $folders) {
    Write-Host "Adding and pushing folder: $($folder.Name)..."
    git add "assets/portfolio-data/$($folder.Name)"
    # Check if there are changes to commit
    $status = git status --porcelain
    if ($status) {
        git commit -m "Upload asset batch: $($folder.Name)"
        git push origin main
    } else {
        Write-Host "No new files in $($folder.Name) to push."
    }
}
Write-Host "All assets pushed successfully! Press any key to exit..."
$Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
