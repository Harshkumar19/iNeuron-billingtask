from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/bill", methods=['POST'])
def billing():
    if (request.method == 'POST'):
        item1 = int(request.json['item1'])
        item2 = int(request.json['item2'])
        item3 = int(request.json['item3'])
        item4 = int(request.json['item4'])
        item5 = int(request.json['item5'])
        item6 = int(request.json['item6'])

        total_cost = int(item1+item2+item3+item4+item5+item6)

        # return "Your total bill is {}".format(total_cost)
        if total_cost <= 1000:
            final_bill = total_cost - (total_cost/100*10)
        elif total_cost <= 2000 and total_cost > 1000:
            final_bill = total_cost - (total_cost/100*20)
        else:
            final_bill = total_cost - (total_cost/100*30)

        return "Total Billing amount {}".format(final_bill)


@app.route("/billing", methods=['POST'])
def bill_final():
    if (request.method == 'POST'):
        item1 = int(request.form['item1'])
        item2 = int(request.form['item2'])
        item3 = int(request.form['item3'])
        item4 = int(request.form['item4'])
        item5 = int(request.form['item5'])
        item6 = int(request.form['item6'])

        total_cost = int(item1+item2+item3+item4+item5+item6)

        # return "Your total bill is {}".format(total_cost)
        if total_cost <= 1000:
            final_bill = total_cost - (total_cost/100*10)
        elif total_cost <= 2000 and total_cost > 1000:
            final_bill = total_cost - (total_cost/100*20)
        else:
            final_bill = total_cost - (total_cost/100*30)

        return render_template('result.html', final_bill=final_bill)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
