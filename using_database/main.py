from flask import Flask, redirect, render_template, request
from flaskext.mysql import MySQL  
from models import ProductModel,ModelFactory, MySQLSingleton 
import pymysql


app = Flask(__name__, template_folder='views')
app.secret_key = 'zineddine'


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'mti-crud'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


mysql = MySQLSingleton.get_instance()
mysql.init_app(app)  
product_model = ModelFactory.create_model('product', mysql)

@app.route('/')
def home():
    products = product_model.fetch_product() 
    return render_template('users.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    text = ''
    if request.method == 'POST' and 'productname' in request.form and 'amount' in request.form and 'price' in request.form:
        productname = request.form['productname']
        amount = request.form['amount']
        price = request.form['price']
        total_price = float(amount) * float(price) 


        conn = mysql.connect()
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute("SELECT * FROM product WHERE productname = %s", (productname,))
        product = cur.fetchone()

        if product:
            text = "Product already exists"
        else:
            
            product_model.create_product(productname, amount, price, total_price)
            text = "Product successfully added!"
            return redirect('/')  

    elif request.method == 'POST':
        text = "Fill in the forms"
    
    return render_template('users.html', text=text)




@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = None
    conn = mysql.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT * FROM product WHERE id = %s", (id,))
    product = cur.fetchone()

    
    if request.method == 'POST':
        productname = request.form['productname']
        amount = request.form['amount']
        price = request.form['price']
        total_price = float(amount) * float(price)  
        
        
        product_model.update_product(productname, amount, price, total_price, id)
        
        
        return redirect('/')  

    
    return render_template('users.html', product=product)


@app.route('/delete_product/<int:id>', methods=['GET'])
def delete_product_controller(id):
    product_model.delete_product(id)  
    return redirect('/')  

if __name__ == '__main__':
    app.run(debug=True)
