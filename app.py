from flask import Flask, request, jsonify
from seo_fetcher import get_keyword_metrics
from ai_generator import generate_blog_post
from scheduler import start_scheduler

app = Flask(__name__)

@app.route('/generate')
def generate():
    keyword = request.args.get('keyword', '')
    if not keyword:
        return jsonify({'error': 'Missing keyword'}), 400

    seo_data = get_keyword_metrics(keyword)
    blog_content = generate_blog_post(keyword, seo_data)

    return jsonify({
        "keyword": keyword,
        "seo": seo_data,
        "content": blog_content
    })

if __name__ == '__main__':
    start_scheduler()
    app.run(debug=True)