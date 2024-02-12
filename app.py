from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    connection = sqlite3.connect('visual.db')
    cursor = connection.cursor()

    data1, data2 ,data3,data4,data5= None, None,None,None,None  # Initialize to None in case no form is submitted
    selected_option=None

    if selected_option==None:
            cursor.execute('SELECT country, end_year FROM jsondata GROUP BY country')
            data1 = cursor.fetchall()
            cursor.execute('SELECT country, start_year FROM jsondata GROUP BY country')
            data2 = cursor.fetchall()
            cursor.execute('SELECT country, likelihood FROM jsondata GROUP BY country')
            data3 = cursor.fetchall()
            cursor.execute('SELECT country, relevance FROM jsondata GROUP BY country')
            data4 = cursor.fetchall()
            cursor.execute('SELECT country, intensity FROM jsondata GROUP BY country')
            data5 = cursor.fetchall()

    
    if request.method == 'POST':
        selected_option=request.form.get("category")

        if selected_option=="country":
            cursor.execute('SELECT country, end_year FROM jsondata GROUP BY country')
            data1 = cursor.fetchall()
            cursor.execute('SELECT country, start_year FROM jsondata GROUP BY country')
            data2 = cursor.fetchall()
            cursor.execute('SELECT country, likelihood FROM jsondata GROUP BY country')
            data3 = cursor.fetchall()
            cursor.execute('SELECT country, relevance FROM jsondata GROUP BY country')
            data4 = cursor.fetchall()
            cursor.execute('SELECT country, intensity FROM jsondata GROUP BY country')
            data5 = cursor.fetchall()

        elif selected_option=="region":
            cursor.execute('SELECT region, end_year FROM jsondata GROUP BY region')
            data1 = cursor.fetchall()
            cursor.execute('SELECT region, start_year FROM jsondata GROUP BY region')
            data2 = cursor.fetchall()
            cursor.execute('SELECT region, likelihood FROM jsondata GROUP BY region')
            data3 = cursor.fetchall()
            cursor.execute('SELECT region, relevance FROM jsondata GROUP BY region')
            data4 = cursor.fetchall()
            cursor.execute('SELECT region, intensity FROM jsondata GROUP BY region')
            data5 = cursor.fetchall()
        elif selected_option=="topic":
            cursor.execute('SELECT topic, end_year FROM jsondata GROUP BY topic')
            data1 = cursor.fetchall()
            cursor.execute('SELECT topic, start_year FROM jsondata GROUP BY topic')
            data2 = cursor.fetchall()
            cursor.execute('SELECT topic, likelihood FROM jsondata GROUP BY topic')
            data3 = cursor.fetchall()
            cursor.execute('SELECT topic, relevance FROM jsondata GROUP BY topic')
            data4 = cursor.fetchall()
            cursor.execute('SELECT topic, intensity FROM jsondata GROUP BY topic')
            data5 = cursor.fetchall()

        elif selected_option=="pestle":
            cursor.execute('SELECT pestle, end_year FROM jsondata GROUP BY pestle')
            data1 = cursor.fetchall()
            cursor.execute('SELECT pestle, start_year FROM jsondata GROUP BY pestle')
            data2 = cursor.fetchall()
            cursor.execute('SELECT pestle, likelihood FROM jsondata GROUP BY pestle')
            data3 = cursor.fetchall()
            cursor.execute('SELECT pestle, relevance FROM jsondata GROUP BY pestle')
            data4 = cursor.fetchall()
            cursor.execute('SELECT pestle, intensity FROM jsondata GROUP BY pestle')
            data5 = cursor.fetchall()

        elif selected_option=="source":
            cursor.execute('SELECT source, end_year FROM jsondata GROUP BY source')
            data1 = cursor.fetchall()
            cursor.execute('SELECT source, start_year FROM jsondata GROUP BY source')
            data2 = cursor.fetchall()
            cursor.execute('SELECT source, likelihood FROM jsondata GROUP BY source')
            data3 = cursor.fetchall()
            cursor.execute('SELECT source, relevance FROM jsondata GROUP BY source')
            data4 = cursor.fetchall()
            cursor.execute('SELECT source, intensity FROM jsondata GROUP BY source')
            data5 = cursor.fetchall()
        
        elif selected_option=="sector":
            cursor.execute('SELECT sector, end_year FROM jsondata GROUP BY sector')
            data1 = cursor.fetchall()
            cursor.execute('SELECT sector, start_year FROM jsondata GROUP BY sector')
            data2 = cursor.fetchall()
            cursor.execute('SELECT sector, likelihood FROM jsondata GROUP BY sector')
            data3 = cursor.fetchall()
            cursor.execute('SELECT sector, relevance FROM jsondata GROUP BY sector')
            data4 = cursor.fetchall()
            cursor.execute('SELECT sector, intensity FROM jsondata GROUP BY sector')
            data5 = cursor.fetchall()
        

    connection.close()

    return render_template('index.html', data1=data1, data2=data2,data3=data3,data4=data4,data5=data5,selected_option=selected_option)


if __name__ == '__main__':
    app.run(debug=True)
