
# auto_blog.py
# 📄 StackPress Styled Blog Generator

import os
from datetime import datetime

# Define example blog posts
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

# Rotate based on date
index = datetime.now().day % len(blog_posts)
post = blog_posts[index]

# Generate fully styled HTML
html = f"""<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>{post['title']}</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <meta name='description' content='AI-powered blog post on budgeting'>
    <link href='https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap' rel='stylesheet'>
    <style>
        body {{
            font-family: 'Inter', sans-serif;
            background: #f9fbfd;
            color: #1a1a2e;
            margin: 0;
            padding: 2rem;
        }}
        main {{
            max-width: 800px;
            margin: 2rem auto;
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0,0,0,0.05);
        }}
        h1 {{
            font-size: 1.8rem;
            color: #1a1a2e;
        }}
        p {{
            line-height: 1.6;
            margin-bottom: 1.2rem;
        }}
        a {{
            color: #0077cc;
            text-decoration: none;
            font-weight: 600;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
<main>
    <h1>{post['title']}</h1>
    <p>{post['content']}</p>
    <p><a href='/best-apps.html'>Compare the best budgeting tools →</a></p>
</main>
</body>
</html>"""

# Save to blog post file
filename = f"blog-post-{post['slug']}.html"
with open(filename, "w") as f:
    f.write(html)
print(f"✅ Created styled blog file: {filename}")

# Append link to blog.html if not already included
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
