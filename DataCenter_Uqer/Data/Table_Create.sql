CREATE DATABASE DataCenter_Uqer
GO

USE DataCenter_Uqer
GO


/*******************************************************
                          沪深股票
********************************************************/
/*
基本信息
*/
CREATE TABLE Stock_BasicInfo_Stock(   --股票基本信息
	RefreshDate Date NOT NULL DEFAULT CONVERT(DATE,GETDATE(),112),
	SecID varchar(20)  NULL,
	Code varchar(20) NOT NULL,
	ExchangeCD varchar(10)  NULL,
	ListSectorCD varchar(10)  NULL,
	ListSector nvarchar(20)  NULL,
	TransCurrCD varchar(20)  NULL,
	Name nvarchar(50)  NULL,
	FullName varchar(100)  NULL,
	ListStatusCD  varchar(20)  NULL,
	ListDate Date  NULL,
	DelistDate Date NULL,
	EquTypeCD varchar(20)  NULL,
	EquType nvarchar(30) NULL,
	ExCountryCD nvarchar(50)  NULL,
	PartyID varchar(50)  NULL, --机构内部ID
	TotalShares float  NULL,
	NonrestFloatShares float  NULL,
	NonrestFloatA float  NULL,
	OfficeAddress nvarchar(200) NULL,
	PrimeOperating nvarchar(1000) NULL,
	EndDate Date NULL,
	TShEquity float NULL,
	remark nvarchar(100) NULL
	PRIMARY KEY(RefreshDate,Code)
	) ON [PRIMARY]
GO 

CREATE TABLE Stock_BasicInfo_Sector( --股票板块成分
	RefreshDate Date not null,
	TypeID varchar(100) not null,
	TypeName nvarchar(50) not null,
	SecID varchar(30) not null,
	Code varchar(20) not null,
	ExchangeCD varchar(20) not null,
	SecShortName nvarchar(50) not null
	PRIMARY KEY(RefreshDate,Code,TypeID)
	) ON [PRIMARY]
GO 


CREATE TABLE Stock_BasicInfo_SHHK(   --沪港通合资格股票名单
	RefreshDate Date not null,
	ExchangeCD varchar(20) null,
	SecID varchar(30) not null,
	Code  varchar(20) not null,
	SecShortName nvarchar(50) null,
	SecFullName nvarchar(100) null,
	IntoDate Date not null,
	OutDate Date null,
	IsNew varchar(10) not null,
	PRIMARY KEY(RefreshDate,Code,IntoDate,IsNew)
	) ON [PRIMARY]
GO
	
CREATE TABLE Stock_BasicInfo_CompanyFeature( --个股企业性质
	RefreshDate Date not null,
	SecID varchar(20) not null,
	Code varchar(20) not null,
	SecShortName nvarchar(20) not null,
	ExchangeCD varchar(20) not null,
	CnSpell nvarchar(50) null ,
	SecFullName nvarchar(100) null,
	PartyNatureCD nvarchar(100) null,
	[Profile] nvarchar(200) null
	PRIMARY KEY(RefreshDate,Code)
	) ON [PRIMARY]
GO
		
CREATE TABLE Stock_BasicInfo_CompanySpecialStates(
	RefreshDate Date not null,
	SecID varchar(20) not null,
	Code varchar(20) not null,
	SecShortName nvarchar(20) null,
	ExchangeCD varchar(20) null,
	PartyState varchar(10) not null,
	EffDate Date not null,
	Reason varchar(10) not null,
	UpdateTime Date not null,
	PRIMARY KEY(RefreshDate,Code,UpdateTime,EffDate)
	) ON [PRIMARY]
GO



