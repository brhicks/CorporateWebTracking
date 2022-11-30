import re
#import libraries
import requests
import pandas as pd
import lxml
from bs4 import BeautifulSoup
import unicodedata
# from get_div_list import get_div_list
# from get_table_list import get_table_list_two
# from get_div_list import get_div_list
from get_table_list import get_table_list_three
from get_div_list import get_div_list_two
from get_div_and_p_list import get_p_list

url = 'https://www.sec.gov/Archives/edgar/data/936395/000093639521000054//ex21120211030-subsidiaries.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1034760/000165495421003119//wyy_ex21.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1050915/000105091521000009//pwr-ex211x12x31x2020.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1018254/000007420821000025//udr-20201231ex21ea607be.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1022079/000102207921000029//dgx12312020ex211.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1089819/000108981921000003//cnl-20201231x10kxex21.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1022079/000102207921000029//dgx12312020ex211.htm'
url = 'https://www.sec.gov/Archives/edgar/data/103682/000156459021008442//d-ex21_497.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1001082/000155837021001322//dish-20201231xex21.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1041803/000156276221000364//psmt-20210831xex21_1.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1041803/000156276221000364//psmt-20210831xex21_1.htm'
url = 'https://www.sec.gov/Archives/edgar/data/723531/000072353121000035//payx-20210531xex21_1.htm'
url = 'https://www.sec.gov/Archives/edgar/data/818686/000119312521036239//d102112dex21.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1000209/000156459021013216//mfin-ex211_9.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1525773/000152577321000006//exhibit211202010-k.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1004036/000089971521000065//skt10k12312020ex212.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1031203/000103120321000007//a2020ex211-subsidiariesofg.htm'
url = 'https://www.sec.gov/Archives/edgar/data/102212/000010221221000010//uvsp-20201231xex21.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1026655/000102665521000003//ex21.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1000228/000100022821000019//exhibit211.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1185348/000118534821000006//newpraa-ex211_20201231x10k.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1364885/000162828021003321//spr-20201231xex211.htm'
url = 'https://www.sec.gov/Archives/edgar/data/917225/000165495421002412//slr_ex211.htm'
url = 'https://www.sec.gov/Archives/edgar/data/899866/000089986621000014//alxnex21112312020.htm'
url = 'https://www.sec.gov/Archives/edgar/data/81362/000008136221000004//exhibit21.htm'
url = 'https://www.sec.gov/Archives/edgar/data/1029199/000121390021010724//ex211_1.htm'
url = 'https://www.sec.gov/Archives/edgar/data/81362/000008136221000004//exhibit21.htm'




#User Agent
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
html_content = requests.get(url, headers=headers).text
soup = BeautifulSoup(html_content, 'html.parser')
print('url', url)
get_div_list_two(soup)

#get_div_list(soup)


















# Difficult tr urls


# url = 'https://www.sec.gov/Archives/edgar/data/1032033/000162828020002579//slmex21112312019.htm'
#
# url = 'https://www.sec.gov/Archives/edgar/data/1621434/000162828020002208//exhibit211-subsidiarie.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1711929/000156459020012051//ck0001711929-ex211_7.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1161154/000116115420000010//eto-12312019xex211.htm'
# url  = 'https://www.sec.gov/Archives/edgar/data/935419/000149315221031404//ex21-1.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/921557/000155837021001988//rbcaa-20201231xex21.htm'
# url='https://www.sec.gov/Archives/edgar/data/921114/000155837021003202//armp-20201231ex21148ae91.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/916076/000156459021006959//mlm-ex2101_7.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1577966/000086054621000010//copt12312020ex212.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1448597/000139390521000121//augg_ex211.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1000209/000156459021013216//mfin-ex211_9.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/100885/000010088521000068//unp-20201231xex21.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1108524/000110852421000014//ex211listofsubsidiariesfy21.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1094084/000168316821001114//telkonet_ex2101.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1067701/000106770121000008//uri-2020123110kex21.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1144519/000114451921000006//subsidiarieslistexhibit211.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1068689/000149315221006652//ex21-1.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1023313/000156459021012256//forr-ex21_7.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1045309/000104530921000028//a4q20exhibit21.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1048286/000162828021002433//mar-q42020xexx21.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1048286/000162828021002433//mar-q42020xexx21.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1293310/000121465921002990//ex21_1.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1029831/000102983121000022//exhibit211-122620.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/1046050/000093905721000347//tsbk-9302021x10kxex21.htm'
# url = 'https://www.sec.gov/Archives/edgar/data/49754/000004975421000007//din-12312020x10kxex21.htm'

#url = 'https://www.sec.gov/Archives/edgar/data/1001082/000155837020000945//ex-21.htm'

# row length varies -> no real way around this one besides what i have written ( does not get all subsidiaries)
# appears to be very uncommon
#url = 'https://www.sec.gov/Archives/edgar/data/100517/000010051720000010//ual12311910kex21.htm'
# no top row
#url = 'https://www.sec.gov/Archives/edgar/data/1000753/000100075320000013//a12312019nsp-ex211xsub.htm'


#Parent co not in first row
#url = 'https://www.sec.gov/Archives/edgar/data/1004980/000100498020000009//exhibit21-123119.htm'

# Row length varies - these are looking good
#url =  'https://www.sec.gov/Archives/edgar/data/1003410/000078328020000010//a10kex2112019.htm'
#url = 'https://www.sec.gov/Archives/edgar/data/1006837/000100683720000044//a10k19ex211-subsidiary.htm'
#url = 'https://www.sec.gov/Archives/edgar/data/1000228/000100022820000018//d848607dex211.htm'

# DBA Issues
#url = 'https://www.sec.gov/Archives/edgar/data/101382/000156459020007046//umbf-ex211_12.htm'
#url = 'https://www.sec.gov/Archives/edgar/data/1012019/000143774920003589//ex_173451.htm'

# No table headers
#url = 'https://www.sec.gov/Archives/edgar/data/1007587/000100758720000004//kvhi12312019ex211listofsub.htm'

# Table row example
#url = 'https://www.sec.gov/Archives/edgar/data/1041061/000104106120000015//yum-12312019xex211.htm'



# https://www.sec.gov/Archives/edgar/data/100517/000010051720000010//ual12311910kex21.htm weird one
# https://www.sec.gov/Archives/edgar/data/101778/000010177820000023//mro-20191231x10kxex211.htm jurisdiction issue

