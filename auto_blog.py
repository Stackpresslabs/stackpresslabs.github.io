
# auto_blog.py
# 🔄 StackPress Auto Blog Generator
# This script picks a blog idea, generates an HTML file, and updates blog.html.

import os
from datetime import datetime

# Step 1: Define some example blog posts
blog_posts = [
    {
        "title": "How to Start Budgeting on a Low Income",
        "slug": "budgeting-low-income",
        "content": "Budgeting on a low income is possible when you prioritize essentials and automate small savings. Use tools like YNAB or Monarch to track everything and stick to your plan."
    },
    {
        "title": "5 Budgeting Mistakes You Might Be Making",
        "slug": "budgeting-mistakes",
        "content": "Common mistakes include not tracking spending, setting unrealistic goals, and not automating bills. Learn how to avoid these pitfalls and gain control of your money."
    },
    {
        "title": "Budgeting Tools That Actually Work in 2025",
        "slug": "best-budget-tools-2025",
        "content": "Explore apps like YNAB, Monarch, and Goodbudget to see which one fits your lifestyle. We break down the pros and cons in our top picks."
    }
]

# Step 2: Pick one based on the day (rotate posts daily)
index = datetime.now().day % len(blog_posts)
post = blog_posts[index]

# Step 3: Generate HTML content using post data
html = f"""<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>{post['title']}</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link href='https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap' rel='stylesheet'>
    <style>
        body {{ font-family: 'Inter', sans-serif; background: #f9fbfd; color: #1a1a2e; padding: 2rem; }}
        main {{ max-width: 800px; margin: auto; background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 0 12px rgba(0,0,0,0.05); }}
        h1 {{ color: #1a1a2e; }}
    </style>
</head>
<body>
<main>
    <h1>{post['title']}</h1>
    <p>{post['content']}</p>
    <p><a href='/best-apps.html'>Compare budgeting apps →</a></p>
</main>
</body>
</html>"""

# Step 4: Save post as a new HTML file
filename = f"blog-post-{post['slug']}.html"
with open(filename, "w") as f:
    f.write(html)
print(f"✅ Created blog file: {filename}")

# Step 5: Append a link to blog.html (skip if already exists)
link_line = f"<li><a href='{filename}'>{post['title']}</a></li>\n"

if os.path.exists("blog.html"):
    with open("blog.html", "r") as bf:
        current_content = bf.read()

    if post['title'] not in current_content:
        with open("blog.html", "a") as bf:
            bf.write(link_line)
        print("✅ Link added to blog.html")
    else:
        print("ℹ️ Blog post already exists in blog.html")
else:
    print("⚠️ blog.html not found in the repo root. Make sure it's uploaded.")
