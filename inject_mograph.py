import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Inject the text splitter JS
splitter_js = """
// Advanced Typography Mograph Splitter
document.querySelectorAll('.sec-title').forEach(title => {
  const text = title.textContent;
  title.innerHTML = '';
  title.classList.add('split-text');
  
  // Wrap each character
  [...text].forEach((char, i) => {
    const span = document.createElement('span');
    span.className = 'char';
    span.style.setProperty('--char-index', i);
    span.textContent = char;
    
    // Add hover listener specifically for the squash and stretch per letter
    span.addEventListener('mouseenter', () => {
      span.style.animation = 'none';
      span.offsetHeight; // trigger reflow
      span.style.animation = null;
      span.classList.add('hovered');
    });
    span.addEventListener('animationend', () => span.classList.remove('hovered'));
    
    title.appendChild(span);
  });
});
"""

# Place it right before </script> at the end
html = html.replace('</script>\n</body>', splitter_js + '\n</script>\n</body>')

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Injected text splitter JS for mograph")
