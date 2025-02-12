from flask import Flask, Response, send_file, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def stream_video():
    # 请自行找一个mp4视频文件，放在当前目录下（即与main.py同一个目录）
    video_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'spiderbuf.mp4') # 这里替换为你的视频文件路径
    print(video_path)
    if not os.path.exists(video_path):
        return "Video not found", 404
    
    # 打开视频文件，以二进制流的形式发送
    def generate_video():
        with open(video_path, 'rb') as f:
            while chunk := f.read(1024 * 1024):  # 每次读取 1MB
                yield chunk

    return Response(generate_video(), content_type='video/mp4')


if __name__ == '__main__':
    app.run(debug=True)
