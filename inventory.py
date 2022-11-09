@app.route('/inventory')
def inventory():
    cursor = mysql.connection.cursor()
    res = cursor.execute("SELECT * FROM inventory WHERE user = %s ORDER BY prodname", (session['username'], ))
    data = cursor.fetchall()
    total1 = cursor.execute("SELECT * FROM inventory WHERE user = %s", (session['username'], ))
    total2 = 0
    cursor.execute("SELECT quantity FROM inventory WHERE user = %s", (session['username'], ))
    q = cursor.fetchall()
    cursor.execute("SELECT sprice FROM inventory WHERE user = %s", (session['username'], ))
    sp = cursor.fetchall()
    print(q)
    print(sp)
    q1 = []
    sp1 = []
    for i in q:
        q1.append(i[0])
    for i in sp:
        sp1.append(i[0])
    print(q1)
    print(sp1)
    for i in  range(len(q1)):
        total2 += (q1[i] * sp1[i])
    print(total2)
    cursor.close()
    
    if res > 0:
        return render_template('inventory.html', data = data, total1 = total1, total2 = total2)
    else:
        msg = "No stock found."
        return render_template('inventory.html', msg = msg, total1 = total1, total2 = total2)