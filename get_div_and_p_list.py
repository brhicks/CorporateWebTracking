import re
from clean_names import clean_names

#get p list function
def get_p_list(soup):
    raw_p_list = soup.find_all('p')
    raw_li_list = soup.find_all('li')
    if len(raw_li_list) > len(raw_p_list):
        raw_p_list = raw_li_list

    p_list = [i.text for i in raw_p_list]
    # print(div_list)

    raw_names = []
    for p in p_list:
        p = re.sub(r'\n|\xa0', ' ', p)
        p = p.strip()
        raw_names.append(p)
    # print(raw_names)

    name_list = clean_names(raw_names)

    error = 0
    if len(name_list) ==0:
        error = 'error'

    return [name_list, error]



# div list function
def get_div_list(soup):

    raw_div_list = soup.find_all('div')
    raw_li_list = soup.find_all('li')
    if len(raw_li_list) > len(raw_div_list):
        raw_div_list = raw_li_list

    div_list = [i.text for i in raw_div_list]
    # print(div_list)

    raw_names = []
    for div in div_list:
        div = re.sub(r'\n|\xa0', ' ', div)
        div = div.strip()
        raw_names.append(div)
    # print(raw_names)

    name_list = clean_names(raw_names)
    # print(name_list)


    error = 0
    if len(name_list) ==0:
        error = 'error'


    return [name_list, error]