import discord
import os

from dotenv import load_dotenv

# Глобальные переменные 
work_token = os.getenv("TOKEN")
version = 'Radio Bot ver. 0.05 2023.08.29'
work_dir = 'e:\projects\dis_bot\\' 
intents = discord.Intents.default()
intents.message_content = True
unknown_command = True


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        unknown_command = True
        return

# Информация о текущей версии программы
    if message.content.startswith('/ver'):
        unknown_command = False
        await message.channel.send(version)

# Проверка работоспособности бота
    if message.content.startswith('/ping'):
        unknown_command = False
        await message.channel.send('pong!')

# Справка по работе с программой
    if message.content.startswith('/help'):
        unknown_command = False
        await message.channel.send('''UN7FGO Discord-Bot.
    Общие команды.
          /help - выдает пользователю справку по командам (данный текст).
          /ver - сообщает текущую версию программы бота.
          /ping - проверка работоспособности бота. В случае нормальной работы возвращает пользователю сообщение "pong".
    Команды работы с файловыми базами информации. 
          /ds <наименование компонента> - высылает PDF-файл с документацией, для запрошенного электронного компонента.
          /mc <наименование микроконтроллера> - высылает подробную документацию, для запрошенного микроконтроллера.
          /pinout <наименование платы> - высылает описание назначения выводов отладочной платы, для запрошенного модуля.
          /books <номер книги> - высылает соответствующую книгу по электринке из имеющейся библиотеки.
          /arduino <номер книги> - высылает соответствующую книгу по микроконтроллерам из имеющейся библиотеки.
          /prg <номер книги> - высылает соответствующую книгу по программрованию из имеющейся библиотеки.
    В случае команды без параметра, будет показан список всех доступных материалов.''')


# ---------------------------------------------------------------------------------------------
# Работа с документациейй к электронным компонентам (datasheets)
    if message.content.startswith('/ds'):
        unknown_command = False
# Определяемся с рабочей директорией и вычисляем переданный с командой параметр        
        content = os.listdir(work_dir + 'datasheets')
        second = message.content[4:].upper()
        count = 0
        
# Если нет второго параметра то ничего не ищем        
        if second != '':
            await message.channel.send('Ищем данные по \"' + second + '\".')
            for k in content:
                if k[:-4]==second:
                    count += 1
             
# Если нашли файл, соответствующий второму параметру, то отправляем его пользователю
        if count != 0:
            await message.channel.send('Документация на \"' + second + '\" найдена.')
            files = work_dir + 'datasheets/' + second + '.pdf'
            await message.channel.send(file=discord.File(files))
            return

# Показываем пользователю список всех доступных файлов
        if count == 0:
            if second != '':
                await message.channel.send('Докуvентация на \"'+second+'\" не найдена.')
            await message.channel.send('В библиотеке есть документация на следующие компоненты:')
            result = ''
            count = 0
            for k in content:
                result += k[:-4]
                result += '  '
                count += 1
                if count>9: 
                    result += '\n'
                    count = 0
            await message.channel.send(result)

# ---------------------------------------------------------------------------------------------
# Работа с документациейй к микроконтроллерам (mc)
    if message.content.startswith('/mc'):
        unknown_command = False

# Определяемся с рабочей директорией и вычисляем переданный с командой параметр        
        content = os.listdir(work_dir + 'mc')
        second = message.content[4:].upper()
        count = 0
        
# Если нет второго параметра то ничего не ищем        
        if second != '':
            await message.channel.send('Ищем данные по \"' + second + '\".')
            for k in content:
                if k[:-4]==second:
                    count += 1
             
# Если нашли файл, соответствующий второму параметру, то отправляем его пользователю
        if count != 0:
            await message.channel.send('Документация на микроконтроллер \"' + second + '\" найдена.')
            files = work_dir + 'mc/' + second + '.pdf'
            await message.channel.send(file=discord.File(files))
            return

# Показываем пользователю список всех доступных файлов
        if count == 0:
            if second != '':
                await message.channel.send('Докуvентация на микроконтроллер \"'+second+'\" не найдена.')
            await message.channel.send('В библиотеке есть описание следующих микроконтроллеров:')
            result = ''
            for k in content:
                result += k[:-4] + '\n'
            await message.channel.send(result)
     
# ---------------------------------------------------------------------------------------------
# Работа с информацией по выводам отладочных плат (pinout)
    if message.content.startswith('/pinout'):
        unknown_command = False

# Определяемся с рабочей директорией и вычисляем переданный с командой параметр        
        content = os.listdir(work_dir + 'pinout')
        second = message.content[8:].upper()
        count = 0
        
# Если нет второго параметра то ничего не ищем        
        if second != '':
            await message.channel.send('Ищем данные по \"' + second + '\".')
            for k in content:
                if k[:-4].upper()==second:
                    count += 1
             
