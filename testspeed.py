import subprocess
import re

def test_video_stream_speed(url):
    try:
        # 使用ffmpeg获取视频流并输出到/dev/null，同时通过-preset ultrafast加速流的获取
        cmd = ['ffmpeg', '-i', url, '-f', 'null', '-preset', 'ultrafast', '-']
        process = subprocess.Popen(cmd, stderr=subprocess.PIPE)
        output, _ = process.communicate()
        output = output.decode('utf-8')

        # 从ffmpeg输出中提取视频流速度
        match = re.search(r'speed=([\d.]+)x', output)
        if match:
            speed = float(match.group(1))
            print(f"视频流速度: {speed}x")
        else:
            print("无法获取视频流速度")
    except Exception as e:
        print(f"发生异常: {e}")

if __name__ == "__main__":
    url = "http://115.171.86.183:9901/tsfile/live/16000_1.m3u8?key=txiptv&playlive=1&authid=0"
    test_video_stream_speed(url)