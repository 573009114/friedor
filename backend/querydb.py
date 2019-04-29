# -*- coding: utf-8 -*-
from models import *

class MemberForm:
    def __init__(self,**kwargs):
        self.name=kwargs.get('name')
        self.tel=kwargs.get('tel')
        self.address=kwargs.get('address')
        self.vipid=kwargs.get('vipid')
        self.id=kwargs.get('id')

    def view_member_list(self):
        result=Members.objects.all()
        return result

    def post_member(self):
        result=Members.objects.create(name=self.name,mobel=self.tel,secret=self.vipid,address=self.address)
        result.save()
        return result.id
    def delete_member(self):
        try:
            Members.objects.filter(id=self.id).delete()
            return bool('True')
        except:
            return bool('False')
            