# Если нашли файл, соответствующий второму параметру, то отправляем его пользователю
        if count != 0:
            await message.channel.send('Описание на \"' + second + '\" найдено.')
            files = work_dir + 'pinout/' + second + '.jpg'
            await message.channel.send(file=discord.File(files))
            return

# Показываем пользователю список всех доступных файлов
        if count == 0:
            if second != '':
                await message.channel.send('Описание на \"'+second+'\" не найдено.')
            await message.channel.send('В библиотеке есть документация на следующие отладочные платы:')
            result = ''
            for k in content:
                result += k[:-4] + '\n'
            await message.channel.send(result)
            
# ---------------------------------------------------------------------------------------------
# Работа с литературой по электронике номеру книги (первые три символа в имени файла)
    if message.content.startswith('/books'):
        unknown_command = False

# Определяемся с рабочей директорией и вычисляем переданный с командой параметр
        content = os.listdir(work_dir + 'books')
        second = message.content[7:10].upper()
        count = 0
        book = ''
        
# Если нет второго параметра то ничего не ищем        
        if second != '':
            await message.channel.send('Ищем книгу с номером \"' + second + '\".')
            for k in content:
                if k[:3].upper()==second:
                    count += 1
                    book = k
             
# Если нашли файл, соответствующий второму параметру, то отправляем его пользователю
        if count != 0:
            await message.channel.send('Книга с номером \"' + second + '\" найдена.\n' + book)
            files = work_dir + 'books/' + book
            await message.channel.send(file=discord.File(files))
            return

# Показываем пользователю список всех доступных файлов
        if count == 0:
            if second != '':
                await message.channel.send('Книга с номером \"'+second+'\" не найдена.')
            await message.channel.send('В библиотеке есть следующие книги по радиоэлектронике:')
            result = ''
            for k in content:
                result += k + '\n'
            await message.channel.send(result)
            await message.channel.send('Чтобы получить книгу, отправьте команду /books <номер книги> (номер книги, три первые цифры имени файла):')
            # ---------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------
# Работа с литературой по микроконтроллерам
    if message.content.startswith('/arduino'):
        unknown_command = False

# Определяемся с рабочей директорией и вычисляем переданный с командой параметр
        content = os.listdir(work_dir + 'arduino')
        second = message.content[9:12].upper()
        count = 0
        book = ''
        
# Если нет второго параметра то ничего не ищем        
        if second != '':
            await message.channel.send('Ищем книгу с номером \"' + second + '\".')
            for k in content:
                if k[:3].upper()==second:
                    count += 1
                    book = k
             
# Если нашли файл, соответствующий второму параметру, то отправляем его пользователю
        if count != 0:
            await message.channel.send('Книга с номером \"' + second + '\" найдена.\n' + book)
            files = work_dir + 'arduino/' + book
            await message.channel.send(file=discord.File(files))
            return

# Показываем пользователю список всех доступных файлов
        if count == 0:
            if second != '':
                await message.channel.send('Книга с номером \"'+second+'\" не найдена.')
            await message.channel.send('В библиотеке есть следующие книги по микроконтроллерам:')
            result = ''
            for k in content:
                result += k + '\n'
            await message.channel.send(result)
            await message.channel.send('Чтобы получить книгу, отправьте команду /arduino <номер книги> (номер книги, три первые цифры имени файла):')
            # ---------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------
# Работа с литературой по программированию
    if message.content.startswith('/prg'):
        unknown_command = False

# Определяемся с рабочей директорией и вычисляем переданный с командой параметр
        content = os.listdir(work_dir + 'prg')
        second = message.content[5:8].upper()
        count = 0
        book = ''
        
# Если нет второго параметра то ничего не ищем        
        if second != '':
            await message.channel.send('Ищем книгу с номером \"' + second + '\".')
            for k in content:
                if k[:3].upper()==second:
                    count += 1
                    book = k
             
# Если нашли файл, соответствующий второму параметру, то отправляем его пользователю
        if count != 0:
            await message.channel.send('Книга с номером \"' + second + '\" найдена.\n' + book)
            files = work_dir + 'prg/' + book
            await message.channel.send(file=discord.File(files))
            return

# Показываем пользователю список всех доступных файлов
        if count == 0:
            if second != '':
                await message.channel.send('Книга с номером \"'+second+'\" не найдена.')
            await message.channel.send('В библиотеке есть следующие книги по программрованию:')
            result = ''
            for k in content:
                result += k + '\n'
            await message.channel.send(result)
            await message.channel.send('Чтобы получить книгу, отправьте команду /prg <номер книги> (номер книги, три первые цифры имени файла):')
            # ---------------------------------------------------------------------------------------------

# Если от пользователя пришла неизвестная команда
    if unknown_command:
        await message.channel.send('''Неизвестная команда.
    Вы можете использовать одну из ниже перечисленных команд для работы с Ботом:
    /help, /ver, /ping, /datasheet, /mc, /pinout, /books, /arduino, /prg .''')

client.run(work_token)
