USE [DataCenter_Commodity]
GO


CREATE TABLE [Commodity](
	[Date] [datetime] NOT NULL,
	[CategoryID] [varchar](20) NOT NULL,
	[CategoryName] nvarchar(50) NOT NULL,
	[ProductID] [varchar](20) NOT NULL,
	[ProductName] nvarchar(50) NOT NULL,
	[ClassID] [varchar](10) NOT NULL,
	[ClassName] [nvarchar](20) NOT NULL,
	[ItemID] [varchar](20) NOT NULL,
	[ItemName] [nvarchar](100) NOT NULL,
	[Frequency] [nvarchar](10) NOT NULL,
	[Unit] [nvarchar](20) NOT NULL,
	[Data] [float] NULL,
	[Source] [nvarchar](100) NULL,
	[UpdateSource] [nvarchar](100) NULL,
	[UpdateTime]  [datetime] default GETDATE(),
	[Remark] [nvarchar](100) NULL
	primary key([Date],[CategoryID],[ProductID],[ClassID],[ItemID])
) ON [PRIMARY]
GO

