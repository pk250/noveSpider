# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import sys

class NovePipeline(object):
    # def open_spider(self,spider):
    #      self.conn=sqlite3.connect('Nove.db')
    #      self.cur=self.conn.cursor()
    # def close_spider(self,spider):
    #     self.conn.close()
    def process_item(self, item, spider):
        # reload(sys)
        # sys.setdefaultencoding('utf-8')
        # insert_sql="insert into name(name,nurl) VALUES ('{}','{}')".format(item['Name'],item['Nurl'])
        # self.cur.execute(insert_sql)
        # self.conn.commit()
        return item
