import uuid
import datetime
import json


class CompanyType:
    LLC = 'LLC'
    LLP = 'LLP'

class NewCompany:
    def __init__(self, company_legal_name=str, company_type=str, source_url=str, source_date=str, source_type=str, company_dba=False, city=None, state=None, zip_code=None, company_ein=None, company_cik=None, parent_company_name=None):
        self.company = {}
        self.company['company id'] = uuid.uuid4()
        self.company['company created'] = datetime.datetime.utcnow()
        self.company['source date'] = source_date
        self.company['source type'] = source_type
        self.company['source'] = source_url
        self.company['company legal name'] = company_legal_name
        self.company['company type'] = company_type
        self.company['company dba'] = company_dba
        self.company['city'] = city
        self.company['state'] = state
        self.company['zip code'] = zip_code
        self.company['company ein'] = company_ein
        self.company['company cik'] = company_cik
        self.company['parent company name'] = parent_company_name
        self.company['parent company id'] = uuid.uuid4()
        # print(self.company['company id'])


    # def check_and_update_db(self):
    #
    #     for i in db:
    #         if self.company['company legal name'] == company
    #     print(self.company['company legal name'])



def main():
    print('hello')
    company = NewCompany('Big Bad, LLC')
    print(company.company.values())
    print(company.company.keys())
    # company.check_and_update_db()


if __name__ == "__main__":
    main()
