import statistics
import re
from clean_names import clean_names
#



def get_table_list(soup):
    # print(soup.prettify())
    row_list = []
    table_rows = soup.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        row_list.append(row)

        # Check to see if there are p or div in td

    # find the correct row length in row list
    good_data_tags = ['Corporation', 'Corp', 'Inc.', 'inc.', 'LLC', 'llc', 'limited',
                      'LTD', 'Limited', 'PTY', ' AG', 'SA de CV', ' AB', 'corp.', 'Co.', 'Company', 'company', 'Corp.',
                      'Inc.', 'L.L.C', 'LLC', 'B.V.', 'Bank', 'National Association', 'Ltd.', 'S.A', 'L.P.', 'B.V.',
                      'Ltd', 'LP', 'GmbH', ' ULC', ' N.V.', ' Inc', 'Bhd.', 'B. V.', ' AS', 'Ltd.']
    # get row length
    length_list = []
    for row in row_list:
        #print(row)
        for i in row:
            if any(x in i for x in good_data_tags):
                length_list.append(len(row))

    # Create error list for no length
    length_error = 0
    if len(length_list) > 0:
        # print('length list', length_list)
        row_length = round(statistics.median(length_list))

        # Only get rows equal to row length
        clean_row_list = []
        for row in row_list:
            if len(row) == row_length:
                # print(row)
                clean_row_list.append(row)
        # print('clean_row_list', clean_row_list)

        # get clean row error list, this will occur when number of clean rows = 0
        clean_row_error = 0
        if len(clean_row_list) > 0:
            # index the subsidiaries list
            index_list = []
            for row in clean_row_list:
                for i in row:
                    subsidiary_tags = [' Corporation',' corporation', 'inc.', 'LLC', 'llc', ' Limited Liability Corporation',
                                       'LTD', 'Limited', 'PTY', 'AG', 'SA de CV', 'AB', 'Co.', 'Corp.', 'corp.',
                                       'Inc.', 'L.L.C', 'B.V.', 'Subsidiary', 'Bank', 'GmbH', 'Ltd.', 'S.A', 'L.P.',
                                       'B.V.', 'Ltd', 'LP', ' limited liability corporation', 'Entity Name', 'Parent'
                                       ]

                    if any(x in i for x in subsidiary_tags):
                        index_list.append(row.index(i))


            # error for when no index is possible
            index_error = 0
            if len(index_list) != 0:
                # print('index list', index_list)
                subsidiary_index = round(statistics.median(index_list))
                # print('subsidiary index', subsidiary_index)
                clean_div_list = []
                clean_p_list = []

                for tr in table_rows:
                    td = tr.find_all('td')
                    th = tr.find_all('th')

                    if len(td) == row_length and len(th) == 0:
                        td = tr.find_all('td')[subsidiary_index]
                        #print('td-', td)
                        div = td.find_all('div')
                        clean_div = [i.text for i in div]
                        p = td.find_all('p')
                        clean_p = [i.text for i in p]
                        # print('clean p', clean_p)

                        #print('clean div',clean_div)
                        for i in clean_div:
                            clean_div_list.append(i)
                        for i in clean_p:
                            clean_p_list.append(i)
                #print('clean',clean_div_list)

                if len(clean_div_list) >= len(clean_row_list):
                    subsidiary_list = clean_div_list
                if len(clean_p_list) >= len(clean_row_list):
                    subsidiary_list = clean_p_list
                if len(clean_div_list) < len(clean_row_list) and len(clean_p_list) < len(clean_row_list):
                    subsidiary_list = []
                    for row in clean_row_list:

                        subsidiary_list.append(row[subsidiary_index])

                # print('raw_subsid', subsidiary_list)

                subsidiary_list = clean_names(subsidiary_list)



                #print('subsid list', subsidiary_list)
            else:
                index_error = 'error'
                subsidiary_list = ['error']
                clean_row_error = 0
                length_error = 0
        else:
            clean_row_error = 'error'
            subsidiary_list = ['error']
            index_error = 0
            length_error = 0
    else:
        length_error = 'error'
        subsidiary_list = ['error']
        clean_row_error = 0
        index_error = 0

    return [subsidiary_list, length_error, clean_row_error, index_error]






