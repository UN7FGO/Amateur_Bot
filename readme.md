# Discord Bot - помошник начинающего радиолюбителя.

## Бот очень простой и не использует какую-либо базу данных для работы. Бот работает со специальным образом подготовленной файловой системой. 

Бот позволяет сокартить время начинающего радиолюбителя, при поиске информации, связанной с радиоэдектроникой.
Возможно сипользование программы по любюому профилю, просто разместив соответствующие файлы в рабочих каталогах.

**Доступные команды**

### Общие команды 

**/help** - выдает пользователю справку по командам (данный текст).
          
**/ver** - сообщает текущую версию программы бота.

**/ping** - проверка работоспособности бота. В случае нормальной работы возвращает пользователю сообщение "pong".
    
### Команды работы с файловыми базами информации. 

**/ds <наименование компонента>** - высылает PDF-файл с документацией, для запрошенного электронного компонента.

**/mc <наименование микроконтроллера>** - высылает подробную документацию, для запрошенного микроконтроллера.

**/pinout <наименование платы>** - высылает описание назначения выводов отладочной платы, для запрошенного модуля.

**/books <номер книги>** - высылает соответствующую книгу по электринке из имеющейся библиотеки.

**/arduino <номер книги>** - высылает соответствующую книгу по микроконтроллерам из имеющейся библиотеки.

**/prg <номер книги>** - высылает соответствующую книгу по программрованию из имеющейся библиотеки.

_В случае команды без параметра, будет показан список всех доступных материалов._
