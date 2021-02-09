import mysql.connector

mydb = mysql.connector.connect(
    host="HOST",
        database="DATABASE",
        user="USER",
        password="PASSWORD"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE CSHARP")


mycursor.execute("CREATE TABLE elabdata (id INTEGER(100), SESSION VARCHAR(255), QUESTION_NO VARCHAR(100), QUESTION_NAME VARCHAR(255), QUESTION_DESC VARCHAR(3000), CODE VARCHAR(5000))")
mycursor.execute("CREATE TABLE elabtestcase (dataid INTEGER(100), TESTCASE_NO VARCHAR(100), INPUT VARCHAR(500), OUTPUT VARCHAR(500))")

#sqlformula = "INSERT INTO elabdata (id, SESSION, QUESTION_NO, QUESTION_NAME, QUESTION_DESC, CODE) VALUES (%s, %s, %s, %s, %s, %s)"
#data1 = (1,"Input and Output", "Q. 7", "Salary Calculator", "Help Raja to calculate a first salary that he got from thebrorganisation , he was confused with an salary credited inbrhis account .brHe asked his friend Ritu to identify how salary pay gotbrcalculated by giving the format of salary.brHis basic pay (to be entered by user) and Ritu developedbra software to calculate the salary pay,with format given asbrbelowbrHRA=80% of the basic pay,brdA=40% of basic paybrbonus = 25 % of hrabrInput and Output Format:brRefer sample input and output for formatting specification.brAll float values are displayed correct to 2 decimal places.brAll text in bold corresponds to input and the rest corresponds to output")
#mycursor.execute(sqlformula, data1)

#sqlformula = "INSERT INTO elabtestcase (id, dataid, TESTCASE_NO, INPUT, OUTPUT) VALUES (%s, %s, %s, %s, %s)"
#data1 = (2,1, 2, "sample.txtbr2breLab an auto evaluation tool in TamilnadubreLab will be launched in SWAYM platform soonbrsample.txt", "eLab will be launched in SWAYM platform soonbreLab an auto evaluation tool in Tamilnadubr")
#mycursor.execute(sqlformula, data1)

#mydb.commit()

