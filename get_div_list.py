from bs4 import BeautifulSoup
import re
from clean_names import clean_names
# def get_div_list(soup):
    #
    # raw_div_list = soup.find_all('div')
    #
    #
    # div_list = [i.text for i in raw_div_list]
    # #print(div_list)
    #
    # clean_div_list = []
    # for div in div_list:
    #     div = div.replace('\xa0', ' ')
    #     clean_div_list.append(div)
    # print(clean_div_list)
    #
    #
    # clean_subsid_list = []
    # for name in clean_div_list:
    #     name = name.replace('\xa0', ' ')
    #     # remove \xa0
    #     name = name.replace(
    #         '..................................................................................................................................................................',
    #         '')
    #     name = name.replace('........................................', '')
    #     name = name.replace('100%', '')
    #     name = name.replace('      ', '')
    #     name = name.replace('●', '')
    #     name = name.replace('•', '')
    #     name = name.replace('\ufeff', '')
    #     name = name.replace(' \xa0', '')
    #     name = name.replace('\xa0', '')
    #     name = name.replace('\n', '')
    #     name = name.replace('\u200b', '')
    #     name = re.sub("[\(\[].*?[\)\]]", "", name)
    #     # name = re.sub(r'^\w[.)]\s*', '', name)
    #     name = name.split(', a ')
    #     name = name[0]
    #     name = name.split('. a ')
    #     name = name[0]
    #     name = name.split('. an ')
    #     name = name[0]
    #     name = name.split('- a')
    #     name = name[0]
    #
    #     name = name.split(', an ')
    #     name = name[0]
    #     name = name.split('f/k/a')
    #     name = name[0]
    #     name = name.split('d/b/a')
    #     name = name[0]
    #     name = name.split(' – incorporated under the laws')
    #     name = name[0]
    #     name = name.split(' - ')
    #     name = name[0]
    #     name = name.split('Incorporated in')
    #     name = name[0]
    #     name = name.split('incorporated in')
    #     name = name[0]
    #     name = name.split('Incorporated under laws')
    #     name = name[0]
    #     name = name.split('A New York Corp')
    #     name = name[0]
    #     name = name.split('Except as otherwise noted in a footnote')
    #     name = name[0]
    #     name = name.split('The address of each additional registrant’s')
    #     name = name[0]
    #     name = name.split('is a Chinese company')
    #     name = name[0]
    #     name = name.split('Organized in')
    #     name = name[0]
    #     name = name.split('formerly known as')
    #     name = name[0]
    #     name = name.split('LLC a ')
    #     name = name[0]
    #     name = name.split('dba')
    #     name = name[0]
    #     name = name.split('DBA')
    #     name = name[0]
    #
    #     name = name.replace('  ', ' ')
    #     name = name.replace('*', '')
    #
    #     name = name.strip()
    #     bullet_test = name.split('.')
    #     # print(bullet_test[0])
    #     if len(bullet_test[0]) < 3 and bullet_test[0].isnumeric() == 'True':
    #         bullet = bullet_test[0] + '.'
    #         name = name.replace(bullet, '', 1)
    #
    #     # bullet_test = name.split('.')
    #     # print(bullet_test[0])
    #     # print(bullet_test[0].isupper())
    #     # if len(bullet_test[0]) < 3 and bullet_test[0].isupper() == 'False':
    #     #     bullet = bullet_test[0] + '.'
    #     #     name = name.replace(bullet, '', 1)
    #
    #     bullet_test = name.split(')')
    #     if len(bullet_test[0]) < 3:
    #         bullet = bullet_test[0] + ')'
    #         name = name.replace(bullet, '', 1)
    #     percent_test = name.split('%')
    #     if len(percent_test[0]) < 5:
    #         percent = percent_test[0] + '%'
    #         name = name.replace(percent, '', 1)
    #
    #     # name = name.split('Inc.')
    #     # name = name[0]+ 'Inc.'
    #     bad_name_tags = ['Bermuda', 'BERMUDA', 'Cayman Islands', 'CAYMAN ISLANDS', 'British Virgin Islands',
    #                      'United States of America', 'UNITED STATES OF AMERICA', 'USA', 'U.S.A.', 'Canada',
    #                      'CANADA', 'Mexico', 'MEXICO', 'Argentina', 'ARGENTINA', 'Brazil', 'BRAZIL',
    #                      'Uruguay',
    #                      'Peru', 'Chile', 'Paraguay', 'Guatemala', 'Colombia', 'Australia', 'AUSTRALIA',
    #                      'Southeast Asia', 'China', 'CHINA', 'Mauritius', 'India', 'Vietnam', 'Japan',
    #                      'JAPAN',
    #                      'United Kingdom', "U.K.", 'UNITED KINGDOM', 'Spain', 'SPAIN', 'France', 'FRANCE',
    #                      'Holland', 'Italy', 'Turkey', 'Hungary', 'Portugal', 'Austria', 'Poland', 'Russia'
    #                                                                                                'Ukraine',
    #                      'Bulgaria', 'Romania', 'Cyprus', 'Finland', 'Egypt', 'South Africa',
    #                      'United Arab Emirates', 'East Africa', 'West Africa', 'North America', 'Russia',
    #                      'RUSSIA', 'Turkey', 'TURKEY', 'Sweden', 'SWEDEN', 'CHINA – PEOPLE’S REPUBLIC OF',
    #                      'ABU DHABI FREE ZONE', 'HUNGARY', 'HONG KONG', 'INDIA', 'IRELAND', 'ITALY',
    #                      'KOREA',
    #                      'LUXEMBOURG', 'MALAYSIA', 'NETHERLANDS', 'PHILIPPINES', 'SINGAPORE',
    #                      'SOUTH AFRICA',
    #                      'THAILAND', 'OMAN', 'CUBA', 'GERMANY', 'Delaware', 'Virginia'
    #                                                                         'Parent', 'Doing Business As',
    #                      'Company', '21.1', 'Americas:', 'Europe:', 'Asia:',
    #                      'Company', ', Inc.)', 'COMPANY', 'Domestic', 'Texas', 'Maryland', 'Alabama',
    #                      'VIE', 'BELGIUM', 'CHILE', 'COLOMBIA', 'GERMANY', 'GERMANY', 'INDONESIA', 'PANAMA',
    #                      'POLAND', 'PORTUGAL', 'TAIWAN', 'TAIWAN', 'Singapore', 'EUROPE', 'Belgium',
    #                      'Germany', 'Ireland', 'Monaco', 'Slovakia',
    #                      'Note: Interrelationships shown by indentation with ownership unless otherwise indicated.',
    #                      'DOMESTIC', 'FOREIGN', 'Monaco', 'Ireland', ', GmbH)', ', GmbH)', ', B.V.)',
    #                      ', SA)', 'Africa:', 'Asia:', 'Also', 'Title', 'Co. Ltd]', 'PTY LTD]', 'Limited]',
    #                      'AMERICAS', 'Idaho', 'DOMESTIC'
    #
    #                      ]
    #     name = name.replace('  ', ' ')
    #     name = name.strip()
    #     if any(x == name for x in bad_name_tags):
    #         badnamess = 'bad'
    #     else:
    #
    #         if len(name) > 1:
    #             # if any(x name != 'Bermuda' or 'Ceval Holdings Ltd.' or 'NAME' and 'Name of Entity' and 'Entity Name' and 'Organization' and 'SUBSIDIARY' \
    #             #          and 'Subsidiary' and '21.1' and 'Company Name' and 'Company' and 'Name*' and ' Name' and \
    #             #          'Entity':
    #             clean_subsid_list.append(name)
    #
    # # remove string containing "Subsidiar", "subsidiar"
    # clean_subsid_list[:] = [x for x in clean_subsid_list if
    #                         "Subsidiar" not in x and "subsidiar" not in x and 'NAME' not in x and 'SUBSIDIAR' not in x and 'Owns' not in x and 'entities' not in x and 'Entities' not in x and 'Business activity' not in x and 'Voting Securities' not in x and 'Table of Contents' not in x]
    # clean_subsid_list[:] = [x for x in clean_subsid_list if
    #                         '21.1' not in x and '-----------' not in x and 'Name' not in x and 'EXHIBIT 21' not in x and 'jurisdiction' not in x and 'Jurisdiction' not in x and 'Entity' not in x and 'ENTITY' not in x and 'name' not in x and 'Incorporated in ' not in x and 'Exhibit 21' not in x and 'As of ' not in x]
    # clean_subsid_list[:] = [x for x in clean_subsid_list if x]
    #
    # # make sure clean subsid list is not just a number.
    # cleaner_subsid_list = []
    # for i in clean_subsid_list:
    #     i = i.strip()
    #     res = "".join(filter(lambda x: not x.isdigit(), i))
    #     if res != '':
    #         cleaner_subsid_list.append(i)
    # subsidiary_list = cleaner_subsid_list
    #
    # print(subsidiary_list)
    #
    #
    #
    #
    #
    # return subsidiary_list
    #
    # #re.compile('(\xa0)')
    #
    #
    #
    #
    #
    #

    #bad_tags = re.compile()



    # bad_row_tags = ['Exhibit 21', 'exhibit 21', 'Exhibit',
    #                 'SUBSIDIARIES', 'subsidiaries', 'Subsidiaries', 'Subsidiary', 'subsidiary',
    #                 'wholly-owned',
    #                 'As of', 'as of',
    #                 'alphabetical order', 'Alphabetical order', 'Alphabetical Order', 'Delaware']
    # div_list = []
    # clean_line_list = []
    # for div in raw_div_list:
    #     line = div.text
    #     if len(line) > 0 and line != '\xa0':
    #         div_list.append(line)
    # for line in div_list:
    #     if any(x in line for x in bad_row_tags):
    #         print('bad line')
    #     else:
    #         clean_line_list.append(line)
    # print(clean_line_list)
    #
    #
    #


def get_div_list(soup):

    raw_div_list = soup.find_all('div')

    div_list = [i.text for i in raw_div_list]
    # print(div_list)

    raw_names = []
    for div in div_list:
        div = re.sub(r'\n|\xa0', ' ', div)
        div = div.strip()
        raw_names.append(div)
    print(raw_names)

    name_list = clean_names(raw_names)
    print(name_list)

    return name_list











