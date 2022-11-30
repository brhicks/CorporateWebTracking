
import pandas as pd


df1 = pd.read_csv('/Users/bradhicks/Dropbox/2021namestrv1.csv')
print(df1)
df2 = pd.read_csv('/Users/bradhicks/Desktop/2021namestrv2.csv')
print(df2)
df3 = pd.read_csv('/Users/bradhicks/Desktop/2021namestrv2.1.csv')
print(df3)



url1 = df1['Subsidiary List URL'].to_list()
url2 = df3['Subsidiary List URL'].to_list()

different = [x for x in url1 if x not in url2]
print(different)




# df = df[df['CIK Number'] != 45919]
# df = df[df['Subsidiary/DBA Name'] >]



# subsidiary_list = df['Subsidiary/DBA Name'].to_list()
# cik = df['CIK Number'].to_list()
# url = df['Subsidiary List URL'].to_list()
# parent = df['Parent Company Name'].to_list()
#
# #print(subsidiary_list)
#
# subsid_test = []
# cik_test = []
# url_test = []
# parent_test = []

#
#
# for name in subsidiary_list:
#     #print(type(name))
#     print(name)
#     #print(cik[subsidiary_list.index(name)])
#     if  len(name) > 65:
#         subsid_test.append(name)
#         cik_test.append(cik[subsidiary_list.index(name)])
#         url_test.append(url[subsidiary_list.index(name)])
#         parent_test.append(parent[subsidiary_list.index(name)])
#         print(parent_test)
# print(parent_test)
#
#
# #
#
# name_df = pd.DataFrame({'Subsidiary/DBA Name' : subsid_test, 'CIK Number' : cik_test,'Parent Company Name' : parent_test, 'Subsidiary List URL' : url_test })
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# print(name_df)
# name_df.to_csv('/Users/bradhicks/Desktop/2021qualitytest.csv', index = False)

