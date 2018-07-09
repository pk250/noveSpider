# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3,sys

class NovePipeline(object):
    def open_spider(self,spider):
         self.conn=sqlite3.connect('Nove.db')
         self.cur=self.conn.cursor()
    def close_spider(self,spider):
        self.conn.close()
    def process_item(self, item, spider):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        if item.keys()[0]=='Surl':
            insert_sql = "insert into Selist(nid,title,surl,sid) VALUES ('{0}','{1}','{2}','{3}')".format(item['nid'],item['Title'], item['Surl'],item['sid'])
        else:
            insert_sql="insert into name(nid,name,nurl) VALUES ('{0}','{1}','{2}')".format(item['nid'],item['Name'],item['Nurl'])
        self.cur.execute(insert_sql)
        self.conn.commit()
        print (item.keys()[0])
        return item
