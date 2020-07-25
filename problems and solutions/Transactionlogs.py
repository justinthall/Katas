"""A program to take a csv of transactions and process them in various different way:"""
import csv

# Gotta set the path we're looking for, so that way it's a little easier to use for other instances.
path = 'payments.csv'


# First, we create a class that serves as a model for all these transactions. we know that all payments follow the same organization.

class transaction:
    def __init__(self, line):
        self.customer = line[1]
        self.age = line[2]
        self.gender = line[3]
        self.zip = line[4]
        self.merchant = line[5]
        self.zipmerchant = line[6]
        self.category = line[7]
        self.amount = float(line[8])
        self.fraud = line[9]
        self.body = {'customer': self.customer, 'age': self.age, 'gender': self.gender, 'zip': self.zip,
                     'mercant': self.merchant, 'merchant zip': self.zipmerchant, 'category': self.category,
                     'amount': self.amount, 'fraud': self.fraud}


# Then, we should make a method to open up our csv and parse all of these transactions into these objects,
# to make it easier to manipulate later.
def parse_to_list():
    list = []
    with open(path, 'r') as fp:
        readdata = csv.reader(fp)
        for line in readdata:
            if line == ['step', 'customer', 'age', 'gender', 'zipcodeOri', 'merchant', 'zipMerchant', 'category',
                        'amount', 'fraud']:
                continue
            list.append(transaction(line))
    return list


# For Task1, we simply need to return the list of merchants in a set, which can be done by running our parse function,
# and iterating through the list of objects to pull their merchant value out.
def list_merchants():
    list = parse_to_list()
    merchants = []
    for transaction in list:
        merchants.append(transaction.merchant)
    return merchants


# for task 2, we have to return all unique mercants. We can easily do that by adding a for statement that checks if
# the merchant is already in our list that we're appending to, and then skipping them if they are.
def list_unique_merchants():
    list = parse_to_list()
    unique_merchants = []
    for transaction in list:
        if transaction.merchant in unique_merchants:
            continue
        unique_merchants.append(transaction.merchant)
    return unique_merchants


# Task 3, print total frauds. Easy for us, as its all conveniently stored in an instance variable!
def total_fraud():
    list = parse_to_list()
    total = 0
    for transaction in list:
        if transaction.fraud == '1':
            total += 1
    return total


# task 4, We need to make our last method take a parameter that lets the user choose wether to see non-frauds as well.
# we'll just go ahead and make an if statement to decide what we're looking for.
def total_fraud_flex(fraudbool=True):
    list = parse_to_list()
    total = 0
    if fraudbool:
        for transaction in list:
            if transaction.fraud == '1':
                total += 1
    else:
        for transaction in list:
            if transaction.fraud == '0':
                total += 1
    return total


# on task 5, we have to check the amount of frauds for a given merchant and return that. We do that by taking our
# last method, slapping a new parameter to hold the merchant we're looking for, and checking for that merchant on each line.
def merchant_fraud(merchant, fraudbool=True):
    list = parse_to_list()
    total = 0
    if fraudbool:
        for transaction in list:
            if transaction.merchant == merchant and transaction.fraud == '1':
                total += 1
    else:
        for transaction in list:
            if transaction.merchant == merchant and transaction.fraud == '0':
                total += 1
    return total


def return_fruadulant_transactions(merchant, fraudbool=True):
    list = parse_to_list()
    transactions = []
    if fraudbool:
        for transaction in list:
            if transaction.merchant == merchant and transaction.fraud == '1':
                transactions.append(transaction.body)
    else:
        for transaction in list:
            if transaction.merchant == merchant and transaction.fraud == '0':
                transactions.append(transaction.body)
    return transactions


'''a very, very slow algorithm with similar properties of a selection algorithm. Not my best work, but i was a wee coder at this point.'''


def list_sort_amounts():
    baselist = parse_to_list()
    sortedlist = []
    for transaction in baselist:
        if len(sortedlist) == 0:
            sortedlist.append(baselist.pop(baselist.index(transaction)))
            continue
        for completed in sortedlist:
            print(len(sortedlist))
            try:
                if transaction.amount > completed.amount:
                    sortedlist.insert(sortedlist.index(completed) - 1, transaction)
                    break
                if transaction.amount == completed.amount:
                    sortedlist.insert(sortedlist.index(completed), transaction)
                    break
                if transaction.amount < completed.amount and sortedlist.index(completed) + 1 == len(sortedlist):
                    sortedlist.append(transaction)
                else:
                    continue
            except(IndexError):
                sortedlist.append(transaction)
    return sortedlist


# a task to find the percent of a gender that commits fraud.
def gender_fraud(gender='m'):
    totalfraud = total_fraud()
    list = parse_to_list()
    genderfraud = 0
    if gender == 'm':
        for transaction in list:

            if transaction.gender == '\'M\'' and transaction.fraud == '1':
                genderfraud += 1
            else:
                continue

    elif gender == 'f':
        for transaction in list:
            if transaction.gender == '\'F\'' and transaction.fraud == '1':
                genderfraud += 1
            else:
                continue
    else:
        return 'this is not a valid gender!'
    return round((genderfraud / totalfraud) * 100)


def customer_frauds():
    list = parse_to_list()
    customersfraudtotals = {}
    for i in list:
        if i.customer not in customersfraudtotals:
            customersfraudtotals.update({'{}'.format(i.customer): 0})
        if i.fraud == '1':
            customersfraudtotals.update({'{}'.format(i.customer): customersfraudtotals['{}'.format(i.customer)] + 1})
        else:
            continue
    return customersfraudtotals


def checkfrauds(target):
    saltyjims = []
    fraudsdict = customer_frauds()
    for key, value in fraudsdict.items():
        if value >= target:
            saltyjims.append(key)
    return saltyjims


def merchant_frauds():
    list = parse_to_list()
    merchantfraudtotals = {}
    for i in list:
        if i.merchant not in merchantfraudtotals:
            merchantfraudtotals.update({'{}'.format(i.merchant): 0})
        if i.fraud == '1':
            merchantfraudtotals.update({'{}'.format(i.merchant): merchantfraudtotals['{}'.format(i.merchant)] + 1})
        else:
            continue
    return merchantfraudtotals


print(merchant_frauds())
