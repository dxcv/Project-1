echo start....>>D:\CXM\Project_New\DataCenter_Uqer\News\log.log
echo %date% >>D:\CXM\Project_New\DataCenter_Uqer\News\log.log

D:
CD D:\CXM\Project_New\DataCenter_Uqer\News

python GetNews.py

echo finished....>>D:\CXM\Project_New\DataCenter_Uqer\News\log.log