--CREATE TABLE Stock_BasicInfo_ExcitationCondition(
--	SecID varchar(20) not null,
--	Code varchar(20) not null,
--	SecShortName nvarchar(20) not null,
--	ExchangeCD varchar(20) null,
--	PublishDate Date not null,
--	ExcitSubject nvarchar(50) not null,
--	ExcitCons nvarchar(100) not null,
--	ExerPer Date not null,
--	[Rank] varchar(20) not null,
--	AchAsseSub 

CREATE TABLE Stock_BasicInfo_Classfication(
	RefreshDate Date not null,
	SecID varchar(20) not null,
	Code varchar(20)  not null,
	ExchangeCD varchar(20) not null,
	SecShortName nvarchar(50) null,
	SecFullName nvarchar(100) null,
	PartyID varchar(50) not null,
	IndustryVersionCD varchar(50) not null,
	Industry nvarchar(50) not null,
	IndustryID varchar(20) not null,
	IndustrySymbol varchar(50) null,
	IntoDate Date not null,
	OutDate Date null,
	IsNew varchar(10) not null,
	IndustryID1 varchar(50) null,
	IndustryName1 nvarchar(100) null,
	IndustryID2 varchar(50) null,
	IndustryName2 nvarchar(100) null,
	IndustryID3 varchar(50) null,
	IndustryName3 nvarchar(100) null,
	IndustryID4 varchar(50) null,
	IndustryName4 nvarchar(100) null,
	PRIMARY KEY(PartyID,IndustryVersionCD,IndustryID,Code,IntoDate,IsNew)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_BasicInfo_IndustryInfo(
	RefreshDate date not null,
	IndustryVersionCD  varchar(50) not null,
	IndustryVersion varchar(50) not null,
	Industry nvarchar(50) not null,
	IndustryID varchar(50) null,
	IndustrySymbol nvarchar(50) not null,
	IndustryName nvarchar(50) null,
	IndustryLevel varchar(10) not null,
	IsNew varchar(10) not null,
	IndexSymbol varchar(50) not null,
	UpdateTime Date not null,
	PRIMARY KEY(RefreshDate,IndustryVersionCD,IndustrySymbol,IndustryLevel,IndexSymbol,UpdateTime)
	) ON [PRIMARY]
GO
	
CREATE TABLE Stock_BasicInfo_Salary(
	SecID varchar(20) not null,
	Code varchar(20) not null,
	ExchangeCD varchar(20) not null,
	EndDate Date not null,
	IntervalLevel varchar(20) not null,
	IntervalNumber float not null
	PRIMARY KEY(Code,EndDate,IntervalLevel)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_BasicInfo_Employee(
	SecID varchar(20) not null,
	Code varchar(20) not null,
	SecShortName nvarchar(20) null,
	RecordTime date not null,
	InfoType nvarchar(10) not null,
	TypeValue nvarchar(20) not null ,
	PersonNum float not null,
	Ratio float null
	PRIMARY KEY(Code,RecordTime,InfoType)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_BasicInfo_Manager(  --上市公司管理层
	SecID varchar(20) not null,
	Code varchar(20) not null,
	SecShortName nvarchar(30) not null,
	ExchangeCD varchar(20) null,
	ManagerName nvarchar(20) not null,
	ManagerType varchar(10) not null,
	[Session] varchar(10) not null,
	Position nvarchar(20) not null,
	BeginDate date not null,
	EndDate date null
	PRIMARY KEY(Code,ManagerName,Position,BeginDate)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_BasicInfo_ManagerInfo(
	SecID varchar(20) not null,
	Code varchar(20) not null,
	SecShortName nvarchar(20) not null,
	ExchangeCD varchar(20) not null,
	ManagerName nvarchar(20) not null,
	Gender varchar(10) null,
	Birthday varchar(10) null,
	Education nvarchar(20) null,
	Nationality nvarchar(20) null,
	BackgroundDesc nvarchar(1000) null
	PRIMARY KEY(Code,ManagerName)
	) ON [PRIMARY]
GO


CREATE TABLE Stock_BasicInfo_ManagerSalary( --公司高管持股薪酬明细
	SecID varchar(20) not null,
	Code varchar(20) not null,
	SecShortName nvarchar(20) not null,
	ExchangeCD varchar(20) not null,
	EndDate Date not null,
	Name nvarchar(20) not null,
	Position nvarchar(50) not null,
	AnnReward float null,
	Subsidy float null,
	BeginHoldVol float null,
	EndHoldVol float null,
	HoldType varchar(10) null,
	IsPayPar varchar(10) null,
	PublishDate date null,
	ReportType varchar(10) null,
	IsConcPosi varchar(10) null,
	Updatetime datetime null
	PRIMARY KEY(Code,Name,Position)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_BasicInfo_Commitee(
	SecID varchar(20) not null,
	Code varchar(20) not null,
	SecShortName nvarchar(20) null,
	ExchangeCD varchar(20) null,
	PublishDate date not null,
	Name nvarchar(20) not null,
	ComName nvarchar(100) not null,
	Position varchar(10) not null,
	AccessionDate date  null,
	DimissionDate date  null,
	UpdateTime datetime null
	PRIMARY KEY(Code,PublishDate,Name,Position,ComName)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_BasicInfo_ManagerChange(
	SecID varchar(20) not null,
	Code varchar(20) not null,
	SecShortName nvarchar(20) null,
	ExchangeCD varchar(20) null,
	PublishDate date not null,
	ReportType varchar(10) not null,
	ChangeDate date not null,
	ChangePosition varchar(10) not null,
	ActionType varchar(10) not null,
	Name nvarchar(50) not null,
	SecFullName varchar(100) not null,
	EducationType varchar(10) null,
	QuitType varchar(10) null,
	QuitAge float null,
	OfficeYear float null,
	SuccessionSouce varchar(10) null,
	IsAgent varchar(10) null,
	Concurrentpost varchar(10) null,
	[Resume] nvarchar(1000) null,
	Updatetime datetime null
	PRIMARY KEY(Code,Name,ChangeDate)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_BasicInfo_ActualController(
	SecID varchar(20) not null,
	Code varchar(20) not null,
	SecShortName nvarchar(20) not null,
	EndDate date not null,
	ActControl nvarchar(100) not null,
	[Type] nvarchar(50) not null,
	Descripition nvarchar(1000) null,
	IsEquControl varchar(10) not null,
	ControlRatio float null,
	NonEquConNote nvarchar(1000) null,
	UpdateTime datetime not null
	PRIMARY KEY(Code,ActControl,EndDate,IsEquControl,UpdateTime)
	) ON [PRIMARY]
GO
	
	
CREATE TABLE Stock_BasicInfo_ManagerPartime(
	SecID varchar(20) not null,
	Code varchar(20) not null,
	SecShortName nvarchar(20) not null,
	EndDate date not null,
	Name nvarchar(20) not null,
	PartUnitName nvarchar(100) not null,
	PartPosition nvarchar(100) not null,
	IsReward varchar(10) ,
	UpdateTime datetime not null,
	PRIMARY KEY(Code,Name,EndDate,UpdateTime)
	) ON [PRIMARY]
GO
	
--CREATE TABLE Stock_BasicInfo_RegulatorSalary(  --监管层薪酬
--	SecID varchar(20) not null,
--	Code varchar(20) not null,
--	SecShortName nvarchar(20) not null,
--	EndDate date not null,	
--	SumSalary float null,
--	SunSubsidy float null,
--	SumSalaryTop3 float null,
--	SumSalaryDireTop3 float null,
--	P
	
CREATE TABLE Stock_FR_BalanceSheet(
	SecID varchar(20) not null,
	PublishDate date not null,
	EndDate date not null,
	EndDateRep date not null,
	PartyID varchar(10) not null,
	Code varchar(20) not null,
	SecShortName nvarchar(20)  null,
	ExchangeCD varchar(20) null,
	ActPuTime datetime not null,
	MergeFlag varchar(10) not null,
	ReportType varchar(10) not null,
	FiscalPeriod varchar(10) not null,
	AccountingStandard varchar(20) not null,
	CurrencyCD varchar(10) not null,
	MoneyFund float null,
	SettlementProvisions float null,
	WithdrawalOfFunds float null,
	TransactionalFinancialAssets float null,
	BillReceivables float null,
	AccountsReceivables float null,
	Prepaymentss float null,
	PremiumReceivable float null,
	ReinsuranceReceivables float null,
	ReceivableContractReserve float null,
	InterestReceivables float null,
	DividendReceivables float null,
	OtherReceivables float null,
	BuyBackResaleFinancialAssets float null,
	Inventory float null,
	NoncurrentAssetsDueWithinOneYear float null,
	OtherCurrentAssets float null,
	TotalCurrentAssets float null,
	IssueEntrustedLoansAndAdvances float null,
	AvailableForSaleFinancialAssets float null,
	HeldToMaturityInvestments float null,
	LongtermReceivables float null,
	LongtermEquityInvestment float null,
	InvestmentRealEstate float null,
	FixedAssets float null,
	ConstructionInProgress float null,
	EngineerMaterial float null,
	FixedAssetsCleanup float null,
	ProductiveBiologicalAssets float null,
	OilAndGasAssets float null,
	IntangibleAssets float null,
	DevelopmentExpenditure float null,
	GoodWill float null,
	LongtermPrepaidExpenses float null,
	DeferredTaxAssets float null,
	OtherNonCurrentAssets float null,
	TotalNonCurrentAssets float null,
	TotalAssets float null,
	ShorttermLoan float null,
	BorrowingFromTheCentralBank float null,
	AbsorbingDepositsAndInterbankDeposits float null,
	LoansFromOtherBanks float null,
	TransactionalFinancialLiabilities float null,
	NotesPayable float null,
	AccountsPayable float null,
	DepositReceived float null,
	FinancialAssetsSoldForRepurchase float null,
	FeesAndCommissions float null,
	PayrollPayable float null ,
	TaxesPayable float null,
	InterestPayable float null,
	DividendPayable float null,
	OtherPayables float null,
	DividendPayableForReinsurance float null,
	InsuranceContractReserve float null,
	AgentTradingSecurities float null,
	AgencyUnderwritingSecurities float null,
	NonCurrentLiabilitiesDueWithinOneYear float null,
	OtherCurrentLiabilities float null,
	TotalCurrentLiabilities float null,
	LongtermLoan float null,
	BondsPayable float null,
	OfWhichPreferredStock float null,
	OfWhichPerpetualDebt float null,
	LongtermPayables float null,
	SpecialPayable float null,
	EstimatedLiabilities float null,
	DeferredIncomeTaxLiabilities float null,
	OtherNonCurrentLiabilities float null,
	TotalNonCurrentLiabilities float null,
	TotalLiabilities float null,
	





	

	



 
	

	
CREATE TABLE Stock_HistoryData_Daily(  --沪深股票日行情
	SecID varchar(20) NOT NULL,
	Code varchar(20) NOT NULL,
	Name nvarchar(50) NULL,
	ExchangeCD varchar(10) NULL,
	TradeDate Date NOT NULL,
	PreClosePrice float NULL,
	ActPreClosePrice float NULL, --实际昨收盘
	OpenPrice float NULL,
	HighestPrice float NULL,
	LowestPrice float NULL,
	ClosePrice float NULL,
	TurnoverVol float NULL,
	TurnoverValue float NULL,
	DealAmount float null,  --成交笔数
	TurnoverRate float NULL,
	AccumAdjFactor float NULL,
	NegMarketValue float NULL, --流通市值
	MarketValue float NULL,
	PriceChangePercent float NULL, 
	PE_TTM float NULL, --滚动市盈率，TTM
	PE_Motive float NULL, --动态市盈率
	PB float NULL, 
	IsOpen int NULL,
	Vwap float NULL, --个股成交总金额/总成交量
	remark float NULL
	primary key(SecID,Code,TradeDate)
	) ON [PRIMARY]
GO


CREATE TABLE Index_HistoryData_Daily(   --指数日行情
	IndexID varchar(20) NOT NULL,
	IndexCode varchar(20) NOT NULL,
	PorgFullName nvarchar(50) NULL,
	SecName nvarchar(50) NULL,	
	ExchangeCD varchar(20) NULL,
	TradeDate Date NOT NULL,
	PreCloseIndex float NUll,
	OpenIndex float NULL,
	LowestIndex float NULL,
	HighestIndex float NULL,
	CloseIndex float NULL,
	TurnoverVol float NULL,
	TurnoverValue float NULL,
	PriceChange float NULL,
	PriceChangePercent float NULL
	primary key(IndexID,IndexCode,TradeDate)
) ON [PRIMARY]
GO

CREATE TABLE Stock_Halt(
	RefreshDate Date NOT NULL,
	SecID varchar(50) NOT NULL,
	HaltBeginTime datetime NOT NULL,
	HaltEndTime datetime Not NULL,
	Code varchar(20) NOT NULL,
	Name nvarchar(50)  NULL,
	ExchangeCD varchar(20)  NULL,
	StatusCD varchar(10)  NULL, --上市状态。L-上市；S-暂停；DE-终止上市；UN-未上市。
	DelistDate datetime NULL,
	AssetClass varchar(10) NOT NULL  --E-股票；B-债券；F-基金；FU-期货等
	primary key(Code,HaltBeginTime,HaltEndTime,AssetClass)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_Large_Transactions(
	ID INT IDENTITY(1,1),
	TradeDate Date NOT NULL,
	SecID varchar(20) NULL,
	Code varchar(20) NOT NULL,
	AssetClass varchar(10) NOT NULL,
	ExchangeCD varchar(20) NULL,
	Name nvarchar(50) NULL,
	CurrenyCD varchar(20) NULL,
	TradePrice float NOT NULL,
	TradeValue float NOT NULL,
	TradeVol float NOT NULL,
	BuyerBD nvarchar(100)  NULL,
	SellerBD nvarchar(100)  NULL
	primary key(ID,TradeDate,Code,AssetClass)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_HK_HistoryData_Daily(
	SecID varchar(20) NOT NULL,
	Code varchar(20) NOT NULL,
	ExchangeCD varchar(20) NULL,
	SecShortName nvarchar(50) NULL,
	TradeDate Date Not null,
	PreClosePrice float  null,
	ActPreClosePrice float  null,
	OpenPrice float  null,
	HighestPrice float  null,
	LowestPrice float  null,
	ClosePrice float  null,
	TurnoverVol float  null,
	TurnovarValue float  null,
	SMA_10 float  null,
	SMA_20 float  null,
	SMA_50 float  null,
	SMA_250 float  null
	primary key(Code,TradeDate)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_HistoryData_AdjPre_Daily(  --沪深股票前复权行情
	SecID varchar(20) NOT NULL,
	Code varchar(20) NOT NULL,
	Name nvarchar(50) NULL,
	ExchangeCD varchar(10) NULL,
	TradeDate Date NOT NULL,
	PreClosePrice float NULL,
	ActPreClosePrice float NULL, --实际昨收盘
	OpenPrice float NULL,
	HighestPrice float NULL,
	LowestPrice float NULL,
	ClosePrice float NULL,
	TurnoverVol float NULL,
	NegMarketValue float NULL,
	DealAmount float null,  --成交笔数
	TurnoverRate float NULL,
	AccumAdjFactor float NULL,
	 --流通市值
	TurnoverValue float NULL,
	MarketValue float NULL,
	IsOpen int NULL,
	remark float NULL
	primary key(SecID,Code,TradeDate)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_AdjFactor_Pre(
	SecID varchar(20)  null,
	Code varchar(20) not null,
	ExchangeCD varchar(20) null,
	SecShortName nvarchar(50) null,
	SecShortNameEn varchar(50) null,
	ExDivDate Date not null,
	PerCashDiv float null,
	PerShareDivRatio float null,
	PerShareTransRatio float null,
	AllotmentRatio float null,
	AllotmentPrice float null,
	AdjFactor float null,
	AccumAdjFactor float null,
	EndDate Date not null
	primary key(Code,ExDivDate,EndDate)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_PriceLimit_Daliy(
	SecID varchar(20) null,
	Code varchar(20) not null,
	SecShortName nvarchar(50)  null,
	SecShortNameEn varchar(100)  null,
	ExchangeCD varchar(20) null,
	TradeDate Date not null,
	LimitUpPrice float null,
	LimitDownPrice float null,
	UpLimitReachedTimes float null,
	DownLimitReachedTimes float null
	primary key(Code,TradeDate)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_Tips_Today(
	RecordDate Date not null,
	SecID varchar(20) not null,
	Code varchar(20) not null,
	ExchangeCD varchar(20) null,
	SecShortName nvarchar(20) null,
	TipsDesc nvarchar(100) null,
	TipsTypeCD varchar(20) null,
	TipsType nvarchar(20) null,
	primary key(Code,RecordDate)
	) ON [PRIMARY]
GO

Create table Stock_MoneyFlowsSingle_Daily(
	SecID varchar(20) not null,
	Code varchar(20) not null,
	SecShortName nvarchar(20) not null,
	SecShortNameEn varchar(50)  null,
	ExchangeCD varchar(20) null,
	TradeDate Date not null,
	MoneyInFlow float null,
	MoneyOutFlow float null,
	NetMoneyInFlow float null,
	primary key(Code,TradeDate)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_MoneyFlowsIndustry_Daily(
	IndustryID varchar(50) not null,
	IndustryName nvarchar(50) not null,
	TradeDate Date not null,
	MoneyInFlow float null,
	MoneyOutFlow float null,
	NetMoneyInFlow float null
	primary key(IndustryID,TradeDate)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_AdjFactor_Post( 
	SecID varchar(20)  null,
	Code varchar(20) not null,
	ExchangeCD varchar(20) null,
	SecShortName nvarchar(50) null,
	SecShortNameEn varchar(50) null,
	ExDivDate Date not null,
	PerCashDiv float null,
	PerShareDivRatio float null,
	PerShareTransRatio float null,
	AllotmentRatio float null,
	AllotmentPrice float null,
	SplitsRatio float null,
	AdjFactor float null,
	AccumAdjFactor float null,
	EndDate Date not null
	primary key(Code,ExDivDate,EndDate)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_HistoryData_AdjPost_Daily(  --沪深股票后复权行情
	SecID varchar(20) NOT NULL,
	Code varchar(20) NOT NULL,
	Name nvarchar(50) NULL,
	ExchangeCD varchar(10) NULL,
	TradeDate Date NOT NULL,
	PreClosePrice float NULL,
	ActPreClosePrice float NULL, --实际昨收盘
	OpenPrice float NULL,
	HighestPrice float NULL,
	LowestPrice float NULL,
	ClosePrice float NULL,
	TurnoverVol float NULL,
	TurnoverValue float NULL,
	DealAmount float null,  --成交笔数
	TurnoverRate float NULL,
	AccumAdjFactor float NULL,
	 --流通市值
	NegMarketValue float NULL,
	IsOpen int NULL,
	MarketValue float NULL,
	remark float NULL
	primary key(SecID,Code,TradeDate)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_MoneyFlowsSingle_Details_Daily(
	SecID varchar(20) not null,
	Code varchar(20) not null,
	SecShortName nvarchar(20) not null,
	TradeDate Date not null,
	InFlowS float null,
	InFlowX float null,
	InFlowL float null,
	InFlowXL float null,
	OutFlowS float null,
	OutFlowX float null,
	OutFlowL float null,
	OutFlowXL float null,
	NetInFlowS float null,
	NetInFlowX float null,
	NetInFlowL float null,
	NetInFlowXL float null,
	primary key(Code,TradeDate)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_MoneyFlowsIndustry_Details_Daily(
	IndustryID varchar(50) not null,
	IndustryName nvarchar(100) not null,
	TradeDate Date not null,
	InFlowS float null,
	InFlowM float null,
	InFlowL float null,
	InFlowXL float null,
	OutFlowS float null,
	OutFlowM float null,
	OutFlowL float null,
	OutFlowXL float null,
	NetInFlowS float null,
	NetInFlowM float null,
	NetInFlowL float null,
	NetInFlowXL float null,
	primary key(IndustryID,TradeDate)
	) ON [PRIMARY]
GO

CREATE TABLE Stock_Abnormal_Single_Daily(
	SecID varchar(20) not null,
	Code varchar(20) not null,
	SecShortName nvarchar(30) not null,
	ExchangeCD varchar(20) null,
	TradeDate Date not null,
	AbnormalTypeCD varchar(20) not null,
	AbnormalType nvarchar(100) null,
	Deviation float null,
	TurnoverVol float null,
	TurnoverValue float null,
	AbnormalBeginDate Date null,
	AbnormalEndDate Date null,
	primary key(Code,TradeDate,AbnormalTypeCD)
	) ON [PRIMARY]
GO
	
CREATE TABLE Stock_Abnormal_SalesDepartment_Daily(
	SecID varchar(20) not null,
	Code varchar(20) not null,
	SecShortName nvarchar(50) not null,
	ExchangeCD varchar(20) not null,
	TradeDate Date not null,
	Side varchar(10) not null,
	[Rank] varchar(10) not null,
	SalesDepartment nvarchar(200) not null,
	BuyValue float null,
	SellValue float null,
	TotalValue float null,
	AbnormalTypeCD varchar(20) not null
	primary key(Code,TradeDate,AbnormalTypeCD,[Rank],Side)
	) ON [PRIMARY]
GO
	

	
CREATE TABLE Future_HistoryData_Daily(
	SecID varchar(20) NOT NULL,
	Code varchar(20) NOT NULL,
	ExchangeCD varchar(10) NULL,
	Name nvarchar(50) NULL,	
	TradeDate Date NOT NULL,
	ContractObjicet varchar(20) NOT NULL,
	ContractMark varchar(20) NULL,
	PreSettlePrice float NULL,
	PreClosePrice float NULL,
	OpenPrice float NULL,
	HighestPrice float NULL,
	LowestPrice float NULL,
	ClosePrice float NULL,
	SettlePrice float NULL,
	TurnoverVol float NULL,
	TurnoverValue float NULL,
	OpenInt float NULL, --持仓量
	CHG_C float NULL, --收盘价与做结算价的价差
	CHG_S float NULL, --今结算价与昨结算价的差额
	PriceChangePercent float NULL, --涨跌幅（收盘价-昨结算价）/昨结算价
	PriceChangePercent_S float NULL, --涨跌幅（今结算价-昨结算价）/昨结算价
	MainCon int NULL,
	SmainCon int NULL
	primary key(SecID,Code,TradeDate)
	) ON [PRIMARY]
GO



/*
-------------------------------
期权
-------------------------------
*/
CREATE TABLE Options_BasicInfo(
	SecID varchar(50) not null,
	OptionID varchar(50) not null,
	SecShortName nvarchar(50) not null,
	TickerSymbol varchar(100) not null,
	ExchangeCD varchar(10) null,
	CurrencyCD varchar(10) null,
	VarSecID varchar(50) not null,
	VarShortName nvarchar(50) null,
	VarTicker varchar(20) not null,
	VarExchangeCD varchar(20) null,
	VarType varchar(20) not null,
	ContractType varchar(20) not null,
	StrikePrice float not null,
	ContractMutiplierNumber float not null,
	ContractStatus varchar(10) not null,
	ListDate Date not null,
	ExpirationYear varchar(10) not null,
	ExpirationMonth varchar(10) not null,
	ExpirationDate Date not null,
	LastTradeDate Date not null,
	ExerciseDate Date not null,
	DeliverDate Date not null,
	DelistDate Date not null
	primary key(OptionID,SecShortName)
	) ON [PRIMARY]
GO





/*
-------------------------------
新闻/公告/社交
-------------------------------
*/
--新闻基本信息

CREATE TABLE News_Info(
	NewsID varchar(50) NOT NULL,
	Title nvarchar(1000) NOT NULL,
	Summary nvarchar(1000) NOT NULL,
	OriginSource nvarchar(50) NULL,
	Author nvarchar(50) NULL,
	PublishSite nvarchar(100) NULL,
	PublishTime datetime NULL,
	InsertTime datetime NULL,
	NewsURL varchar(1000) NOT NULL
	primary key (NewsID)
	) ON [PRIMARY]
GO



