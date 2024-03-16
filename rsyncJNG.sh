#!/bin/zsh
# pull source tvbox txt
sourceGitDir="~/project/tvbox"
destGitDir="~/project/myiptve"
cd $sourceGitDir
git pull

# rsync tvlist.txt to myiptv
cd $destGitDir
rsync -a $sourceGitDir/tvlive/tvlive.txt $destGitDir/tvlive/tvlive.txt
python convertToM3u.py
git add .
git commit -m "JNG.m3u"
git push
