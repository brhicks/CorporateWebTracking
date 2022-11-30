import re


def clean_names(raw_list):


    name_list = []
    for string in raw_list:
        string = re.sub(r'(\xa0|\n)', ' ', string)
        # double white space
        string = re.sub(r'"', '', string)
        string = re.sub(r'  ', ' ', string)
        # remove % at beginning of line
        string = re.sub(r'^[0-9][0-9][0-9]?\%', '', string)
        # remove bullet points
        string = re.sub(r"^(—|-| -|--|•|●|◦|\*|†|\+|=\+|\*\*?\*?)",'', string)
        string = re.sub(r"^([a-z][.)])", '', string)
        #remove if upper case and )
        string = re.sub(r"^([A-Z]\))",'', string)
        # remove number bullets
        string = re.sub(r"^([0-9]+[.)])",'',string)
        #remove anything in parenthesis
        string = re.sub(r"[\(\[\{].*[\)\]\}]", "", string)

        # print(string)
        # remove anything after corporation type
        llc = re.compile(r"( L\.L\.C| LLC| limited liablility company)", re.IGNORECASE)
        llc_exists = re.search(llc, string)
        if llc_exists != None:
            string = re.split(llc, string)
            string = string[0] + ' LLC'
        # print(string)

        inc = re.compile(r"( inc\.| incorporated)", re.IGNORECASE)
        inc_exists = re.search(inc, string)
        if inc_exists != None:
            string = re.split(inc, string)
            string = string[0] + ' Inc.'
        # print('check 1', string)
        corp = re.compile(r"( corp\.| corporation)", re.IGNORECASE)
        corp_exists = re.search(corp, string)
        if corp_exists != None:
            string = re.split(corp, string)
            string = string[0] + ' Corp.'
        # print('check 2', string)

        ltd = re.compile(r"( ltd| limited)", re.IGNORECASE)
        ltd_exists = re.search(ltd, string)
        if ltd_exists != None:
            string = re.split(ltd, string)
            string = string[0]+ ' ltd'

        sarl = re.compile(r"( S\.[àáa] r\.l| S\.A\.)", re.IGNORECASE)
        sarl_exists = re.search(sarl, string)
        if sarl_exists != None:
            string = re.split(sarl, string)
            string = string[0]+ ' S.à r.l.'

        gmbh = re.compile(r"(gmbh)", re.IGNORECASE)
        gmbh_exists = re.search(gmbh, string)
        if gmbh_exists != None:
            string = re.split(gmbh, string)
            string = string[0]+ 'GmbH'

        # comp = re.compile(r"(co\.|company)", re.IGNORECASE)
        # comp_exists = re.search(comp, string)
        # if comp_exists != None:
        #     string = re.split(comp, string)
        #     string = string[0] + 'Co.'

        lp = re.compile(r"(L\.P\.|limited partner|Limited Partner)")
        lp_exists = re.search(lp, string)
        if lp_exists != None:
            string = re.split(lp, string)
            string = string[0] + 'LP'

        bv = re.compile(r"(b\.v\.)", re.IGNORECASE)
        bv_exists = re.search(bv, string)
        if bv_exists != None:
            string = re.split(bv, string)
            string = string[0] + 'B.V.'

        srl = re.compile(r"(s\.r\.l)", re.IGNORECASE)
        srl_exists = re.search(srl, string)
        if srl_exists != None:
            string = re.split(srl, string)
            string = string[0] + 'S.r.l'

        the_rest = re.compile('(, a |, an |- a |- an |– a |– an )', re.IGNORECASE)
        the_rest_exists = re.search(the_rest, string)
        if the_rest_exists != None:
            string = re.split(the_rest, string)
            string = string[0]
        string = string.strip()
        #remove if string starts with
        bad_start = re.compile(r"(name|all of|also doing business|State of Incorporation|Brackets indicate state or country of incorporation|tradename|Entity also does business|Property Name|parent|exact name|Legal Entity|entity legal|percentage of ownership|PEOPLE’S REPUBLIC OF CHINA|MACAO, SPECIAL ADMINISTRATIVE REGION|dormant|which|entity name|certain companies|incorporated state|legal name|owned by:|address:|corporate name|membership units:)", re.IGNORECASE)
        bad_start_exists = re.match(bad_start, string)
        if bad_start_exists != None:
            string = ''


        # string must contain a alphapetic character > len 3
        letters = re.findall(r'[a-zA-Z\s]+',string)
        letters_length = len(''.join(letters))

        string = string.strip()
        string = string.replace('  ',' ')
        string = string.replace('  ',' ')

        # get rid of anything under length 3
        if letters_length <= 3:
            string = ''

        # remove exact match lines
        bad_strings = re.compile(r"(dba|U\.S\.A\.|international|company|company name|foreign|Ownership Percentage Name|full legal name|Entity Name|Business Conducted under Same Name|none\.|LEGAL ENTITY NAME|Republic of South Africa|Sevilla, Spain|Bangkok, Thailand|Andover, Hampshire, England|Domestic|corporate name|USA|korea|name|entity|Alberta|British Columbia|Cayman Islands|Manitoba|New Brunswick|Nova Scotia|Ontario|Quebec|Saskatchewan|Alabama|Alaska|Arizona|Arkansas|California|Colorado|Connecticut|Delaware|Massachusetts|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|Mississippi|Missouri|Montana|Nebraska|Nevada|New Hampshire|New Jersey|New Mexico|New York|North Carolina|North Dakota|Ohio|Oklahoma|Oregon|Pennsylvania|Rhode Island|South Carolina|South Dakota|Tennessee|Texas|Utah|Vermont|Virginia|Washington|West Virginia|Wisconsin|Wyoming|China|India|United States|Indonesia|Pakistan|Brazil|Nigeria|Bangladesh|Russia|Mexico|Japan|Ethiopia|Philippines|Egypt|Vietnam|DR Congo|Turkey|Iran|Germany|Thailand|United Kingdom|France|Italy|Tanzania|South Africa|Myanmar|Kenya|South Korea|Colombia|Spain|Uganda|Argentina|Algeria|Sudan|Ukraine|Iraq|Afghanistan|Poland|Canada|Morocco|Saudi Arabia|Uzbekistan|Peru|Angola|Malaysia|Mozambique|Ghana|Yemen|Nepal|Venezuela|Madagascar|Cameroon|Côte d'Ivoire|North Korea|Australia|Niger|Sri Lanka|Burkina Faso|Mali|Romania|Malawi|Chile|Kazakhstan|Zambia|Guatemala|Ecuador|Syria|Netherlands|Senegal|Cambodia|Chad|Somalia|Zimbabwe|Guinea|Rwanda|Benin|Burundi|Tunisia|Bolivia|Belgium|Haiti|Cuba|South Sudan|Dominican Republic|Czech Republic|Greece|Jordan|Portugal|Azerbaijan|Sweden|Honduras|United Arab Emirates|Hungary|Tajikistan|Belarus|Austria|Papua New Guinea|Serbia|Israel|Switzerland|Togo|Sierra Leone|Laos|Paraguay|Bulgaria|Libya|Lebanon|Nicaragua|Kyrgyzstan|El Salvador|Turkmenistan|Singapore|Denmark|Finland|Congo|Slovakia|Norway|Oman|State of Palestine|Costa Rica|Liberia|Ireland|Central African Republic|New Zealand|Mauritania|Panama|Kuwait|Croatia|Moldova|Georgia|Eritrea|Uruguay|Bosnia and Herzegovina|Mongolia|Armenia|Jamaica|Qatar|Albania|Lithuania|Namibia|Gambia|Botswana|Gabon|Lesotho|North Macedonia|Slovenia|Guinea-Bissau|Latvia|Bahrain|Equatorial Guinea|Trinidad and Tobago|Estonia|Timor-Leste|Mauritius|Cyprus|Eswatini|Djibouti|Fiji|Comoros|Guyana|Bhutan|Solomon Islands|Montenegro|Luxembourg|Suriname|Cabo Verde|Micronesia|Maldives|Malta|Brunei|Belize|Bahamas|Iceland|Vanuatu|Barbados|Sao Tome & Principe|Samoa|Saint Lucia|Kiribati|Grenada|St. Vincent & Grenadines|Tonga|Seychelles|Antigua and Barbuda|Andorra|Dominica|Marshall Islands|Saint Kitts & Nevis|Monaco|Liechtenstein|San Marino|Palau|Tuvalu|Nauru|Holy See|Bermuda).?", re.IGNORECASE)
        bad_line = re.fullmatch(bad_strings, string)
        if bad_line == None:



            # print('check 3', string)
            # Remove blanks and lines that contain bad tags
            string = string.strip()
            remove_line = re.search('(Securities Exchange Act|registrant|table of contents|exhibit 21|subsidiar|jurisdiction|voting securities|january|february|march|april|june|july|august|september|october|november|december|[0-9][0-9]?\,|\/[0-9][0-9]?\,|\/[1-2][901][0-9][0-9]|percentage.+of)', string, re.IGNORECASE)
            if remove_line == None and string != '':
                # print('check 4', string)
                name_list.append(string)
        # print(name_list)
    return name_list