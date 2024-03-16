import re

class Convert:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert(self):
        self.pretext = "#EXTINF:-1 group-title="
        content = []
        fw = open(self.output_file, 'w')
        fw.write("#EXTM3U\n")
        with open(self.input_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "#genre#" in line:
                    groupTitle = line.split(',')[0]
                    continue
                if "http" in line:
                    title = line.split(',')[0]
                    titleUrl = line.split(',')[1]
                buf = self.pretext + '"' + groupTitle + '"' + "," + title + "\n" + titleUrl
                #print(buf)
                fw.write(buf)

if __name__ == '__main__':
    convert = Convert('./tvlive/tvlive.txt', 'JNG.m3u')
    convert.convert()
    print("Done")
    exit(0)