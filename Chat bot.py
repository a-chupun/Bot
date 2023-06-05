import random
from datetime import datetime as dt
import math
from colorama import init
import time

init(autoreset=True)
blue = "\x1b[;36;3m"

class ChatEntry:
    def __init__(self, user, system):
       self.user = user
       self.user = system

class ChatBot:

    def __init__(self):
        self.responses = ["Хм... Ну гаразд.", "Ну якщо ви так просите.", "Цікавий вибір!",
                          "Вам вдалось мене здивувати!", "Неочікувано)"]
        self.topics = {
            "математика": self.maths,
            "фізика": self.physics,
            "філологія": self.philology,
            "географія": self.geography,
            "робота з текстом": self.work_with_text,
            "інше": self.other_tasks
        }
        self.output = ""
        self.entries = []
        
    def __add_user_entry(self, user):
        self.entries.append(ChatEntry('Користувач', user))
    def __add_system_entry(self, system):
        self.entries.append(ChatEntry('Помічник', system))

    def program(self):
        while True:
            system = "Ви можете задати мені питання з наступних тем: математика, фізика, філологія, географія, робота з текстом, інше."
            chat.program_output(system)
            topic = input("")
            self.__add_user_entry(topic)
            a.write(f'Користувач: {topic}\n')
            if topic.lower() in chat.topics.keys():
                system = random.choice(chat.responses)
                chat.program_output(system)
                system = f"Ви обрали тему '{topic.lower()}'. У цій темі є такі підтеми:"
                chat.program_output(system)
                chat.topics[topic.lower()]()
            elif topic.lower() == "вихід":
                system = f"Радий був поспілкуватись! Якщо виникнуть нові питання, звертайтесь)"
                chat.program_output(system)
                a.close()
                exit()
            elif topic.lower() == "допомога":
                chat.user_help()
                continue
            else:
                chat.error()

    def user_input(self):
        user = input("")
        chat.user = user
        self.__add_user_entry(user)
        a.write(f'Користувач: {user}\n')
        if chat.user.lower() == "назад":
            chat.program()
        elif chat.user.lower() == "вихід":
            system = f"Радий був поспілкуватись! Якщо виникнуть нові питання, звертайтесь)"
            chat.program_output(system)
            a.close()
            exit()
        elif chat.user.lower() == "допомога":
            chat.user_help()

    def program_output(self, system):
        print(f"{blue}" + system)
        self.__add_system_entry(system)
        a.write(f'Бот: {system}\n')

    def error(self):
        system = "Я не знаю цієї теми."
        chat.program_output(system)

    def user_help(self):
        system = "Для виходу, напишіть 'вихід'. Для повернення напишіть 'назад'."
        chat.program_output(system)
        chat.program()

    def maths(self):
        maths_topics = {"відстань між двома точками в просторі": chat.distance,
                        "площа трикутника за векторним добутком": chat.area_triangle,
                        "площа трикутника за основою та висотою": chat.s_triangle,
                        "виведення числа π": chat.pi
                        }
        chat.maths_topics = maths_topics
        system = '\n'.join(maths_topics)
        chat.program_output(system)
        chat.user_input()
        if chat.user in maths_topics.keys():
            system = f"Ви обрали тему '{chat.user}'"
            chat.program_output(system)
            chat.maths_topics[chat.user.lower()]()
        else:
            chat.error()

    def pi(self):
        system = str(math.pi)
        chat.program_output(system)

    def distance(self):
        distance = lambda x1, x2, y1, y2, z1, z2: math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
        system = "Введіть значення координат x1, y1, z1, x2, y2, z2 через пробіл: "
        chat.program_output(system)
        chat.user_input()
        coordinates = chat.user.split()
        try: x1, y1, z1, x2, y2, z2 = map(float, coordinates)
        except:
            system = f"Очевидно виникла якась помилка, спробуйте ще раз!"
            chat.program_output(system)
            chat.distance()
        system = f"Відстань між двома точками дорівнює {round(distance(x1, x2, y1, y2, z1, z2))}"
        chat.program_output(system)

    def area_triangle(self):
        area_triangle = lambda a, b: 1 / 2 * abs(a * b)
        system = f"Введіть довжини обох векторів через пробіл: "
        chat.program_output(system)
        chat.user_input()
        variables = chat.user.split()
        try: a, b = map(float, variables)
        except:
            system = "Очевидно виникла якась помилка, спробуйте ще раз!"
            chat.program_output(system)
            chat.area_triangle()
        system = f"Площа трикутника дорівнює {round(area_triangle(a, b))}"
        chat.program_output(system)

    def s_triangle(self):
        s_triangle = lambda b, h: 1 / 2 * b * h
        system = "Введіть довжину висоти та основи через пробіл: "
        chat.program_output(system)
        chat.user_input()
        variables = chat.user.split()
        try:
            h, b = map(float, variables)
        except:
            system = "Очевидно виникла якась помилка, спробуйте ще раз!"
            chat.program_output(system)
            chat.s_triangle()
        system = f"Площа трикутника дорівнює {round(s_triangle(b, h))}"
        chat.program_output(system)

    def physics(self):
        physics_topics = {"формула Ампера": chat.ampere_formula,
                          "виведення сталої Планка": chat.planka,
                          "закон Архімеда": chat.archimedes_principle,
                          "знаходження маси тіла": chat.weight}
        self.physics_topics = physics_topics
        system = '\n'.join(physics_topics)
        chat.program_output(system)
        chat.user_input()
        if chat.user in physics_topics.keys():
            system = f"Ви обрали тему '{chat.user}'"
            chat.program_output(system)
            chat.physics_topics[chat.user]()
        else:
            chat.error()

    def planka(self):
        h = 6.62607015e-34
        system = f"Значення сталої Планка (h):{h}"
        chat.program_output(system)

    def ampere_formula(self):
        magnetic_constant = 4 * math.pi * 10 ** (-7)
        ampere_formula = lambda i, r: (magnetic_constant * i) / 2 * math.pi * r
        system = "Введіть силу струму та відстань до провідника через пробіл: "
        chat.program_output(system)
        chat.user_input()
        variables = chat.user.split()
        try: i, r = map(float, variables)
        except:
            system = "Очевидно виникла якась помилка, спробуйте ще раз!"
            chat.program_output(system)
            chat.s_triangle()
        system = f"Індукція магнітного поля дорівнює {ampere_formula(i, r)}"
        chat.program_output(system)

    def archimedes_principle(self):
        archimedes_principle = lambda p, v: 9.8 * p * v
        system = "Введіть густину рідини та об'єм зануреного тіла через пробіл: "
        chat.program_output(system)
        chat.user_input()
        variables = chat.user.split()
        try: p, v = map(float, variables)
        except:
            system = "Очевидно виникла якась помилка, спробуйте ще раз!"
            chat.program_output(system)
            chat.s_triangle()
        system = f"Сила Архімеда дорівнює {archimedes_principle(p, v)}"
        chat.program_output(system)

    def weight(self):
        weight = lambda v, p: p * v
        system = "Введіть густину та об'єм тіла через пробіл: "
        chat.program_output(system)
        chat.user_input()
        variables = chat.user.split()
        try: p, v = map(float, variables)
        except:
            system = "Очевидно виникла якась помилка, спробуйте ще раз!"
            chat.program_output(system)
            chat.s_triangle()
        system = f"Маса тіла дорівнює {weight(p, v)}"
        chat.program_output(system)

    def geography(self):
        geography_topics = {"яке найбільше озеро в світі за площею?": chat.lake,
                            "які дві держави мають найбільшу кількість кордонів з іншими державами?": chat.states,
                            "яка площа України?": chat.square,
                            "який найбільший вулкан у світі?": chat.volcano}
        chat.geography_topics = geography_topics
        system = f"{blue}" + '\n'.join(geography_topics)
        chat.program_output(system)
        chat.user_input()
        if chat.user in geography_topics.keys():
            system = f"Ви обрали тему '{chat.user}'"
            chat.program_output(system)
            chat.geography_topics[chat.user]()
        else:
            chat.error()

    def lake(self):
        lake = """Найбільше озеро в світі за площею - це Каспійське море. 
Хоча його назва містить термін "море", Каспійське море фактично вважається найбільшим озером на планеті. 
Загальна площа Каспійського моря становить близько 371 000 квадратних кілометрів. 
Це солоновате озеро розташоване між Азією та Європою, і його природні кордони включають росію, Казахстан, Туркменістан, Іран та Азербайджан."""
        system = lake
        chat.program_output(system)

    def states(self):
        states = """Дві держави, які мають найбільшу кількість кордонів з іншими державами, 
це російська федерація та Китай.
російська федерація межує з 14 країнами: Азербайджаном, Білоруссю, Китаєм, Естонією, Фінляндією, Грузією, 
Казахстаном, Латвією, Литвою, Монголією, Норвегією, Польщею, Південною Кореєю, Україною та Фінляндією.
Китай межує з 14 країнами: Афганістаном, Бутаном, М'янмою, Казахстаном, Киргизстаном, Лаосом, 
Макао (Автономна область Китаю), Монголією, Непалом, Пакистаном, Російською Федерацією, Таджикистаном, В'єтнамом та Індією."""
        system = states
        chat.program_output(system)

    def square(self):
        square = "Загальна площа України становить 603 700 км²"
        system = square
        chat.program_output(system)

    def volcano(self):
        volcano = """Найбільший вулкан у світі - це Мауна Лоа на острові Гаваї в США. 
Мауна Лоа є одним з найактивніших вулканів у світі і має величезні розміри. 
Висота вулкана від його основи під водою до вершини становить близько 9 144 метрів. 
Якщо виміряти відстань від його основи на дні океану, Мауна Лоа визначається як найвищий гора у світі. 
Вулкан займає значну частину острова Гаваї та є величезним об'єктом геологічного і наукового дослідження."""
        system = volcano
        chat.program_output(system)

    def philology(self):
        philology_topics = {"які часи є в англійській мові?": chat.tenses,
                            "як утворити Passive Voice в Present Simple?": chat.passive,
                            "як утворюються дієслова в давальному відмінку?": chat.verbs}
        chat.philology_topics = philology_topics
        system = '\n'.join(philology_topics)
        chat.program_output(system)
        chat.user_input()
        if chat.user in philology_topics.keys():
            system = f"Ви обрали тему '{chat.user}'"
            chat.program_output(system)
            chat.philology_topics[chat.user]()
        else:
            chat.error()

    def tenses(self):
        tenses = """В англійській мові є наступні часи:
Present Simple (теперішній простий час)
Present Continuous (теперішній тривалий час)
Present Perfect (теперішній доконаний час)
Present Perfect Continuous (теперішній доконаний тривалий час)
Past Simple (минулий простий час)
Past Continuous (минулий тривалий час)
Past Perfect (минулий доконаний час)
Past Perfect Continuous (минулий доконаний тривалий час)
Future Simple (майбутній простий час)
Future Continuous (майбутній тривалий час)
Future Perfect (майбутній доконаний час)
Future Perfect Continuous (майбутній доконаний тривалий час)"""
        system = tenses
        chat.program_output(system)

    def passive(self):
        passive = """Утворення Passive Voice в Present Simple виконується за допомогою допоміжного дієслова "to be" в Present Simple (am/is/are) + дієслово у формі Past Participle.
Утворення Passive Voice в Present Simple має наступну структуру:
[Subject] + am/is/are + [Past Participle (3rd form of the verb)]
У Passive Voice суб'єкт дії стає об'єктом речення, а хто виконує дію може бути вказано за допомогою фрази "by + агент дії" (необов'язково)."""
        system = passive
        chat.program_output(system)

    def verbs(self):
        verbs = """У давальному відмінку відбуваються зміни у формі дієслів, залежно від роду та числа іменника, до якого вони відносяться.
Основні правила утворення дієслів у давальному відмінку української мови:
Якщо іменник є чоловічого роду, однини, дієслово в давальному відмінку має закінчення "-ові" або "-еві". 
Наприклад: дати комусь (дати батькові), допомогти хтось (допомогти другові).
Якщо іменник є жіночого роду, однини, дієслово в давальному відмінку має закінчення "-і" або "-ї". 
Наприклад: дати комусь (дати матері), розказати комусь (розказати подрузі).
Якщо іменник є середнього роду, однини, дієслово в давальному відмінку має закінчення "-у" або "-ю". 
Наприклад: показати чому-небудь (показати вікну), вчити когось (вчити студента).
У множині незалежно від роду іменників, дієслово в давальному відмінку має закінчення "-ам" або "-ям". 
Наприклад: допомагати комусь (допомагати друзям), говорити про щось (говорити про фактах)."""
        system = verbs
        chat.program_output(system)

    def work_with_text(self):
        text_topics = {
            "знайти складені з латинських літер слова, які у тексті зустрічаються більше 10 разів": chat.find_words_10,
            "знайти всі слова, які складаються з цифр": chat.digit_words,
            "вивести текст без зайвих пробілів": chat.spaces,
            "знайти найдовше речення в тексті": chat.longest_sentence,
            "знайти найбільш часто вживану літеру в тексті": chat.most_common_letter}
        chat.text_topics = text_topics
        system = '\n'.join(text_topics.keys())
        chat.program_output(system)
        chat.user_input()
        topic = chat.user
        if topic in text_topics.keys():
            system = f"Ви обрали тему '{topic}'"
            chat.program_output(system)
            chat.file()
            chat.text_topics[topic.lower()](chat.text)
        else:
            chat.error()


    def file(self):
        system = "Введіть шлях до файлу з текстом: "
        chat.program_output(system)
        chat.user_input()
        input_file = chat.user
        chat.read_file(input_file)
        system = f"Введіть шлях до файлу, куди потрібно записати відповідь: "
        chat.program_output(system)
        chat.user_input()
        output_file = chat.user
        output = chat.output
        chat.write_output(output_file, output)
        system = f"Відповідь записано в файл '{output_file}'"
        chat.program_output(system)

    def read_file(self, input_file):
        try:
            file = open(input_file, 'r')
            text = file.read()
            chat.text = text
        except:
            system = "Очевидно виникла якась помилка, спробуйте ще раз!"
            chat.program_output(system)
            chat.file()

    def write_output(self, output_file, output):
        try:
            file = open(output_file, 'w')
            file.write(output)
        except:
            system = "Очевидно виникла якась помилка, спробуйте ще раз!"
            chat.program_output(system)
            chat.file()

    def find_words_10(self, text):
        word_count = {}
        words = text.split()
        for word in words:
            word = word.strip('.,!?:;"')
            if word.isalpha() and word.islower():
                word_count[word] = word_count.get(word, 0) + 1
        result = [word for word, count in word_count.items() if count > 10]
        if not result:
            result = "немає таких слів."
        chat.output = f"Слова складені з латинських літер, що зустрічаються більше 10 разів:{result}"

    def digit_words(self, text):
        words = text.split()
        result = [word for word in words if word.isdigit()]
        if result == []:
            result = "немає таких слів."
        chat.output = f"Слова, які складаються з цифр: {result}"

    def spaces(self, text):
        chat.output = ' '.join(text.split())
        return chat.output

    def longest_sentence(self, text):
        sentences = text.split('. ')
        chat.output = max(sentences, key=len)
        return chat.output

    def most_common_letter(self, text):
        letter_count = {}
        for letter in text:
            if letter.isalpha():
                letter = letter.lower()
                letter_count[letter] = letter_count.get(letter, 0) + 1
        most_common_letter = max(letter_count, key=letter_count.get)
        chat.output = f"Найбільш часто вживана літера в тексті: {most_common_letter}"
        return chat.output

    def other_tasks(self):
        other_tasks = {"який зараз рік?": chat.current_year,
                       "підкидання кубика": chat.dice_roll,
                       "улюблена пісня": chat.favourite_song,
                       "гра 'історія'": chat.story_game}
        chat.other_tasks = other_tasks
        system = '\n'.join(other_tasks)
        chat.program_output(system)
        chat.user_input()
        if chat.user in other_tasks:
            system = f"Ви обрали тему '{chat.user}'"
            chat.program_output(system)
            chat.other_tasks[chat.user.lower()]()
        else:
            chat.error()

    def current_year(self):
        current_date = dt.now()
        current_year = current_date.year
        system = f"Поточний рік: {current_year}"
        chat.program_output(system)

    def dice_roll(self):
        system = f"Випало число: {random.randint(1, 6)}"
        chat.program_output(system)

    def favourite_song(self):
        song1 = """Her name is she, queen of the kings
Running so fast, beating the wind
Nothing in this world could stop the spread of her wings 
She, queen of the kings
Broken hеr cage, threw out the keys
She will be the warrior of north and southern seas"""
        song2 = """Don’t care what you say
Don’t care how you feel
Get out of my way
‘Cause I got a heart of steel"""
        song3 = """Instead I wrote a song
‘Bout how you did me wrong
I could’ve cried at home
And spent the night alone
Instead I wrote a song
I feel much better now
Mе and my girls are out
And we all sing along
Instead I wrotе a song"""
        song4 = """No I don’t care about them all
‘Cause all I want is to be loved
And all I care about is you
You’re stuck on me like a tattoo
No I don’t care about the pain
I’ll walk through fire and through rain
Just to get closer to you
You’re stuck on me like a tattoo"""
        song5 = """And when the world got me going crazy
I carry on
‘Cause I know I’m strong
When the world got me going crazy
I carry on
And it’s all because of"""
        songs = [song1, song2, song3, song4, song5]
        system = f"Приспів моєї улюбленої пісні: \
{random.choice(songs)}"
        chat.program_output(system)

    def story_game(self):
        system = "Дайте відповідь на наступні питання, щоб вийшла повноцінна історія."
        chat.program_output(system)
        templates = [
            "Жив-був {хто} {де} {коли} і робив це {навіщо}. І отже, {що}.",
            "{хто} з'явився {де} {коли} та зробив це {навіщо}. А потім {що}.",
            "Був {хто} {де} {коли}, мав ціль {навіщо} та виконав {що}.",
            "{хто} проживав у {де} {коли} з метою {навіщо} і досяг {що}.",
            "{де} {коли} {хто} робив це {навіщо} та досяг {що}."]
        questions = {
            "хто": "Хто?",
            "де": "Де?",
            "коли": "Коли?",
            "навіщо": "Навіщо?",
            "що": "Що?"
        }
        answers = {}
        for key, question in questions.items():
            system = question
            chat.program_output(system)
            chat.user_input()
            answer = chat.user
            answers[key] = answer
        for template in templates:
            system = template.format(**answers)
            chat.program_output(system)
            system = f"--------------------"
            chat.program_output(system)


dialog_file = f'dialog-{time.strftime("%Y%m%d-%H%M%S")}.txt'
a = open(dialog_file, "w", encoding = 'utf-8')
chat = ChatBot()
system = f"Вітаю, мене звати Помічник. "\
           "Для повернення до попередньої теми введіть 'назад', для виходу - 'вихід', а для допомоги  - 'допомога'"
chat.program_output(system)
chat.program()
