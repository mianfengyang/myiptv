import re

class Convert:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert(self):
        self.pretext = "#EXTINF:-1 group-title="
        self.channel_counters = {}
        result_counter = 3
        fw = open(self.output_file, 'w')
        fw.write("#EXTM3U\n")
        with open(self.input_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "http" in line:
                    title = line.split(',')[0]
                    titleUrl = line.split(',')[1]

                    if "CCTV-13" in title or "凤凰" in title or "TVB" in title or "香港" in title:
                        if title in self.channel_counters:
                            if self.channel_counters[title] >= result_counter:
                                continue
                            else:
                                fw.write(f"#EXTINF:-1 group-title=\"收藏频道\",{title}\n")
                                fw.write(f"{titleUrl}\n")
                                self.channel_counters[title] += 1
                        else:
                            fw.write(f"#EXTINF:-1 group-title=\"收藏频道\",{title}\n")
                            fw.write(f"{titleUrl}\n")
                            self.channel_counters[title] = 1
                    else:
                        continue
if __name__ == '__main__':
    iptv_itvall_txt_file = './itv_results.txt'
    iptv_itvall_m3u_file = './itvall.m3u'
    iptv_jng_txt_file = './tvlive/tvlive.txt'
    iptv_jng_m3u_file = './jng.m3u'
    convert = Convert(iptv_jng_txt_file, iptv_jng_m3u_file)
    convert.convert()
    print("Done")
    exit(0)