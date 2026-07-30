import os
import glob

workspace = r'c:\Users\spars\Music\RASHME'

# HTML updates
html_files = glob.glob(os.path.join(workspace, '*.html'))

favicon_target = '<link rel="stylesheet" href="css/globals.css"/>'
favicon_repl = '<link rel="icon" type="image/x-icon" href="rashme.ico"/>\n  <link rel="stylesheet" href="css/globals.css"/>'

nav_logo_target = '<a href="index.html" class="navbar__logo"><span class="navbar__logo-text">RASHMÉ</span></a>'
nav_logo_repl = '<a href="index.html" class="navbar__logo"><img src="rashme.svg" alt="RASHMÉ Logo" class="navbar__logo-img"></a>'

footer_logo_target = '<div class="footer__logo">RASHMÉ</div>'
footer_logo_repl = '<img src="rashme.svg" alt="RASHMÉ Logo" class="footer__logo-img">'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(favicon_target, favicon_repl)
    content = content.replace(nav_logo_target, nav_logo_repl)
    content = content.replace(footer_logo_target, footer_logo_repl)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {os.path.basename(filepath)}")

# Navbar CSS update
nav_css_path = os.path.join(workspace, 'css', 'navbar.css')
with open(nav_css_path, 'r', encoding='utf-8') as f:
    nav_content = f.read()

nav_css_target = """/* Logo */
.navbar__logo-text {
  font-family: var(--font-serif);
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--black);
  transition: opacity var(--transition-fast);
}
.navbar__logo:hover .navbar__logo-text { opacity: 0.7; }"""

nav_css_repl = """/* Logo */
.navbar__logo-img {
  height: 28px;
  width: auto;
  display: block;
  transition: opacity var(--transition-fast);
}
.navbar__logo:hover .navbar__logo-img { opacity: 0.7; }"""

if nav_css_target in nav_content:
    nav_content = nav_content.replace(nav_css_target, nav_css_repl)
    with open(nav_css_path, 'w', encoding='utf-8') as f:
        f.write(nav_content)
    print("Updated navbar.css")
else:
    print("Could not find target in navbar.css")

# Footer CSS update
footer_css_path = os.path.join(workspace, 'css', 'footer.css')
with open(footer_css_path, 'r', encoding='utf-8') as f:
    footer_content = f.read()

footer_css_target = """.footer__logo {
  font-family: var(--font-serif);
  font-size: 1.8rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--beige);
  margin-bottom: 0.75rem;
}"""

footer_css_repl = """.footer__logo-img {
  height: 38px;
  width: auto;
  display: block;
  margin-bottom: 1rem;
  filter: invert(1) opacity(0.85);
}"""

if footer_css_target in footer_content:
    footer_content = footer_content.replace(footer_css_target, footer_css_repl)
    with open(footer_css_path, 'w', encoding='utf-8') as f:
        f.write(footer_content)
    print("Updated footer.css")
else:
    print("Could not find target in footer.css")

print("All updates applied successfully.")
