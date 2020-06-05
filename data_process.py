# -*- coding: utf-8 -*
import json
import pandas as pd
import re

df = pd.DataFrame(columns=('index','講義科目名','授業科目区分','授業概要'))
columns =['index','講義科目名','授業科目区分','授業概要']
i=0
with open('result1.json', 'r', encoding='utf-8') as f:

    try:
        while True:
            line = f.readline()
            if line:
                d = json.loads(line)
                name = d['講義科目名'].replace("\n", "")
                cate = d['授業科目区分'].replace("\n", "")
                content = d['授業概要'].replace("\n", "")
                content = content.replace("&#13; .none_display {&#13; display:none;&#13; }&#13;", "")
                uncn = re.compile(r'[\u0061-\u007a,\u0020]')
                en = "".join(uncn.findall(content.lower()))
                df=df.append(pd.DataFrame({'index':[i],'講義科目名':[name],'授業科目区分':[cate],'授業概要':[en]}))
                print(df)
                i=i+1
            else:
                break
    except:
        f.close()

df.to_csv('syllabus_en.csv', encoding='utf-8',index=False,columns=columns)
