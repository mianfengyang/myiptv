import subprocess
import re
import os

os.environ['no_proxy'] = '*'  # 禁用代理

def get_stream_resolution(m3u_url):
    # 使用 FFmpeg 获取视频流信息
    command = ['ffmpeg', '-i', m3u_url]
    result = subprocess.run(command, stderr=subprocess.PIPE)

    # 从输出中解析分辨率信息
    output = result.stderr.decode('utf-8')
    for line in output.split('\n'):
        if 'Video: ' in line:
            print(line)
            match = re.search(r'(h\d+|h\w+|vp9|mpeg).* (\d+)x(\d+)', line)
            #print(match)
            if match:
                code = match.group(1)
                width = match.group(2)
                height = match.group(3)
                #print(f"Resolution: {code}-{width}x{height}")
                if '1920' in width and 'h264' in code:
                    resolution = f"{code}-{width}x{height}"
                else:
                    resolution = None
            else:
                    resolution = None
    return resolution
# 测试 m3u 链接的视频流分辨率
m3u_url = "http://[2409:8087:7001:20:3::2]:80/dbiptv.sn.chinamobile.com/PLTV/88888888/224/3221226233/index.m3u8"#
get_stream_resolution(m3u_url)
