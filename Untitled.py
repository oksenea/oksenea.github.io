#!/usr/bin/env python
# coding: utf-8

# In[3]:


number = 178
k = 0
for i in range(2, number//2+1):
    if (number % i == 0):
        print("Не является простым")
        k=k+1
        break  
    else:
        continue
if k==0:
    print("Простое")


# In[1]:


11111*1111111


# In[9]:


42/(4+(2*(-2)))


# In[15]:


round(0.3+0.3+0.3)


# In[10]:


2014**14


# In[16]:


print(0.3 + 0.3 + 0.3 == 0.9)


# In[6]:


otv=0
for i in range(5):
    string = 'Нет'
    if string!="да": #and otv!=4:
        otv=otv+1
        continue
    else:
        print("Это отлично!")    
        break       
if string!="да" and otv!=5:
      print("Увы, это неправильный ответ.")
else:  
      print("Это безнадёжно!")


# In[19]:


S = 'spam"s'
S
S = "spam's"
S


# In[28]:


string = 'прелестная строка'
p=0
glas=('а','у','о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
for i in range ( len ( string ) ):
    if (string[i] in glas) and ((i+2)%2==0):
        print("Строка мне не нравится!")
        p=p+1
        break
    else:
        continue
if p==0:
    print("Какая хорошая строка!")


# In[29]:


money = 1
year = 0
yearly_multiplier = 1.06

while money < 2:
    money = money*yearly_multiplier
    year += 1
else:
    print('Деньги удвоятся через', year, 'лет')


# In[20]:


# добавьте номера телефонов в список phones
phones = ['+79033923029', '+78125849204', '+79053049385', '+79265748370', '+79030598495']


# In[40]:


country=['Египет','Россия','Португалия','Франция','Дания','Италия']
group = []
group_spisok={}
drawdict = {'Россия': 'A','Португалия': 'B','Франция': 'C','Дания': 'C','Египет': 'A'}
for i in country:
    if i in drawdict:
        group_list.append(drawdict[i])
        group_spisok[i] = (drawdict[i])
    else:
        group.append('unknown')
        group_spisok[i] = ('unknown')
        
print(group_list,group_spisok)


# In[52]:


employee_base = {'Мария Никитина': 'разработчик', 'Егор Савичев': 'разработчик', 'Александр Пахомов': 'дизайнер', 'Алина Егорова': 'разработчик', 'Руслан Башаров': 'верстальщик'}
k=0
'''for employee in employee_base.keys():
    print(employee, employee_base[employee])'''
for position in employee_base.values():
    if position=='разработчик':
        k+=1
print('В компании {} разработчик:' .format(k))
for employee, position in employee_base.items():
    if position == 'разработчик':
        print(employee)


# In[53]:


phones = {
	'Гордиенко Виктория': 5140,
	'Анисимов Кирилл': 5145,
	'Кузнецова Дарья': 5142
}
type(phones)


# In[57]:


mylist=[['a','b','c'],['d','e','f'],['j','h','i']]
for x in mylist:
    print(x[1])


# In[61]:


csv_dict = [
    {'id': '100412', 'position': 'Ботинки для горных лыж ATOMIC Hawx Prime 100', 'count': 9},
    {'id': '100728', 'position': 'Скейтборд Jdbug RT03', 'count': 32},
    {'id': '100732', 'position': 'Роллерсерф Razor RipStik Bright', 'count': 11},
    {'id': '100803', 'position': 'Ботинки для сноуборда DC Tucknee', 'count': 20},
    {'id': '100898', 'position': 'Шагомер Omron HJA-306', 'count': 2},
    {'id': '100934', 'position': 'Пульсометр Beurer PM62', 'count': 17},
]
csv_dict_boots=[]
for dic in csv_dict:
    for key,value in dic.items():
        if key.index==1 and 'Ботинки' in value:
            csv_dict_boots.append(dic)
print(csv_dict_boots)


# In[77]:


k=1
defect_stats = [
	{'step number': 1, 'damage': 0.98},
	{'step number': 2, 'damage': 0.99},
	{'step number': 3, 'damage': 0.99},
	{'step number': 4, 'damage': 0.96},
	{'step number': 5, 'damage': 0.97},
	{'step number': 6, 'damage': 0.97},
]
for i in defect_stats:
    k=k*i['damage']
    if k<0.9:
        print(i['step number'])   
        break


# In[155]:


currency = {
	'AMD': {
		'Name': 'Армянских драмов',
		'Nominal': 100,
		'Value': 13.121
	},

	'AUD': {
		'Name': 'Австралийский доллар',
		'Nominal': 1,
		'Value': 45.5309
	},

	'INR': {
		'Name': 'Индийских рупий',
		'Nominal': 100,
		'Value': 92.9658
	},

	'MDL': {
		'Name': 'Молдавских леев',
		'Nominal': 10,
		'Value': 36.9305
	},
}
kyrs=[]
ky={}
a=0
aa=0
for values in currency:
    #print(values,'\n',currency[values])
    #for x in currency[values]:
        #print(x,currency[values][x])
    kyrs.append(currency[values]['Value']/currency[values]['Nominal'])
    k[values]=(currency[values]['Value']/currency[values]['Nominal'])
    print(kyrs)
print(ky)
aa=min(ky, key = lambda k: ky[k])
a=min(kyrs)
print(a,aa)
for values in currency:
    for x in currency[values]:
        if currency[values][x]==a:
            print(x)


# In[145]:


p_ages = {"Андрей": 32, "Виктор": 29, "Максим": 18}
a = p_ages.items()
print(a)


# In[212]:


results = [
	{'cost': 98, 'source': 'vk'},
	{'cost': 153, 'source': 'yandex'},
	{'cost': 110, 'source': 'facebook'},
]
k=[]
kk={}
for i in results:
	#k.append(i['cost'])
	kk[i['source']]=i['cost']
print(kk)
a=0
aa=0
aa=min(kk.values())
a=[key for key in kk if kk[key]==aa]
print('Минимальные затраты на ресурсе {0} и равны {1}'.format(a,aa))


# In[215]:


results = [
	{'cost': 98, 'source': 'vk'},
	{'cost': 153, 'source': 'yandex'},
	{'cost': 110, 'source': 'facebook'},
]
k={}
asp=[]
for i in results:
    del asp[:]
    for j in i:        
        asp.append(i[j])
    k[asp[1]]=asp[0]

print(k)


print('Минимальные затраты на ресурсе {0} и равны {1}'.format([key for key in k if k[key]==aa],min(k.values())))


# In[173]:


currency = {
	'AMD': {
		'Name': 'Армянских драмов',
		'Nominal': 100,
		'Value': 133.121
	},

	'AUD': {
		'Name': 'Австралийский доллар',
		'Nominal': 1,
		'Value': 45.5309
	},

	'INR': {
		'Name': 'Индийских рупий',
		'Nominal': 100,
		'Value': 92.9658
	},

	'MDL': {
		'Name': 'Молдавских леев',
		'Nominal': 10,
		'Value': 36.9305
	},
}
kyrs=[]
kyr=[]
k={}
aa=0
a=0
nom=0
val=0
for values in currency:

    kyrs.append(currency[values]['Value']/currency[values]['Nominal'])
    k[values]=(currency[values]['Value']/currency[values]['Nominal'])
    
aa=min(k.values())
a=[key for key in k if k[key]==aa]

print('Минимальный курс у валюты {0} и составляет {1}'.format(a,aa))


# In[175]:


currency = {
	'AMD': {
		'Name': 'Армянских драмов',
		'Nominal': 100,
		'Value': 133.121
	},

	'AUD': {
		'Name': 'Австралийский доллар',
		'Nominal': 1,
		'Value': 45.5309
	},

	'INR': {
		'Name': 'Индийских рупий',
		'Nominal': 100,
		'Value': 92.9658
	},

	'MDL': {
		'Name': 'Молдавских леев',
		'Nominal': 10,
		'Value': 36.9305
	},
}
kyr={}
nom=0
val=0
a=''
for values in currency:
    for x in currency[values]:

        if type(currency[values][x])==float:
            val=currency[values][x]
        elif type(currency[values][x])==int:
            nom=currency[values][x]
        else: continue
            
    kyr[values]=(val/nom)
    if min(kyr.values())==kyr[values]:a=str(values)
        
print('Минимальный курс у валюты {0} и составляет {1}'.format(a,min(kyr.values())))


# In[288]:


bodycount = {
	'Проклятие Черной жемчужины': {
		'человек': 17
	}, 

	'Сундук мертвеца': {
		'человек': 56,
		'раков-отшельников': 1
	},

	'На краю света': {
		'человек': 88
	},

	'На странных берегах': {
		'человек': 56,
		'русалок': 2,
		'ядовитых жаб': 3,
		'пиратов зомби': 2
	}
}
k=[]
for name in bodycount:#bodycount исходный словарь с элементами словарями
	print ('{0} - Это содержимое словаря (элементы словаря) "{1}" который в свою очередь является ключом словаря bodycount' .format(bodycount[name],name))#вывод значения элемента исходного словаря. bodycount - словарь, name - ключ, bodycount[name]-значение ключа)
	for num in bodycount[name]: #bodycount[name] - доступ к значению исх словаря, bodycount[name]-вложенный словарь
		k.append(bodycount[name][num])#bodycount[name][num]-значение элемента вложенного словаря, num-ключ
		print('{0} - Это значение ключа "{1}"' .format(bodycount[name][num],num))
print('\nОтвет на поставленную задачу: '+ str(sum(k)))


# In[ ]:





# Работа с файлом:

# In[219]:


import json
with open('data.json', 'rb') as infile:
    data = json.load(infile)
type(data)


# In[220]:


data.keys()


# In[221]:


data['events_data']


# In[222]:


data_list = data['events_data']


# In[229]:


print(data_list)


# In[224]:


categories = []
for item in data_list:
    category = item['category']
    categories.append(category)
print (categories)


# In[225]:


import collections
c = collections.Counter()
for category in categories:
    c[category] += 1
print (c)


# In[226]:


sum(c.values()) 


# Теперь давайте посмотрим, какие клиенты совершают события table. Для этого пройдемся по каждому словарю из списка data_list и добавим значение client_id в новый список table_clients, но только в тех случаях, где category = 'table':

# In[234]:


table_clients=[]
for i in data_list:
    for cl_iter in i:
        if i[cl_iter]=='table':
            table_clients.append(i['client_id'])
        
print(table_clients)


# In[236]:


c = collections.Counter()
for table_client in table_clients:
    c[table_client] += 1
print (c)


# In[237]:


print (len(c.keys()))


# 1. Подсчитайте количество клиентов (client_id), которые совершали какие-либо действия

# In[249]:


c = collections.Counter()
client=[]
for i in data_list:
    client.append(i['client_id'])
for id in client:
    c[id]+=1
print (len(c))


# 2. Сколько действий совершил клиент (client_id) под номером 60459?

# In[250]:


print(c[60459])


# 3. Сколько действий с категорией (category) = page совершил клиент под номером 62602?

# In[258]:


a=0
client=[]
for i in data_list:
    if i['category']=='page' and i['client_id']==62602:
        a+=1
print (a)


# 4. Сколько уникальных клиентов совершили действия с категорией (category) = report?

# In[260]:


c = collections.Counter()
client=[]
for i in data_list:
    if i['category']=='report':
        client.append(i['client_id'])
for id in client:
    c[id]+=1
print (len(c))


# 5. Перечислите в каждом из полей идентификаторы клиентов, которые совершили действия с категорией (category) = report (В порядке возрастания)

# In[261]:


print (c.keys())


# Шифровка: 
# 1. код был
# 2. код написала я

# In[274]:


proverb = 'Программисты - это устройства, преобразующие кофеин в код.'

new_proverb = list(proverb)
for i in range(len(new_proverb) - 1):
    if i % 2 == 0:
        t = new_proverb[i]
        tt = new_proverb[i + 1]
        new_proverb[i] = tt
        new_proverb[i + 1] = t
        
new_proverb=''.join(new_proverb)
print(new_proverb)


# In[285]:


import re
proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
new_proverb = re.split('\s',proverb)
a=""
str(a)
b=''
ind=0
slovonew=""
for slovo in new_proverb:
  
  ind=new_proverb.index(slovo)
  if len(slovo)%2==0 and b!=('\W'):
    for b in range(0,len(slovo),2):
      a=slovo[b+1]
      b=slovo[b]
      slovonew+=a+b
  else:
    for b in range(0,len(slovo),2):
      if len(slovo)-1==0 and b!=('\W'):
        slovonew+=slovo[b]
      elif b!=len(slovo)-1 and b!=('\W'):
        a=slovo[b+1]
        b=slovo[b]
        slovonew+=a+b
      else:
        slovonew+=slovo[b]
  new_proverb[ind]=slovonew
  slovonew=''
  
n=(' '.join(new_proverb))
new_proverb=n
print(n)


# In[287]:


import collections
c = collections.Counter()
for word in ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']:
    c[word] += 1

print(c)
print(c['counter'])
print(c['collections'])
c = collections.Counter(a=4, b=2, c=0, d=-2)
list(c.elements())


# In[286]:


arrivals = {
	'Париж': {'время': '15:25', 'статус': 'ожидается', 'рейс': ['Аэрофлот']},
	'Пекин': {'время': '15:35', 'статус': 'опаздывает', 'рейс': ['China Southern Airlines', 'Россия']},
	'Лиссабон': {'время': '15:40', 'статус': 'ожидается', 'рейс': ['Nordwind', 'Аэрофлот']},
}
print(len(arrivals['Пекин']['рейс']))
print(arrivals['Пекин']['рейс'][0] + arrivals['Пекин']['рейс'][1])


# In[278]:


inverted_word=''
basic_word = 'программирование'
for i in range(len(basic_word)-1,-1,-1):
  inverted_word+=basic_word[i]
if inverted_word==basic_word:
  print('Слово "{}" полиндром'.format(basic_word))
else:
  print('Слово "{}" - не полиндром'.format(basic_word))


# In[272]:


number = 56.257
s=0
pos=str(number)
pos=pos[pos.find('.')+1:]
for i in pos:
  s+=int(i)
print(s)


# In[271]:


emails_list = ['vasya@mail.ru', 
          'akakiy@yandex.ru', 
          'spyderman@yandex.ru', 
          'XFiles@gmail.com', 
          'hello@mail.ru', 
          'noname@gmail.com', 
          'DonaldTrump@mail.ru', 
          'a768#af@yandex.ru', 
          'Ivan_Ivanovich@yandex.ru', 
          'thebestmail@yandex.ru']
domain_d={}
domain_list=[i[(i.find('@')+1):] for i in emails_list]
from collections import Counter
domain_d=Counter(domain_list)
print(dict(domain_d))


# In[269]:


string = 'Интернет-открытки - это лучшее средство для мужчины сказать женщине о своих чувствах прямо в глаза.'
secret = string[24:30]
new_string = string.replace(secret.lower(), secret.upper()) 


# In[270]:


secret


# In[265]:


string = 'Тяжёлая интернет-зависимость - это когда ты выходишь из интернета, а он из тебя нет.'
import re 
string =(re.sub(r'[^\w ]',r':)',string))
print(string)


# In[264]:


name = 'Севастиан'
soglasnie=('б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ').split(', ')
glasnie=('а, у, о, ы, э, я, ю, ё, и, е').split(', ')
for i in range(len(name)):
  if name[i].lower() in glasnie:
    print("{} - гласная буква" .format(name[i]))
  elif name[i].lower() in soglasnie:
    print("{} - согласная буква" .format(name[i]))


# Регулярные выражения:

# In[262]:


text = '''Разработка языка Python была начата в конце 1980-х годов сотрудником голландского института CWI Гвидо ван Россумом. 
      Для распределённой ОС Amoeba требовался расширяемый скриптовый язык, и Гвидо начал писать Python на досуге, позаимствовав 
      некоторые наработки для языка ABC (Гвидо участвовал в разработке этого языка, ориентированного на обучение программированию). 
      В феврале 1991 года Гвидо опубликовал исходный текст в группе новостей alt.sources. Название языка произошло вовсе не от вида пресмыкающихся. 
      Автор назвал язык в честь популярного британского комедийного телешоу 1970-х "Летающий цирк Монти Пайтона".'''


# In[266]:


re.search('\\d+',text)
re.findall('\\d+',text)
re.search('[A-Za-z]+',text)
re.findall('[A-Za-z]+',text)
re.search('[А-Яа-я]+ка',text)
re.findall('[А-Яа-я]+ка',text)


# In[267]:


re.findall('[^\\W|\\s][А-Яа-яЁё]*[а|А][А-Яа-яЁё]{2}[И|и][А-Яа-яЁё]*[\\W|\\s$]',text)


# In[268]:


from collections import Counter
Pattern=re.compile('(?ui:[аеёиоуыэюя])\\s(?ui:[бвгджзйклмнпрстфхцчшщ])')#(?ui:...) Важно! Если вы работаете с юникодом, то вышеуказанный ключ не сработает. Нужно добавить UNICODE_CASE, т.е. ?ui.\n",
len(Pattern.findall(text))


# In[ ]:




