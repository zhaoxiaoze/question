import xlwt
import re



new_workbook = xlwt.Workbook()
new_sheet = new_workbook.add_sheet('questionandanswer')



result = []
questions = []
raw_message=[]
answer_message=[]




i = 0




for line in open('question'):


    if line[0]=='问' and line[1]=='题':

        raw_message = [line]

        questions = raw_message

        new_sheet.write(i, 0, questions)
        i = i+1



    else:

        answer_message = [line]
        result = answer_message
        new_sheet.write(i, 1, result)
        i =i+1



new_workbook.save(r"questionandanswer.xls")