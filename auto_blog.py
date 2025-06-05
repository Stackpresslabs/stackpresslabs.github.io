
import os
from datetime import datetime

# Define a list of example blog titles and content
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

# Pick post by day of the month
index = datetime.now().day % len(blog_posts)
post = blog_posts[index]

# Generate HTML content
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

# Save to file
filename = f"blog-post-{post['slug']}.html"
with open(filename, "w") as f:
    f.write(html)

# Append link to blog.html (naive append, ideally would use HTML parsing)
blog_link = f"<li><a href='{filename}'>{post['title']}</a></li>\n"

with open("blog.html", "a") as blogfile:
    blogfile.write(blog_link)
