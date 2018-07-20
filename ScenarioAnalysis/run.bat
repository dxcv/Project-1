echo start....>>D:\CXM\Project_New\ScenarioAnalysis\log.log
echo %date% >>D:\CXM\Project_New\ScenarioAnalysis\log.log

D:
CD D:\CXM\Project_New\ScenarioAnalysis\Data\Data_Update\


python Update_Future_Multiplier.py
python Update_HistData_Future.py
python Update_MarketEod.py
python Update_PositionEod.py
python Update_InstrumentInfo_Stock.py
python Update_HistData_Stock.py

D:
CD D:\CXM\Project_New\ScenarioAnalysis\
python VaR.py
python ToExcel_VaR.py
python ToExcel_Hedge.py
python SendEmail.py

echo finished....>>D:\CXM\Project_New\ScenarioAnalysis\log.log