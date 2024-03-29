/****** Script for SelectTopNRows command from SSMS  ******/
 
ALTER TABLE [ScenarioAnalysis].[dbo].[Future_Multiplier_Continuing] WITH NOCHECK ADD 
CONSTRAINT PK_Future_Multiplier_Continuing PRIMARY KEY  NONCLUSTERED 
(
[ProductID],
[RecordDate]
) ON [PRIMARY] 
go

ALTER TABLE [ScenarioAnalysis].[dbo].[HistData_Future] WITH NOCHECK ADD 
CONSTRAINT PK_HistData_Future PRIMARY KEY  NONCLUSTERED 
(
[productID],
[tradingDate]
) ON [PRIMARY]
go

ALTER TABLE [ScenarioAnalysis].[dbo].[HistData_Stock] WITH NOCHECK ADD 
CONSTRAINT PK_HistData_Stock PRIMARY KEY  NONCLUSTERED 
(
[Date],
[InstrumentID]
) ON [PRIMARY]
go

ALTER TABLE [ScenarioAnalysis].[dbo].[MarketEod] WITH NOCHECK ADD 
CONSTRAINT PK_MarketEod PRIMARY KEY  NONCLUSTERED 
(
[Date],
[InstrumentID]
) ON [PRIMARY]
go

ALTER TABLE [ScenarioAnalysis].[dbo].[PositionEod] WITH NOCHECK ADD 
CONSTRAINT PK_PositionEod PRIMARY KEY  NONCLUSTERED 
(
[Date],
[AccountID],
[InstrumentID],
[TotalPosition],
[direction],
[portfolioID],
[parentID]
) ON [PRIMARY]
go

ALTER TABLE [ScenarioAnalysis].[dbo].[VaR_Record] WITH NOCHECK ADD 
CONSTRAINT PK_VaR_Record PRIMARY KEY  NONCLUSTERED 
(
[date],
[portfolioID],
[InstrumentID],
[productID]
) ON [PRIMARY]
go

ALTER TABLE [ScenarioAnalysis].[dbo].[SectorInfo_Stock] WITH NOCHECK ADD 
CONSTRAINT PK_SectorInfo_Stock PRIMARY KEY  NONCLUSTERED 
(
[SectorID]
,[SectorName]
,[InstrumentID]
) ON [PRIMARY]
go
