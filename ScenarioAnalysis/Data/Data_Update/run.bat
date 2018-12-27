echo start....>>D:\CXM\Project\ScenarioAnalysis\Data\Data_Update\log.log
echo %date% >>D:\CXM\Project\ScenarioAnalysis\Data\Data_Update\log.log

D:
CD D:\CXM\Project\ScenarioAnalysis\Data\Data_Update


python Update_HistData_Stock.py



echo finished....>>D:\CXM\Project\ScenarioAnalysis\Data\Data_Update\log.log