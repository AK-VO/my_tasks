#Шифр Цезаря
t = input()
txt = ''
tt = ''
tt = t.split()

for j in tt:
    k = 0
    for b in j:
        if b.isupper() or b.islower():
            k+=1
    for i in j:
        if 65<=ord(i)<=90:
            if ord(i)+k>90:
                 txt+=chr(ord(i)+k-26)
            elif ord(i)+k < 65:
                 txt+=chr(ord(i)+k+26)
            else:
                 txt+=chr(ord(i)+k)
        elif 97<=ord(i)<=122:
            if ord(i)+k>122:
                 txt+=chr(ord(i)+k-26)
            elif ord(i)+k<97:
                 txt+=chr(ord(i)+k+26)
            else:
                 txt+=chr(ord(i)+k)
        elif ord("А")<=ord(i)<=ord("Я"):
            if ord(i)+k>ord("Я"):
                 txt+=chr(ord(i)+k-32)
            elif ord(i)+k<ord("А"):
                 txt+=chr(ord(i)+k+32)
            else:
                 txt+=chr(ord(i)+k)
        elif ord("а")<=ord(i)<=ord("я"):
            if ord(i)+k>ord("я"):
                 txt+=chr(ord(i)+k-32)
            elif ord(i)+k<ord("а"):
                 txt+=chr(ord(i)+k+32)
            else:
                 txt+=chr(ord(i)+k)
        else:
            txt+=i
    txt+=' '

print(txt)



#Генератор безопасных паролей
from random import *

quantity_pass = int (input ('Введите сколько паролей сгенерировать:'))

def creation_sym ():
  list_sym = [chr (i) for i in range (33, 127)]
  return list_sym

def generation_pass (quantity_pass, list_sym):  
  len_pas = int (input ('Введите длину пароля:'))
  list_val = []
  for i in range (quantity_pass):
    password = ''
    for _ in range (1, len_pas + 1):
      password += choice(list_sym)
    list_val += password.split ()
  return list_val

print ('Ваши пароли:', * generation_pass (quantity_pass, creation_sym()), sep='\n')



#Магический шар
from random import *

print ('Приветствую тебя таинственный незнакомец!')
name = input ('Представься, как тебя зовут:')

while True:
  var = input (f'{name}, хочешь я отвечу на любой твой вопрос? Ответь "Да" или "Нет:"')
  
  def play_1 ():
    vop = input ('Напиши свой вопрос:')
    grp = ['Положительные', 'Нерешительно положительные', 'Нейтральные', 'Отрицательные']
    grp_r = choice (grp)
    if grp_r == grp [0]:
      return (choice (['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом']))
    elif grp_r == grp [1]:  
      return (choice (['Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да']))
    elif grp_r == grp [2]:
      return (choice (['Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять']))
    else:
      return (choice (['Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно' ]))
      
  
  if var.lower () == 'да':
    print (play_1 ())
    var_2 = input ('Есть еще вопросы?')
    if var_2.lower () == 'да':
      print (play_1 ())
    else:
      break
  
  
  elif var.lower () == 'нет':
    print ('Всего наилучшего!')
    break
  else:
    print ('Ошибка! Введи "Да" или "Нет!')
    continue



#Угадайка чисел
from random import *

while True: 
  name = input ('Привет, как тебя зовут:')
  if name.isalpha():
    print ('Супер', name + '!')
    while True:
      num0 = input ('Хочешь сыграть в игру "Числовая угадайка?" Введи "Да" если хочешь.')
      
      if num0.lower() == 'да':
          print ('Тебе нужно угадать число от 1 до заданого тобой числа на следующей строке, удачи!')
            
          def play_1 ():
              ran = randint (1, int (input ('Введи число:')))
              print (ran)
              x = 0
              while True:
                  num = int (input ())
                  if 0 < num < ran:
                      print ('Число ниже случайного')
                      x += 1
                      continue
                  elif 101 > num > ran:
                      print ('Число выше случайного')
                      x += 1
                      continue
                  elif num == ran:
                      x += 1        
                      print ('Угадал', 'Количество попыток:', x)  
                      break
                  else:
                    print ('Введи число от 1 до 100!')
                    continue
                  
          play_1 ()    
          num2 = input ('Сыграем еще раз? Введите "Да" если хотите.')
      
          if num2.lower () == 'да':
            play_1 ()
          elif num2.lower () == 'нет':
            print ('Пока!')
            break
          else:
            print ('Введи корректный ответ')
            num2 = input ('Сыграем еще раз? Введите "Да" если хотите.')
      elif num0.lower () == 'нет': 
        print ('Пока!')
        break
      else:
        print ('Введи "Да" или "Нет"!')
        continue  
  else:
    print ('Ошибка, введи только буквы!')
    continue
