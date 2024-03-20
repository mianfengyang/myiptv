#!/bin/zsh
# pull source tvbox txt
sourceGitDir=~/project/tvbox
destGitDir=~/project/myiptv
cd $sourceGitDir
git pull

# rsync tvlist.txt to myiptv
cd $destGitDir
if [[ -f yqiqtv.txt ]]:then
  rm -rf yqiqtv.txt
fi
wget -O yqiqtv.txt https://lqtv.github.io/m3u/tv.m3u 
#rsync -a $sourceGitDir/tvlive/tvlive.txt $destGitDir/tvlive/tvlive.txt
python convertToM3u.py
git add .
git commit -m "yqiqtv.m3u"
git push
