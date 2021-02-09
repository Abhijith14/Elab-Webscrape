# ONLY FOR OOPS
# DONT COPY !!!!!!
#!!!!!
#!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!OOPS CONCEPT ELAB!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import mysql.connector

def url_return(num):
    numberIter = 1
    uN = 2411110
    oN = 2411110
    for h in range(1, 301):
        noF = uN + numberIter
        numberIter = numberIter + 1
        if h == 100:
            uN = oN + 100;
            numberIter = 1
        elif h == 200:
            uN = oN + 200;
            numberIter = 1
        elif h == 300:
            uN = oN + 300;
            numberIter = 1
        elif h % 10 == 0:
            uN = uN + 1000
            numberIter = 1
        #print(noF)
        if h == num:
            return noF



mydb = mysql.connector.connect(
    host="HOST",
        database="DATABASE",
        user="USER",
        password="PASSWORD"
)

mycursor = mydb.cursor()


driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
driver.get("https://care.srmist.edu.in/srmstudentskill/login")
n = input("Enter Confirmation ")
maindata = []
maintestcase_data = []
skippeddata = []
codedata = []
number = 1
url_no = 2411110
old_url = 2411110
for i in range(1,11):
    title = []
    answer = []
    IO = []
    mainlist = []
    codelist = []
    codestr = ""
    print("-----------------------------------------------------")
    print("Loading Question ",i)
    print("-----------------------------------------------------")
    url = "https://care.srmist.edu.in/srmstudentskill/student/solve/"

    no = url_no + number
    number = number + 1

    if i == 100:
        url_no = old_url + 100;
        number = 1
    elif i == 200:
        url_no = old_url + 200;
        number = 1
    elif i == 300:
        url_no = old_url + 300;
        number = 1

    elif i%10 == 0:
        url_no = url_no + 1000
        number = 1

    url = url + str(no)
    driver.execute_script("window.open('https://www.google.com');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)
    sleep(2)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html5lib")
    print("SOup is .....")
    print(soup)
    print("END of SOup")
    # print(soup.findAll('div', attrs={'class':'list-item'}))
    # print(len(soup.findAll('div', attrs={'class':'list-item'})))
    if soup.findAll('div', attrs={'class': 'list-item'}):
        for a in soup.findAll('div', attrs={'class': 'list-item'}):
            title_sub = a.find('a', attrs={'class': 'title'})
            # print(title_sub.text)
            ans_sub = a.findAll('a', attrs={'_ngcontent-c16': ''})
            # print(ans_sub[1].text)
            title.append(title_sub.get_text(separator="<br>").strip())
            answer.append(ans_sub[1].get_text(separator="<br>").strip())
        print(title)
        print(answer)
        for b in soup.findAll('div', attrs={'class': 'list-item ng-star-inserted'}):
            name = b.findAll('code', attrs={'_ngcontent-c16': ''})
            for n in name:
                IO.append(n.get_text(separator="<br>").strip())
        print(IO)
        count = 3
        for j in range(0, len(IO), 2):
            maintestcase = []
            maintestcase.append(i)
            maintestcase.append(title[count])
            maintestcase.append(IO[j])
            maintestcase.append(IO[j + 1])
            count = count + 1
            maintestcase = list(maintestcase)
            maintestcase_data.append(maintestcase)
            print(maintestcase)
        mainlist.append(i)
        mainlist.append(answer[0])
        mainlist.append(title[1])
        mainlist.append(answer[1])
        mainlist.append(answer[2])
        # mainlist = list(mainlist)

        # maindata.append(mainlist)

        for c in soup.findAll('pre', attrs={'role': 'presentation'}):
            code_sub = c.findAll('span', attrs={'role': 'presentation'})
            for codei in code_sub:
                codelist.append(codei.get_text().strip())
            # print(codelist)
        for l in codelist:
            codestr = codestr + l
            codestr = codestr + "<br>"
        #print(codestr)
        start = codestr.find("#include")
        #print(start)
        #print(codestr[start:])
        mainlist.append(codestr[start:])
        # print(mainlist)

        mainlist = list(mainlist)
        maindata.append(mainlist)

    else:
        print("Skipped", i)
        skippeddata.append(i)

print(maindata)
print(maintestcase_data)
print()
print("-----------------------------------------------------------------")
print(str(len(maindata)) + " Questions Loaded Successfully")
print(str(len(skippeddata)) + " Questions Skipped...")
if len(skippeddata) > 0:
    print("List of skipped data is ")
    print(skippeddata)
print("-----------------------------------------------------------------")

save = input("Do you want to save to database ?(yes|no)")
if save == "yes":
    sqlformula1 = "INSERT INTO elabdata (id, SESSION, QUESTION_NO, QUESTION_NAME, QUESTION_DESC, CODE) VALUES (%s, %s, %s, %s, %s, %s)"
    mycursor.executemany(sqlformula1, maindata)

    sqlformula2 = "INSERT INTO elabtestcase (dataid, TESTCASE_NO, INPUT, OUTPUT) VALUES (%s, %s, %s, %s)"
    mycursor.executemany(sqlformula2, maintestcase_data)

    mydb.commit()
    print("Loaded to database")
    print(maindata)
    print(maintestcase_data)
    maindata = []
    maintestcase_data = []
recheck = input("Do you want to recheck the skipped questions ?")
if recheck == "yes":
    single = ""
    while (single != 'c'):
        single = input("Enter the question NO to add (if all enter 'all' | if cancel enter 'c')")
        if single == "all":
            for i in skippeddata:
                title = []
                answer = []
                IO = []
                mainlist = []
                codelist = []
                codestr = ""
                print("-----------------------------------------------------")
                print("Loading Question ", i)
                print("-----------------------------------------------------")
                url_no = url_return(i)
                url = "https://care.srmist.edu.in/srmstudentskill/student/solve/"

                url = url + str(url_no)
                driver.execute_script("window.open('https://www.google.com');")
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(url)
                sleep(2)
                content = driver.page_source
                soup = BeautifulSoup(content, features="html5lib")
                # print(soup.findAll('div', attrs={'class':'list-item'}))
                # print(len(soup.findAll('div', attrs={'class':'list-item'})))
                if soup.findAll('div', attrs={'class': 'list-item'}):
                    for a in soup.findAll('div', attrs={'class': 'list-item'}):
                        title_sub = a.find('a', attrs={'class': 'title'})
                        # print(title_sub.text)
                        ans_sub = a.findAll('a', attrs={'_ngcontent-c16': ''})
                        # print(ans_sub[1].text)
                        title.append(title_sub.get_text(separator="<hahahaha>").strip())
                        answer.append(ans_sub[1].get_text(separator="<hahahaha>").strip())
                    print(title)
                    print(answer)
                    for b in soup.findAll('div', attrs={'class': 'list-item ng-star-inserted'}):
                        name = b.findAll('code', attrs={'_ngcontent-c16': ''})
                        for n in name:
                            IO.append(n.get_text(separator="<hahahaha>").strip())
                    print(IO)
                    count = 3
                    for j in range(0, len(IO), 2):
                        maintestcase = []
                        maintestcase.append(i)
                        maintestcase.append(title[count])
                        maintestcase.append(IO[j])
                        maintestcase.append(IO[j + 1])
                        count = count + 1
                        maintestcase = list(maintestcase)
                        maintestcase_data.append(maintestcase)
                        print(maintestcase)
                    mainlist.append(i)
                    mainlist.append(answer[0])
                    mainlist.append(title[1])
                    mainlist.append(answer[1])
                    mainlist.append(answer[2])
                    # mainlist = list(mainlist)

                    # maindata.append(mainlist)

                    for c in soup.findAll('pre', attrs={'role': 'presentation'}):
                        code_sub = c.findAll('span', attrs={'role': 'presentation'})
                        for codei in code_sub:
                            codelist.append(codei.get_text().strip())
                        # print(codelist)
                    for l in codelist:
                        codestr = codestr + l
                        codestr = codestr + "&#13;&#10;"
                    # print(codestr)
                    mainlist.append(codestr)
                    # print(mainlist)

                    mainlist = list(mainlist)
                    maindata.append(mainlist)

                else:
                    print("Skipped", i)
                    skippeddata.append(i)

            print(maindata)
            print(maintestcase_data)
            print()
            print("-----------------------------------------------------------------")
            print(str(len(maindata)) + " Questions Loaded Successfully")
            print(str(len(skippeddata)) + " Questions Skipped...")
            if len(skippeddata) > 0:
                print("List of skipped data is ")
                print(skippeddata)
            print("-----------------------------------------------------------------")

            save = input("Do you want to save to database ?(yes|no)")
            if save == "yes":
                #sqlformula1 = "INSERT INTO elabdata (id, SESSION, QUESTION_NO, QUESTION_NAME, QUESTION_DESC, CODE) VALUES (%s, %s, %s, %s, %s, %s)"
                #mycursor.executemany(sqlformula1, maindata)

                #sqlformula2 = "INSERT INTO elabtestcase (dataid, TESTCASE_NO, INPUT, OUTPUT) VALUES (%s, %s, %s, %s)"
                #mycursor.executemany(sqlformula2, maintestcase_data)

                #mydb.commit()
                print("Loaded to database")
                print(maindata)
                print(maintestcase_data)
                maindata = []
                maintestcase_data = []
            else:
                print("Exited with nothing saved...")

        elif single == 'c':
            print("Cancelled !!")
            break

        else:
            title = []
            answer = []
            IO = []
            mainlist = []
            codelist = []
            codestr = ""
            print("-----------------------------------------------------")
            print("Loading Question ", single)
            print("-----------------------------------------------------")
            url_no = url_return(single)
            url = "https://care.srmist.edu.in/srmstudentskill/student/solve/"

            url = url + str(url_no)
            driver.execute_script("window.open('https://www.google.com');")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(url)
            sleep(2)
            content = driver.page_source
            soup = BeautifulSoup(content, features="html5lib")
            # print(soup.findAll('div', attrs={'class':'list-item'}))
            # print(len(soup.findAll('div', attrs={'class':'list-item'})))
            if soup.findAll('div', attrs={'class': 'list-item'}):
                for a in soup.findAll('div', attrs={'class': 'list-item'}):
                    title_sub = a.find('a', attrs={'class': 'title'})
                    # print(title_sub.text)
                    ans_sub = a.findAll('a', attrs={'_ngcontent-c16': ''})
                    # print(ans_sub[1].text)
                    title.append(title_sub.get_text(separator="(br)").strip())
                    answer.append(ans_sub[1].get_text(separator="(br)").strip())
                print(title)
                print(answer)
                for b in soup.findAll('div', attrs={'class': 'list-item ng-star-inserted'}):
                    name = b.findAll('code', attrs={'_ngcontent-c16': ''})
                    for n in name:
                        IO.append(n.get_text(separator="(br)").strip())
                print(IO)
                count = 3
                for j in range(0, len(IO), 2):
                    maintestcase = []
                    maintestcase.append(i)
                    maintestcase.append(title[count])
                    maintestcase.append(IO[j])
                    maintestcase.append(IO[j + 1])
                    count = count + 1
                    maintestcase = list(maintestcase)
                    maintestcase_data.append(maintestcase)
                    print(maintestcase)
                mainlist.append(i)
                mainlist.append(answer[0])
                mainlist.append(title[1])
                mainlist.append(answer[1])
                mainlist.append(answer[2])
                # mainlist = list(mainlist)

                # maindata.append(mainlist)

                for c in soup.findAll('pre', attrs={'role': 'presentation'}):
                    code_sub = c.findAll('span', attrs={'role': 'presentation'})
                    for codei in code_sub:
                        codelist.append(codei.get_text().strip())
                    # print(codelist)
                for l in codelist:
                    codestr = codestr + l
                    codestr = codestr + "(br)"
                # print(codestr)
                mainlist.append(codestr)
                # print(mainlist)

                mainlist = list(mainlist)
                maindata.append(mainlist)

            else:
                print("Skipped", i)
                skippeddata.append(i)

            print(maindata)
            print(maintestcase_data)
            print()
            print("-----------------------------------------------------------------")
            print(str(len(maindata)) + " Questions Loaded Successfully")
            print(str(len(skippeddata)) + " Questions Skipped...")
            if len(skippeddata) > 0:
                print("List of skipped data is ")
                print(skippeddata)
            print("-----------------------------------------------------------------")

            save = input("Do you want to save to database ?(yes|no)")
            if save == "yes":
                #sqlformula1 = "INSERT INTO elabdata (id, SESSION, QUESTION_NO, QUESTION_NAME, QUESTION_DESC, CODE) VALUES (%s, %s, %s, %s, %s, %s)"
                #mycursor.executemany(sqlformula1, maindata)

                #sqlformula2 = "INSERT INTO elabtestcase (dataid, TESTCASE_NO, INPUT, OUTPUT) VALUES (%s, %s, %s, %s)"
                #mycursor.executemany(sqlformula2, maintestcase_data)

                #mydb.commit()
                print("Loaded to database")
                print(maindata)
                print(maintestcase_data)
                maindata = []
                maintestcase_data = []
            else:
                print("Exited with nothing saved...")




