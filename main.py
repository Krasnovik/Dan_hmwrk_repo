goods = {'Лампа': '12345','Стол': '23456','Диван': '34567','Стул': '45678',}
store = {'12345': [{'quantity': 27, 'price': 42}],
'23456': [{'quantity': 22, 'price': 510},{'quantity': 32, 'price': 520}],
'34567': [{'quantity': 2, 'price': 1200},{'quantity': 1, 'price': 1150}],
'45678': [{'quantity': 50, 'price': 100},{'quantity': 12, 'price': 95},{'quantity': 43, 'price': 97}]}
#x=store.get('23456')
x=input()
o=goods.get(x)
predmet=store.get(o)
sum1=0
sum2=0
for i in range(0,len(predmet)):
    sum1+=predmet[i].get('quantity')
    sum2+=predmet[i].get('quantity') * predmet[i].get('price')
print(x + ' - ' + str(sum1) + ' штук, стоимость ' + str(sum2) + ' рубль' )








