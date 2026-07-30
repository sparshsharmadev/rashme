import os
import glob

workspace = r'c:\Users\spars\Music\RASHME'

# 1. Update the footer in all existing HTML files
html_files = glob.glob(os.path.join(workspace, '*.html'))
# Exclude brand.html as it's a standalone brand kit
html_files = [f for f in html_files if 'brand.html' not in f and 'legal_' not in f]

footer_replacement = """        <div class="footer__bottom-links">
          <a href="privacy.html">Privacy Policy</a>
          <a href="terms.html">Terms of Service</a>
          <a href="refund.html">Refund Policy</a>
        </div>"""

# Find an existing file to steal the navbar and footer from (e.g. index.html)
with open(os.path.join(workspace, 'index.html'), 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract Navbar
nav_start = index_content.find('<nav class="navbar">')
nav_end = index_content.find('</nav>', nav_start) + 6
navbar = index_content[nav_start:nav_end]

# Extract Footer (we'll replace the links in the extracted footer too)
footer_start = index_content.find('<footer class="footer">')
footer_end = index_content.find('</footer>', footer_start) + 9
footer_html = index_content[footer_start:footer_end]

# Update the footer HTML snippet with the new links
import re
footer_html = re.sub(
    r'<div class="footer__bottom-links">.*?</div>',
    footer_replacement,
    footer_html,
    flags=re.DOTALL
)

# Update all HTML files with the new footer links
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(
        r'<div class="footer__bottom-links">.*?</div>',
        footer_replacement,
        content,
        flags=re.DOTALL
    )
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated footer in {os.path.basename(filepath)}")

# 2. Create the 3 Legal Pages
template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — RASHMÉ</title>
  <link rel="icon" type="image/x-icon" href="rashme_nobg.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/globals.css">
  <link rel="stylesheet" href="css/navbar.css">
  <style>
    .legal-content {{ max-width: 800px; margin: 0 auto; padding-top: calc(var(--nav-h) + 4rem); padding-bottom: 4rem; min-height: 70vh; }}
    .legal-content h1 {{ font-family: var(--font-serif); font-size: 3rem; margin-bottom: 2rem; font-weight: 500; letter-spacing: -0.02em; }}
    .legal-content h2 {{ font-family: var(--font-serif); font-size: 1.5rem; margin-top: 3rem; margin-bottom: 1rem; color: var(--black); font-weight: 500; }}
    .legal-content p, .legal-content li {{ margin-bottom: 1rem; color: var(--muted); line-height: 1.8; }}
    .legal-content ul {{ margin-left: 1.5rem; margin-bottom: 1.5rem; }}
    .legal-content strong {{ color: var(--black); font-weight: 600; }}
  </style>
</head>
<body>
  {navbar}
  <main class="legal-content container reveal">
    <h1>{title}</h1>
    {content}
  </main>
  {footer}
  <script src="js/main.js"></script>
</body>
</html>"""

privacy_content = """
    <p>Last Updated: July 2026</p>
    <p>At RASHMÉ, we value your privacy and are committed to protecting your personal data. This Privacy Policy outlines how we collect, use, and safeguard your information when you visit our website or make a purchase.</p>
    
    <h2>1. Information We Collect</h2>
    <p>We collect personal information that you provide to us when you make a purchase, sign up for our newsletter, or contact us. This may include your name, email address, shipping address, and payment details.</p>
    
    <h2>2. How We Use Your Information</h2>
    <p>We use your information strictly to:</p>
    <ul>
        <li>Process and fulfill your orders.</li>
        <li>Send order confirmations and shipping updates.</li>
        <li>Communicate with you regarding customer support inquiries.</li>
        <li>Send marketing communications (only if you have opted in).</li>
    </ul>
    
    <h2>3. Data Protection</h2>
    <p>We implement a variety of security measures to maintain the safety of your personal information. All sensitive payment information is encrypted and transmitted via secure payment gateways. We do not store credit card details on our servers.</p>
    
    <h2>4. Third-Party Disclosure</h2>
    <p>We do not sell, trade, or otherwise transfer your personally identifiable information to outside parties, except trusted third parties who assist us in operating our website or servicing you, so long as those parties agree to keep this information confidential.</p>
    
    <h2>5. Contact Us</h2>
    <p>If you have any questions regarding this Privacy Policy, please contact us via our <a href="contact.html">Contact Page</a>.</p>
"""

terms_content = """
    <p>Last Updated: July 2026</p>
    <p>Welcome to RASHMÉ. By accessing or using our website, you agree to be bound by the following Terms of Service. Please read them carefully.</p>
    
    <h2>1. General Conditions</h2>
    <p>We reserve the right to refuse service to anyone for any reason at any time. You understand that your content (excluding credit card information) may be transferred unencrypted over various networks.</p>
    
    <h2>2. Products and Pricing</h2>
    <p>All descriptions of products and pricing are subject to change at any time without notice. We reserve the right to discontinue any product at any time. We have made every effort to display as accurately as possible the colors and images of our products.</p>
    
    <h2>3. Accuracy of Billing and Account Information</h2>
    <p>We reserve the right to refuse any order you place with us. In the event that we make a change to or cancel an order, we may attempt to notify you by contacting the e-mail and/or billing address provided at the time the order was made.</p>
    
    <h2>4. Medical Disclaimer</h2>
    <p>The products and claims made about specific products on or through this site have not been evaluated by the FDA or equivalent medical boards. Our products are not intended to diagnose, treat, cure, or prevent any disease. Always consult with a healthcare professional before starting any new cosmetic regimen.</p>
    
    <h2>5. Governing Law</h2>
    <p>These Terms of Service and any separate agreements whereby we provide you services shall be governed by and construed in accordance with the laws of our operating jurisdiction.</p>
"""

refund_content = """
    <p>Last Updated: July 2026</p>
    <p>We want you to be completely satisfied with your RASHMÉ purchase. If you are not entirely happy with your order, we are here to help.</p>
    
    <h2>1. Returns</h2>
    <p>You have <strong>14 days</strong> to return an item from the date you received it. To be eligible for a return, your item must be unused, in the same condition that you received it, and in the original packaging.</p>
    <p>To initiate a return, please contact our support team through the <a href="contact.html">Contact Page</a> with your order number and reason for return.</p>
    
    <h2>2. Refunds</h2>
    <p>Once we receive your item, we will inspect it and notify you that we have received your returned item. If your return is approved, we will initiate a refund to your original method of payment. You will receive the credit within a certain amount of days, depending on your card issuer's policies.</p>
    
    <h2>3. Shipping Costs</h2>
    <p>You will be responsible for paying for your own shipping costs for returning your item. Shipping costs are non-refundable. If you receive a refund, the cost of return shipping will be deducted from your refund.</p>
    
    <h2>4. Damaged or Defective Items</h2>
    <p>If you received a damaged or defective product, please notify us immediately for assistance. We will arrange for a replacement to be sent to you at no additional cost.</p>
"""

pages = {
    'privacy.html': ('Privacy Policy', privacy_content),
    'terms.html': ('Terms of Service', terms_content),
    'refund.html': ('Refund Policy', refund_content)
}

for filename, (title, content) in pages.items():
    filepath = os.path.join(workspace, filename)
    full_html = template.format(
        title=title,
        navbar=navbar,
        content=content,
        footer=footer_html
    )
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Created {filename}")

