import os, glob

workspace = r'c:\Users\spars\Music\RASHME'
html_files = glob.glob(os.path.join(workspace, '*.html'))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('href="rashme.ico"', 'href="rashme_nobg.ico"')
    content = content.replace('src="rashme.svg"', 'src="rashme_nobg.svg"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
