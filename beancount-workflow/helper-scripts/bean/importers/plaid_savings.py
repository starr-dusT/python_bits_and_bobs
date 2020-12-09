from beancount.core.number import D
from beancount.core.number import ZERO
from beancount.core import data
from beancount.core import account
from beancount.core import amount
from beancount.core import position
from beancount.ingest import importer
from beancount.core import flags

import re
from os import path
from dateutil.parser import parse
import csv
from titlecase import titlecase

class plaid_savings(importer.ImporterProtocol):
    
    def name(self):
        return('plaid_savings')

    def identify(self, file):
        return(re.match('plaid_savings_\d\d\d\d-\d\d-\d\d_\d\d\d\d-\d\d-\d\d', path.basename(file.name))) 

    def extract(self, file):
        entries = []
        with open(file.name) as file:
            for index, row in enumerate(csv.DictReader(file)):
                trans_date = parse(row['date']).date()
                trans_desc = titlecase(row['name'].rstrip())
                trans_amt = row['amount']
                meta = data.new_metadata(file.name, index)
                txn = data.Transaction(
                        meta=meta,
                        date=trans_date,
                        flag=flags.FLAG_OKAY,
                        payee=trans_desc,
                        narration="",
                        tags=set(),
                        links=set(),
                        postings=[]
                )

                if D(trans_amt) > 0:
                    txn.postings.append(data.Posting('Assets:VSCU:Savings', amount.Amount(D(trans_amt), 'USD'), None, None, None, None))
                    txn.postings.append(data.Posting('FIXME', None, None, None, None, None))
                else:
                    txn.postings.append(data.Posting('FIXME', amount.Amount(D(trans_amt), 'USD'), None, None, None, None))
                    txn.postings.append(data.Posting('Assets:VSCU:Savings', None, None, None, None, None))

                entries.append(txn)
        return entries
