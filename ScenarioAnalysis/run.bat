echo start....>>D:\CXM\Project\ScenarioAnalysis\log.log
echo %date% >>D:\CXM\Project\ScenarioAnalysis\log.log

D:
CD D:\CXM\Project\ScenarioAnalysis\Data\Data_Update
python Update_InstrumentInfo_Stock.py
python Update_HistData_Stock.py
python Update_HistData_ETF.py
python GenerateCAL.py
python Update_HistData_FutureContract.py
python Update_Future_Multiplier.py
python Update_HistData_Future.py
python Update_MarketEod.py
python Update_PositionEod.py

D:
CD D:\CXM\Project\ScenarioAnalysis\
python VaR.py
python ToExcel_VaR.py
python ToExcel_Hedge.py
python SendEmail.py

echo finished....>>D:\CXM\Project\ScenarioAnalysis\log.log