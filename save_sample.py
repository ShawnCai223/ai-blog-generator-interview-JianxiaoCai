result = {
    "content": """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Exploring the World of Wireless Earbuds</title>
</head>
<body>

<h1>The Ultimate Guide to Wireless Earbuds</h1>

<p>Welcome to our in-depth exploration of the wonderful world of wireless earbuds! With a search volume of 5400 and a keyword difficulty of 38, it's clear that these nifty gadgets are all the rage. In this blog post, we'll discuss everything you need to know about wireless earbuds, from how they work to the best ones on the market.</p>

<h2>How Do Wireless Earbuds Work?</h2>
<p>Wireless earbuds use Bluetooth technology to connect to your device without the need for any pesky cords. This allows for greater freedom of movement and a more convenient listening experience.</p>

<h2>Benefits of Using Wireless Earbuds</h2>
<p>One of the main advantages of wireless earbuds is their portability. You can easily toss them in your pocket or bag and take them with you wherever you go. They also provide a more streamlined look compared to traditional wired earphones.</p>

<h2>Top Wireless Earbud Picks</h2>
<p>Looking to upgrade your listening experience? Check out these top wireless earbud picks:</p>
<ol>
  <li><a href="{AFF_LINK_1}" target="_blank">Product 1</a></li>
  <li><a href="{AFF_LINK_2}" target="_blank">Product 2</a></li>
</ol>

<h2>Conclusion</h2>
<p>Wireless earbuds have revolutionized the way we listen to music on the go. With a search volume of 5400, it's clear that these tiny devices are here to stay. Whether you're working out at the gym or commuting to work, wireless earbuds are the perfect companion for all your audio needs.</p>

</body>
</html>""",
    "keyword": "wireless earbuds",
    "seo": {
        "search_volume": 5400,
        "keyword_difficulty": 38,
        "avg_cpc": 1.25
    }
}
# 1. 获取 HTML 内容
html = result["content"]

# 2. 替换占位链接
html = html.replace("{AFF_LINK_1}", "https://example.com/product1")
html = html.replace("{AFF_LINK_2}", "https://example.com/product2")

# 3. 保存为 HTML 文件
with open("example_wireless_earbuds.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ 成功写入 example_wireless_earbuds.html")