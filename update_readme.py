import feedparser
import os

# URL of your VideoJIN RSS feed
RSS_URL = "https://videojin.com/api/v1/blog/rss"
BLOG_LIMIT = 5

def update_readme():
      print(f"Fetching feed from {RSS_URL}...")
      feed = feedparser.parse(RSS_URL)

    if not feed.entries:
              print("No entries found in feed. Checking if feed is accessible...")
              return

    posts = feed.entries[:BLOG_LIMIT]

    blog_list = "\n".join([f"- [{post.title}]({post.link}) - {post.published[:16]}" for post in posts])

    readme_path = "README.md"
    if not os.path.exists(readme_path):
              print("README.md not found!")
              return

    with open(readme_path, "r", encoding="utf-8") as f:
              content = f.read()

    # Look for these markers in your README to know where to insert
    start_marker = "<!-- BLOG-POST-LIST:START -->"
    end_marker = "<!-- BLOG-POST-LIST:END -->"

    if start_marker in content and end_marker in content:
              print("Updating README content...")
              new_content = content.split(start_marker)[0] + start_marker + "\n" + blog_list + "\n" + end_marker + content.split(end_marker)[1]
              with open(readme_path, "w", encoding="utf-8") as f:
                            f.write(new_content)
                        print("README.md updated successfully.")
else:
        print(f"Markers not found in README.md. Please add {start_marker} and {end_marker}")

if __name__ == "__main__":
      update_readme()
