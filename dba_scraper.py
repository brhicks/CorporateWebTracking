import re


def dba_scraper(soup):
    row_list = []
    table_rows = soup.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        row_list.append(row)
    # print(row_list)
    dba_tags = re.compile(r"(dba|d/b/a|doing business as|Name Doing Business As|does business|trade name)", re.IGNORECASE)
    top_row_tag = re.compile(r"(subsidiar|state of incorporation|State or Country of Incorporation'|% of Ownership|percentage of ownership|jurisdiction of incorporation)", re.IGNORECASE)


    index_found = 0
    for row in row_list:
        # print(row)
        dba_exists = []
        top_row_exists = []
        for string in row:
            dba_exists.append(re.search(dba_tags, string))

            top_row_exists.append(re.search(top_row_tag,string))


        # print('other tag', top_row_exists)
        # print('dba', dba_exists)


        for i in top_row_exists:
            if i != None:
                for i in dba_exists:
                    if i != None:
                        # print(i)
                        dba_list_index = row_list.index(row)
                        dba_row_index = dba_exists.index(i)
                        index_found = 'found'

        if index_found == 'found':
            break

    subsid_list = []
    raw_dba_list = []
    if index_found == 'found':
        # print('list index', dba_list_index)
        # print('row index', dba_row_index)
        for row in row_list[dba_list_index+1:]:
            if len(row) == len(row_list[dba_list_index]):
                # print(row)
                dba = row[dba_row_index]
                raw_dba_list.append(dba)

        list_two = []
        for string in raw_dba_list:
            string = re.sub(r'(\xa0|\n)', ' ', string)
            # double white space
            string = re.sub(r'"', '', string)
            string = re.sub(r'  ', ' ', string)
            # remove % at beginning of line
            string = re.sub(r'^[0-9][0-9][0-9]?\%', '', string)
            # remove bullet points
            string = re.sub(r"^(-| -|--|•|●|◦|\*|†|\+|=\+|\*\*?\*?)", '', string)
            string = re.sub(r"^([a-z][.)])", '', string)
            # remove if upper case and )
            string = re.sub(r"^([A-Z]\))", '', string)
            # remove number bullets
            string = re.sub(r"^([0-9]+[.)])", '', string)
            # remove anything in parenthesis
            string = re.sub(r"[\(\[\{].*[\)\]\}]", "", string)

            #remove any business tags
            re.compile(r"(, Inc\.|, L\.?L\.?C\.?)")

            # split to see if string contains a list
            string = re.split(r"(\,|\:|\;)", string)

            for i in string:
                list_two.append(i)


        for string in list_two:
            string = string.strip()
            has_letters = re.search(r"[a-zA-Z]", string)
            if has_letters != None:
                subsid_list.append(string)
        # print(subsid_list)

    return subsid_list
















