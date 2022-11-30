import requests
import json
from bs4 import BeautifulSoup
import pandas as pd


# headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
#
# content = requests.get('https://www.sec.gov/files/company_tickers_exchange.json', headers=headers,)
#
# big_dict = content.json()
# print(type(big_dict))
# rows = big_dict["data"]
#
# cik_list = []
# company_name_list = []
# ticker_list = []
# exchange_association_list = []
#
# for i in rows:
#     cik_list.append(i[0])
#     company_name_list.append(i[1])
#     ticker_list.append(i[2])
#     exchange_association_list.append(i[3])
#
# mapping_df = pd.DataFrame({'ticker': ticker_list, 'company name': company_name_list, 'CIK number': cik_list, 'Exchange': exchange_association_list})
#
# mapping_df.to_csv('/Users/bradhicks/Desktop/tickerswithexchange.csv', index = False)


string = r"China\
India\
United States\
Indonesia\
Pakistan\
Brazil\
Nigeria\
Bangladesh\
Russia\
Mexico\
Japan\
Ethiopia\
Philippines\
Egypt\
Vietnam\
DR Congo\
Turkey\
Iran\
Germany\
Thailand\
United Kingdom\
France\
Italy\
Tanzania\
South Africa\
Myanmar\
Kenya\
South Korea\
Colombia\
Spain\
Uganda\
Argentina\
Algeria\
Sudan\
Ukraine\
Iraq\
Afghanistan\
Poland\
Canada\
Morocco\
Saudi Arabia\
Uzbekistan\
Peru\
Angola\
Malaysia\
Mozambique\
Ghana\
Yemen\
Nepal\
Venezuela\
Madagascar\
Cameroon\
Côte d'Ivoire\
North Korea\
Australia\
Niger\
Sri Lanka\
Burkina Faso\
Mali\
Romania\
Malawi\
Chile\
Kazakhstan\
Zambia\
Guatemala\
Ecuador\
Syria\
Netherlands\
Senegal\
Cambodia\
Chad\
Somalia\
Zimbabwe\
Guinea\
Rwanda\
Benin\
Burundi\
Tunisia\
Bolivia\
Belgium\
Haiti\
Cuba\
South Sudan\
Dominican Republic\
Czech Republic\
Greece\
Jordan\
Portugal\
Azerbaijan\
Sweden\
Honduras\
United Arab Emirates\
Hungary\
Tajikistan\
Belarus\
Austria\
Papua New Guinea\
Serbia\
Israel\
Switzerland\
Togo\
Sierra Leone\
Laos\
Paraguay\
Bulgaria\
Libya\
Lebanon\
Nicaragua\
Kyrgyzstan\
El Salvador\
Turkmenistan\
Singapore\
Denmark\
Finland\
Congo\
Slovakia\
Norway\
Oman\
State of Palestine\
Costa Rica\
Liberia\
Ireland\
Central African Republic\
New Zealand\
Mauritania\
Panama\
Kuwait\
Croatia\
Moldova\
Georgia\
Eritrea\
Uruguay\
Bosnia and Herzegovina\
Mongolia\
Armenia\
Jamaica\
Qatar\
Albania\
Lithuania\
Namibia\
Gambia\
Botswana\
Gabon\
Lesotho\
North Macedonia\
Slovenia\
Guinea-Bissau\
Latvia\
Bahrain\
Equatorial Guinea\
Trinidad and Tobago\
Estonia\
Timor-Leste\
Mauritius\
Cyprus\
Eswatini\
Djibouti\
Fiji\
Comoros\
Guyana\
Bhutan\
Solomon Islands\
Montenegro\
Luxembourg\
Suriname\
Cabo Verde\
Micronesia\
Maldives\
Malta\
Brunei\
Belize\
Bahamas\
Iceland\
Vanuatu\
Barbados\
Sao Tome & Principe\
Samoa\
Saint Lucia\
Kiribati\
Grenada\
St. Vincent & Grenadines\
Tonga\
Seychelles\
Antigua and Barbuda\
Andorra\
Dominica\
Marshall Islands\
Saint Kitts & Nevis\
Monaco\
Liechtenstein\
San Marino\
Palau\
Tuvalu\
Nauru\
Holy See"




string = string.split('\\')
print(string)
a = []
for i in string:

    str = i.replace('\n', '')
    str = str+'|'
    a.append(str)

print(a)
fin = ''.join(a)
print(fin)


