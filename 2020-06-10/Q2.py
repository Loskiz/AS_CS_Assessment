#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:17:25 2020

@author: zlt
"""


class SMS_store():
    def __init__(self, messages=[]):
        
        self.msgs=messages
    def add_new_arrival(self,from_number, time_arrived, text_of_SMS):
        has_been_viewed=False
        self.megs.append((has_been_viewed, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        return(len(self.msgs))
        
    def get_unread_indexes(self):
        l=[]
        for i in range(len(self.msgs)):
            if self.msgs[i][0]==False:
                l.append(i)
        return l
    
    def get_message(self,i):
        return self.msgs[i]
    
    def delete(self,i):
        del(self.msgs[i])
    
    def clear(self):
        self.megs=[]