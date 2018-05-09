import Lab1.parser.request as request


def read_links_test():
    requested_content = request.read_links(['https://raw.githubusercontent.com/kirick1/cse/master/Lab1/test/test.txt'])
    expected_content = 'Heroku — хмарна PaaS-платформа, що підтримує ряд мов програмування. Компанією Heroku володіє Salesforce.com. Heroku, одна з перших хмарних платформ, зявилась в червні 2007 року і спочатку підтримувала тільки мову програмування Ruby, але на даний момент список підтримуваних мов також включає в себе Java, Node.js, Scala, Clojure, Python і PHP. На серверах Heroku використовуються операційні системи Debian або Ubuntu (яка також заснована на Debian). Джеймс Лінденбаум, Адам Віггінс і Оріон Генрі заснували Heroku в 2007 році в підтримку проектів, заснованих на Rack. 8 грудня 2010 року компанія Salesforce.com купила Heroku, зробивши її своєю дочірньою компанією. 12 липня 2011 року Мацумото Юкіхіро творець мови програмування Ruby, прийшов в компанію на посаду провідного інженера. У цьому ж місяці Heroku впровадила підтримку Node.js і Clojure. 15 вересня 2011 року Heroku і Facebook представили нову опцію «Heroku для Facebook». Heroku також надає підтримку таких систем управління базами даних, як CouchDB, Membase, MongoDB і Redis, крім основної — PostgreSQL. Програми, що працюють на Heroku, використовують також DNS-сервер Heroku (зазвичай додатки мають доменне імя виду «імя_додатку.herokuapp.com»). Для кожної програми виділяється кілька незалежних віртуальних процесів, які називаються «dynos». Вони розподілені по спеціальній віртуальній сітці («dynos grid»), яка складається з декількох серверів. Heroku також має систему контролю версій Git. Через сильний червневий шторм 2012 року в Північній Америці безліч додатків, що працюють на Heroku, відключилися, проте доступ був відновлений менш, ніж через 24 години.'
    assert requested_content == expected_content, 'Requests content from test link is not equal with expected'
    return '\tfile_reader.request.read_links test'
