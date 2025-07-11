# 📝 AI Blog Generator

A simplified AI-powered content generator built with Flask and OpenAI.  
Given a keyword, it performs mock SEO analysis and generates a blog post in HTML format using GPT models.  
It also supports daily scheduled post generation.

---
## 🎥 Demo Presentation

[![Demo Presentation](https://img.youtube.com/vi/Y5RJF4bPSbk/0.jpg)](https://www.youtube.com/watch?v=Y5RJF4bPSbk)

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **Flask** – REST API framework
- **OpenAI API** – For content generation
- **APScheduler** – For daily scheduled post creation
- **python-dotenv** – Environment variable handling

---

## 🚀 Setup & Run Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-blog-generator-interview-JianxiaoCai.git
cd ai-blog-generator-interview-JianxiaoCai
```

### 2. Create virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate     
pip install -r requirements.txt
```

### 3. Create .env file with your OpenAI API key

From https://platform.openai.com/docs/overview 

```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

### 4. Run the app
```bash
python app.py
```

---

### 5. API Endpoint

GET /generate?keyword=<your_keyword>

Example:
```bash
curl "http://127.0.0.1:5000/generate?keyword=wireless%20earbuds"
```

Returns:
```json
{
  "keyword": "...",
  "seo": {
    "search_volume": "...",
    "keyword_difficulty": "...",
    "avg_cpc": "..."
  },
  "content": "<!DOCTYPE html>...</html>"
}
```

### 6. Daily Blog Generation (Scheduler)

The app uses **APScheduler** to generate a blog post once every 24 hours.
- Default keyword: wireless earbuds
- Output is saved in the project root directory as: *generated_<YYYYMMDD_HHMM>.html*

You can test this manually by calling *scheduled_job()* inside *scheduler.py*.

### 7. Example Output

An example blog post is included here:
**example_wireless_earbuds.html**

This HTML was generated using actual GPT model output, with affiliate link placeholders replaced.

---

## 📝 Author

**Jianxiao Cai**

Mail: shawn.jx.cai@gmail.com

[LinkedIn](https://www.linkedin.com/in/jianxiao-shawn-cai/) | [GitHub](https://github.com/ShawnCai223/)