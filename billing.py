'''
Created on Feb 3, 2014

@author: wongpiti
'''
import datetime
import mongoengine as me

class ServicePlan(me.Document):
    meta = {'collection': 'service_plans'}
    
    name        = me.StringField(max_length=100, required=True)
    description = me.StringField()
    server_cost = me.FloatField()
    office_rent = me.FloatField()
    consume_cost = me.FloatField()
    salary = me.FloatField()
    internet_service_charge = me.FloatField()
    colocation_service_charge = me.FloatField()
    profit = me.FloatField()
    status = me.StringField(required=True, default='active')
    sell_price_per_minute = me.FloatField()
    scaling_factor = me.FloatField(required=True, default=0.5)
    default = me.BooleanField(required=True, default=False)
