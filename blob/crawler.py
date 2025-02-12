import requests

def download_video(video_url, output_path):
    try:
        # 发送 GET 请求
        response = requests.get(video_url, stream=True)
        
        # 如果请求成功
        if response.status_code == 200:
            # 打开文件并写入下载的数据
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:  # 防止下载过程中产生空数据
                        f.write(chunk)
            print(f"Video downloaded successfully: {output_path}")
        else:
            print(f"Failed to retrieve video, HTTP status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # 视频文件的 URL
    video_url = 'http://localhost:5000/video'  # 替换成目标视频 URL
    
    # 本地保存的路径
    output_path = 'downloaded_video.mp4'
    
    # 下载视频
    download_video(video_url, output_path)
