# -*- coding: utf-8 -*-

import datetime
import json

__author__ = 'gia_sebua'


class Storage(object):
    items = None
    _obj = None
    json_file = 'database.json'

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = object.__new__(cls)
            cls.items = []
            try:
                with open(cls.json_file, 'r') as file:
                    cls.items = json.load(file)
            except:
                pass
        return cls._obj

    @classmethod
    def add(cls, item):
        cls.items.append(item)
        with open(cls.json_file, 'w+') as file:
            json.dump(cls.items, file)


class BlogPostModel(object):
    def __init__(self, form_data):
        self.title = form_data['title']
        self.text = form_data['text']
        self.time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.author = form_data['author']

    def to_dict(self):
        return {'title': self.title, 'text': self.text, 'data': self.time_stamp, 'author': self.author}

