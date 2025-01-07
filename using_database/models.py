from flask import Flask, render_template, session
from flaskext.mysql import MySQL
import pymysql

class MySQLSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if MySQLSingleton._instance is None:
            MySQLSingleton._instance = MySQL()
        return MySQLSingleton._instance


class ProductModel:
    def __init__(self, mysql):
        self.mysql = mysql

    def create_product(self, productname, amount, price, total_price):
        conn = self.mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("INSERT INTO product(productname, amount, price, total_price) VALUES (%s, %s, %s, %s)", (productname, amount, price, total_price))
        conn.commit()

    def fetch_product(self):
        conn = self.mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM product")
        return cur.fetchall()

    def update_product(self, productname, amount, price, total_price, id):
        conn = self.mysql.connect()
        cur = conn.cursor()
        query = "UPDATE product SET productname = %s, amount = %s, price = %s, total_price = %s WHERE id = %s"
        cur.execute(query, (productname, amount, price, total_price, id))
        conn.commit()
        cur.close()
        conn.close()

    def delete_product(self, id):
        conn = self.mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("DELETE FROM product WHERE id = %s", (id,))
        conn.commit()

    
        

class ModelFactory:
    @staticmethod
    def create_model(model_name, mysql):
        if model_name == 'product':
            return ProductModel(mysql)
        else:
            raise ValueError(f"Model {model_name} not recognized.")