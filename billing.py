'''
Created on Feb 3, 2014

@author: wongpiti
'''
import datetime
from mongoengine import *

class ServicePlan(Document):
    meta = {'collection': 'service_plans'}
    
    name        = StringField(max_length=100, required=True)
    description = StringField()
    server_cost = FloatField()
    office_rent = FloatField()
    consume_cost = FloatField()
    salary = FloatField()
    internet_service_charge = FloatField()
    colocation_service_charge = FloatField()
    profit = FloatField()
    status = StringField(required=True, default='active')
    sell_price_per_minute = FloatField()