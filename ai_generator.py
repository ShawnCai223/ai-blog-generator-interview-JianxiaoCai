import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_blog_post(keyword, seo_data):
    prompt = f"""
You are a professional content writer. Please write a blog post in HTML about the topic: "{keyword}".
Use the following SEO data to guide the writing:
- Search Volume: {seo_data['search_volume']}
- Keyword Difficulty: {seo_data['keyword_difficulty']}
- CPC: ${seo_data['avg_cpc']}

The blog post should:
- Have a main heading and multiple subheadings
- Include a short introduction and conclusion
- Mention 2–3 affiliate products, with placeholders {{AFF_LINK_1}}, {{AFF_LINK_2}}, etc.
- Be written in an informative yet casual tone

Output only the HTML content.
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    content = response.choices[0].message.content

    
    content = content.replace("{{AFF_LINK_1}}", "https://example.com/product1")
    content = content.replace("{{AFF_LINK_2}}", "https://example.com/product2")
    return content