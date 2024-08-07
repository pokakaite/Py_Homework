from django.shortcuts import render


# Create your views here.

def writers(request):
    return render(request, 'writers/writers.html')


def hemingway(request):
    cont = {
        'Hemingway': 'Американский писатель, журналист, лауреат Пулитцеровской и Нобелевской премий по литературе. Еще в детстве маленький Эрнест с подачи отца и деда стал увлекаться рыбалкой и охотой. Второй страстью юного Эрнеста стала литература. Еще в школе он решил, что будет писателем. Вместо поступления в ВУЗ вопреки воле родителей устроился на должность репортера в газете Канзас‑Сити, где вел колонку о происшествиях. Под руководством редакторов Хемингуэй учился писать лаконично и емко — так складывался его литературный стиль. В годы Первой мировой войны отчаянно пытался попасть на фронт, но получал отказы по состоянию здоровья. После нескольких неудачных попыток наконец отправился на Итальянский фронт. Вернулся в США героем после ранения, но с собой привез боль и разочарование. В 1921 году после свадьбы Хемингуэй отправился в Париж, где для него началась новая жизнь. Он вошел в кружок писателей и художников, которые посещали книжный магазин «Шекспир и его друзья». Особое влияние на Эрнеста оказала Гертруда Стайн, которая настаивала, чтобы Хемингуэй бросил работу на газету и посвятил себя исключительно писательству. Первый крупный литературный успех пришел к Хемингуэю с публикацией романа «И восходит солнце», но более значимым в его творчестве стал роман «Прощай, оружие!». После окончания Второй мировой войны автор отправился на Кубу, где написал повесть «Старик и море». За нее он получил Пулитцеровскую премию в 1953 году и она же повлияла на вручение Хемингуэю Нобелевской премии по литературе в 1954 году. В конце жизни Хемингуэй тяжело болел и погрузился в депрессию. К сожалению, врачи не смогли ему помочь, и 2 июля 1961 года Эрнест Хемингуэй застрелился в собственном доме'
    }
    return render(request, 'writers/writers.html', cont)


def shakespeare(request):
    cont = {
        'shakespeare': 'Уи́льям Шекспи́р'
    }
    return render(request, 'writers/writers.html', cont)
