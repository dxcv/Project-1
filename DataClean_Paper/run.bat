echo start....>>D:\Python\Project\DataClean_Paper\log.log
echo %date% >>D:\Python\Project\DataClean_Paper\log.log

D:
CD D:\Python\Project\DataClean_Paper
python SectiontoPanel_BS.py
python Sectiontopanel_BS_sectorbank.py
python Sectiontopanel_BS_countrybank.py
python Sectiontopanel_BS_nonpublic.py
python Sectiontopanel_BS_public.py


echo finished....>>D:\Python\Project\DataClean_Paper\log.log