for filename in ['index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    foolproof_css = """
<style>
/* ABSOLUTE FOOLPROOF AWARDS FIX */
.awards {
    background: #0D0C11 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    padding: 30px !important;
    border-radius: 16px !important;
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    height: auto !important;
    min-height: 200px !important;
}
.awards-h {
    color: #FFFFFF !important;
    font-size: 24px !important;
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
}
.aw {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
}
.aw-n {
    color: #FFFFFF !important;
    font-size: 18px !important;
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
}
.aw-t {
    color: #AAAAAA !important;
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
}
.aw-i {
    color: #FFFFFF !important;
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
}
</style>
"""
    
    html = html.replace('</body>', foolproof_css + '\n</body>')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
print("Injected foolproof CSS into index!")
