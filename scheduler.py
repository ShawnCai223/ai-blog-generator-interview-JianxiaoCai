from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import os
from seo_fetcher import get_keyword_metrics
from ai_generator import generate_blog_post

def save_blog_to_file(keyword, content):
    filename = f"generated_{keyword.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    with open(filename, 'w') as f:
        f.write(content)
    print(f"[+] Blog post saved: {filename}")

def scheduled_job():
    keyword = "wireless earbuds"
    print(f"[{datetime.now()}] Generating blog for: {keyword}")
    seo = get_keyword_metrics(keyword)
    content = generate_blog_post(keyword, seo)
    save_blog_to_file(keyword, content)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduled_job, trigger='interval', days=1)
    scheduler.start()