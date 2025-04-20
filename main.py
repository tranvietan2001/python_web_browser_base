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