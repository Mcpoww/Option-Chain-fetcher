
# coding: utf-8

# In[254]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[255]:


r=requests.get('https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-10006&symbol=NIFTY&symbol=NIFTY&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17#')
c=r.content


# In[256]:


soup=BeautifulSoup(c,'html.parser')


# In[257]:


table_it=soup.find_all(class_='opttbldata')
table_cls_1=soup.find_all(id='octable')


# In[258]:


col_list=[]


# In[259]:


for mytable in table_cls_1:
    table_head=mytable.find('thead')
    
    try:
        rows=table_head.find_all('tr')
        for tr in rows:
            cols=tr.find_all('th')
            for th in cols:
                er=th.text
                ee = er.encode('utf8')   
                ee = str(ee, 'utf-8')
                col_list.append(ee)
    except:
        print('no thead')


# In[260]:


cols_list_fnl=[e for e in col_list if e not in('CALLS','PUTS','Chart','\xa2\xa0','\xa0')]
print (cols_list_fnl)


# In[280]:


table_cls_2=soup.find_all(id='octable')
tablall_trs=soup.find_all('tr')
req_row=soup.find_all('tr')
new_table2=pd.DataFrame(index=range(0,len(req_row)-80),columns=cols_list_fnl)
row_marker=0


# In[282]:



for row_number, tr_nos in enumerate(req_row):
    
     
    # This ensures that we use only the rows with values    
    if row_number <=1 or row_number == len(req_row)-1:   
        pass
          
    td_columns = tr_nos.find_all('td')
     
     # This removes the graphs columns
    select_cols = td_columns[1:22]                  
    cols_horizontal = range(0,len(select_cols))
      
    for nu, column in enumerate(select_cols):
        
         
        utf_string = column.get_text()
        utf_string = utf_string.strip('\n\r\t": ')
         
        tr = utf_string.encode('utf-8')
        tr = str(tr, 'utf-8')
        tr = tr.replace(',' , '')
        new_table2.ix[row_marker,[nu]]= tr
         
    row_marker += 1   
          
new_table2.to_csv('Downloads/Option_Chain_Table14.csv')


# In[279]:


new_table


# In[184]:


a=['1','2','3']
list(enumerate(a))

