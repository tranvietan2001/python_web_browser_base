# from flask import Flask, request, render_template_string
# import requests
# from bs4 import BeautifulSoup

# app = Flask(__name__)

# # Trang HTML đơn giản
# HTML_TEMPLATE = '''
# # <!doctype html>
# # <html lang="en">
# # <head>
# #     <meta charset="UTF-8">
# #     <meta name="viewport" content="width=device-width, initial-scale=1.0">
# #     <title>Simple Browser</title>
# #     <style>
# #         body { font-family: Arial, sans-serif; }
# #         pre { background: #f4f4f4; padding: 10px; border-radius: 5px; }
# #     </style>
# # </head>
# # <body>
# #     <h1>Simple Browser</h1>
# #     <form method="POST">
# #         <label for="url">Nhập URL:</label>
# #         <input type="text" id="url" name="url" required>
# #         <select name="method">
# #             <option value="GET">GET</option>
# #             <option value="POST">POST</option>
# #             <option value="HEAD">HEAD</option>
# #         </select>
# #         <button type="submit">Gửi</button>
# #     </form>
# #     {% if result %}
# #         <h2>Kết quả:</h2>
# #         <h3>Nội dung HTML:</h3>
# #         <div style="border: 1px solid #ccc; padding: 10px; border-radius: 5px; overflow: auto;">
# #             {{ result|safe }}
# #         </div>
# #     {% endif %}
# #     {% if stats %}
# #         <h2>Thông tin phân tích:</h2>
# #         <p>Chiều dài HTML: {{ stats.length }} ký tự</p>
# #         <p>Số thẻ <p>: {{ stats.p_count }}</p>
# #         <p>Số thẻ <div>: {{ stats.div_count }}</p>
# #         <p>Số thẻ <span>: {{ stats.span_count }}</p>
# #         <p>Số thẻ <img>: {{ stats.img_count }}</p>
# #     {% endif %}
# # </body>
# # </html>
# '''

# def analyze_html(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     return {
#         'length': len(html),
#         'p_count': len(soup.find_all('p')),
#         'div_count': len(soup.find_all('div')),
#         'span_count': len(soup.find_all('span')),
#         'img_count': len(soup.find_all('img'))
#     }

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     result = None
#     stats = None

#     if request.method == 'POST':
#         url = request.form['url']
#         method = request.form['method']

#         try:
#             if method == 'GET':
#                 response = requests.get(url)
#                 response.raise_for_status()  # Kiểm tra mã trạng thái
#                 result = response.text
#                 stats = analyze_html(result)

#             elif method == 'POST':
#                 response = requests.post(url)
#                 response.raise_for_status()  # Kiểm tra mã trạng thái
#                 result = response.text
#                 stats = analyze_html(result)

#             elif method == 'HEAD':
#                 response = requests.head(url)
#                 response.raise_for_status()  # Kiểm tra mã trạng thái
#                 result = response.headers  # Hiển thị thông tin tài nguyên

#         except requests.exceptions.RequestException as e:
#             result = f"Có lỗi xảy ra: {e}"

#     return render_template_string("index.html", result=result, stats=stats)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def analyze_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return {
        'length': len(html),
        'p_count': len(soup.find_all('p')),
        'div_count': len(soup.find_all('div')),
        'span_count': len(soup.find_all('span')),
        'img_count': len(soup.find_all('img'))
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    stats = None

    if request.method == 'POST':
        url = request.form['url']
        method = request.form['method']

        try:
            if method == 'GET':
                response = requests.get(url)
                response.raise_for_status()  # Kiểm tra mã trạng thái
                result = response.text
                stats = analyze_html(result)

            elif method == 'POST':
                response = requests.post(url)
                response.raise_for_status()  # Kiểm tra mã trạng thái
                result = response.text
                stats = analyze_html(result)

            elif method == 'HEAD':
                response = requests.head(url)
                response.raise_for_status()  # Kiểm tra mã trạng thái
                result = response.headers  # Hiển thị thông tin tài nguyên

        except requests.exceptions.RequestException as e:
            result = f"Có lỗi xảy ra: {e}"

    return render_template('index.html', result=result, stats=stats)

if __name__ == '__main__':
    app.run(debug=True)