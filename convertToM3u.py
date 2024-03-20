import time
import requests




class Convert:
    def __init__(self, input_file, output_file,speed_file):
        self.input_file = input_file
        self.output_file = output_file
        self.speed_file = speed_file
        self.pretext = "#EXTINF:-1 group-title=\"收藏频道\""
        self.results = []
        self.ans = []
        self.channel_counters = {}
        self.speed = 0.5
        with open(self.input_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if '#genre#' in line:
                    continue
                if 'CCTV' in line or '第一财经' in line or '凤凰' in line:
                    self.results.append(line.strip().split(','))


    def test_stream_speed(self):
        error_channels = []
        for line in self.results:
            channel_name, channel_url = line
            try:
                response = requests.get(channel_url, stream=True, timeout=3)
                if response.status_code == 200:
                    file_size = 0
                    start_time = time.time()
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file_size += len(chunk)
                    response.close()
                    end_time = time.time()
                    response_time = end_time - start_time
                    download_speed = file_size / response_time / 1024
                    normalized_speed = download_speed / 1024  # 将速率从kB/s转换为MB/s
                    if normalized_speed > self.speed:
                        self.ans.append(f"{channel_name},{channel_url},{normalized_speed:.3f} MB/s\n")
                        print(f"可用频道：{len(self.ans)} , 网速：{normalized_speed:.3f} MB/s , 不可用频道：{len(error_channels)} 个 , 总频道：{len(self.results)} 个")
                    else:
                        error_channel = channel_name, channel_url
                        error_channels.append(error_channel)
                        print(f"可用频道：{len(self.ans)} , 网速：{normalized_speed:.3f} MB/s , 不可用频道：{len(error_channels)} 个 , 总频道：{len(self.results)} 个")
                else:
                    error_channel = channel_name, channel_url
                    error_channels.append(error_channel)
                    print(f"可用频道：{len(self.ans)} ,  不可用频道：{len(error_channels)} 个 , 总频道：{len(self.results)} 个")
            except Exception as e:
                error_channel = channel_name, channel_url
                error_channels.append(error_channel)
                print(f"可用频道：{len(self.ans)} ,  不可用频道：{len(error_channels)} 个 , 总频道：{len(self.results)} 个")
        

    def writeSpeedFile(self):
        self.ans.sort(key=lambda x: (x[0], -float(x[2].split()[0])))
        fw = open(self.speed_file, 'w')
        for line in self.ans:
            fw.write(line)
        fw.close()

    def convert(self):
        result_counter = 3
        fw = open(self.output_file, 'w')
        fw.write("#EXTM3U\n")
        
        for result in self.ans:
            title, titleUrl, speed = result
            if "CCTV13" in title or "第一财经" in title:
                if title in self.channel_counters:
                    if self.channel_counters[title] >= result_counter:
                        continue
                    else:
                        fw.write(f"{self.pretext},{title}\n")
                        fw.write(f"{titleUrl}\n")
                        self.channel_counters[title] += 1
                else:
                    fw.write(f"{self.pretext},{title}\n")
                    fw.write(f"{titleUrl}\n")
                    self.channel_counters[title] = 1
            else:
                continue
        fw.close()

if __name__ == '__main__':
    iptv_itvall_txt_file = './itv_results.txt'
    iptv_itvall_m3u_file = './itvall.m3u'
    iptv_jng_txt_file = './tvlive/tvlive.txt'
    iptv_jng_m3u_file = './jng.m3u'
    iptv_yq_txt_file = './yqiqtv.txt'
    iptv_yq_m3u_file = './yqiqtv.m3u'
    iptv_yq_speed_file = './yqiqtv_speed.txt'
  
    convert = Convert(iptv_yq_txt_file,iptv_yq_m3u_file,iptv_yq_speed_file)
   
    convert.test_stream_speed()
    convert.writeSpeedFile()
    convert.convert()
    print("Done")
    exit(0)