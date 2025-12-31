# ------------------------------------------------------------
# act2_flow.rpy
# Акт 2 - переходы между ветками (расширенные, полноценные)
# Цель: сделать ощущение маршрута, последствий и "сшивки" города
# ------------------------------------------------------------

label act2_entry:
    scene bg cyberspace_city
    with dissolve

    play music "audio/music/act2_1.mp3" fadein 2.0 loop volume 0.008
    voice "audio/Hamayumi/act_2/1.mp3"
    hamayumi "Точка выбора - не меню."
    voice "audio/Hamayumi/act_2/2.mp3"
    hamayumi "Это маршрут."
    voice "audio/Hamayumi/act_2/3.mp3"
    hamayumi "Ты уже идёшь. Вопрос только - куда позволяет инерция."

    "Город дышит."
    "Вывески мерцают не рекламой - диагнозами."
    "Переулки складываются в направляющие, будто кто-то заранее нарисовал тебе траекторию."

    "На перекрёстке четыре тени."
    "Они не стоят отдельно - они встроены в архитектуру."
    voice "audio/Hamayumi/act_2/4.mp3"
    hamayumi "Quins первым."
    voice "audio/Hamayumi/act_2/5.mp3"
    hamayumi "Потому что обещание всегда идёт раньше цены."

    "Ты чувствуешь, как воздух становится плотнее - как перед входом в новую зону."
    "Карта исчезает."
    "Остаётся только шаг."

    jump branch_quins


# ------------------------------------------------------------
# После Quins -> к Nighstess
# ------------------------------------------------------------
label act2_after_quins:
    scene bg cyberspace_city
    with dissolve
    play music "audio/music/act2_1.mp3" fadein 2.0 loop volume 0.008
    show hamayumi at center
    "После Quins город кажется строже."
    "Как будто тебя измерили и отпустили."
    "Не осудили. Не приняли."
    "Просто присвоили значение и перестали спорить."
    voice "audio/Hamayumi/act_2/6.mp3"
    hamayumi "Ты заплатил не деньгами."
    voice "audio/Hamayumi/act_2/7.mp3"
    hamayumi "Ты заплатил тем, что теперь знаешь, чего хочешь."
    voice "audio/Hamayumi/act_2/8.mp3"
    hamayumi "Знание - тяжёлое. Оно тянет дальше."

    "На стекле витрины появляется отражение: не твоё лицо - твой выбор."
    "Отражение не двигается синхронно."
    "Оно показывает вариант, где ты не пошёл дальше."
    voice "audio/Hamayumi/act_2/9.mp3"
    hamayumi "Видишь?"
    voice "audio/Hamayumi/act_2/10.mp3"
    hamayumi "Город хранит несделанные шаги как мусор."
    voice "audio/Hamayumi/act_2/11.mp3"
    hamayumi "И потом кидает ими тебе под ноги."

    "Светофор мигает одним цветом - спокойным."
    "Спокойствие как приглашение."
    "И как ловушка."
    voice "audio/Hamayumi/act_2/12.mp3"
    hamayumi "Дальше Nighstess."
    voice "audio/Hamayumi/act_2/13.mp3"
    hamayumi "Он не обещает. Он упрощает."
    voice "audio/Hamayumi/act_2/14.mp3"
    hamayumi "А упрощение всегда звучит как спасение."

    "Переход не происходит сразу."
    "Сначала город 'гасит' лишние улицы."
    "Дороги складываются в одну прямую линию - к крыше."
    hide hamayumi
    jump branch_nighstess


# ------------------------------------------------------------
# После Nighstess -> к Sand
# ------------------------------------------------------------
label act2_after_nighstess:
    scene bg cyberspace_city
    with dissolve
    show hamayumi at center
    stop music fadeout 1.0
    play music "audio/music/act2_1.mp3" fadein 2.0 loop volume 0.008

    "Спокойствие ложится ровным слоем."
    "Слишком ровным."
    "Будто кто-то провёл валиком по твоим мыслям."
    voice "audio/Hamayumi/act_2/15.mp3"
    hamayumi "Так выглядит согласие."
    voice "audio/Hamayumi/act_2/16.mp3"
    hamayumi "Когда вопрос уже задан, но ответ за тебя подставили."

    "Ты пытаешься вспомнить, о чём спорил минуту назад."
    "Слова расплываются."
    "Остаётся только ощущение: 'не сопротивляйся'."
    voice "audio/Hamayumi/act_2/17.mp3"
    hamayumi "В этом и риск."
    voice "audio/Hamayumi/act_2/18.mp3"
    hamayumi "Согласие приятно тем, что не требует доказательств."

    "Пол под ногами становится рыхлым."
    "Пауза перестаёт быть комнатой."
    "Она превращается в поверхность, которая сыпется."
    voice "audio/Hamayumi/act_2/19.mp3"
    hamayumi "Теперь Sand."
    voice "audio/Hamayumi/act_2/20.mp3"
    hamayumi "Если Nighstess учит принять - Sand учит не требовать."
    voice "audio/Hamayumi/act_2/21.mp3"
    hamayumi "И это ещё тише."

    "Город не исчезает."
    "Он просто отодвигается, как будто ты выключил дальность прорисовки."
    "Остаётся край."

    jump branch_sand


# ------------------------------------------------------------
# После Sand -> к Hospital
# ------------------------------------------------------------
label act2_after_sand:
    scene bg cyberspace_edge
    with dissolve

    stop music fadeout 1.0
    play music "audio/music/act2_1.mp3" fadein 2.0 loop volume 0.008

    "Пауза тянется дольше, чем нужно."
    "Как будто ты стоишь AFK, а мир решает, выкидывать ли тебя с сервера."
    "Песок сыпется не вниз - в стороны."
    "Он заполняет пустоты между мыслями."
    show hamayumi at center
    voice "audio/Hamayumi/act_2/22.mp3"
    hamayumi "Тебя возвращают."
    voice "audio/Hamayumi/act_2/23.mp3"
    hamayumi "Потому что неопределённость - это тоже нагрузка."
    voice "audio/Hamayumi/act_2/24.mp3"
    hamayumi "А ядро не любит нагрузку без результата."

    "Где-то за спиной слышится щелчок."
    "Не звук двери."
    "Звук переключателя."
    voice "audio/Hamayumi/act_2/25.mp3"
    hamayumi "Смотри внимательно."
    voice "audio/Hamayumi/act_2/26.mp3"
    hamayumi "Следующий переход - не прогулка."
    voice "audio/Hamayumi/act_2/27.mp3"
    hamayumi "Это будет попытка перепрошить то, как ты называешь реальность."

    "Песок под ногами становится белым."
    "Свет перестаёт быть солнечным."
    "Он становится медицинским."

    "Край превращается в коридор."
    "Коридор - в палату."

    jump branch_hospital


# ------------------------------------------------------------
# Общий переход в Акт 3 (после Hospital)
# ------------------------------------------------------------
label act2_transition:
    scene bg cyberspace_edge
    with fade

    stop music fadeout 1.5
    play music "audio/music/act2_1.mp3" fadein 2.0 loop volume 0.008
    show hamayumi at center
    "Все линии сходятся."
    "Город снова целый."
    "Но теперь он выглядит иначе: как схема, которую собирали из твоих решений."

    "Где-то в высоте включается подсветка."
    "Окна загораются одновременно, будто система проверяет, на месте ли ты."
    voice "audio/Hamayumi/act_2/28.mp3"
    hamayumi "Акт закрывается."
    voice "audio/Hamayumi/act_2/29.mp3"
    hamayumi "Ты прошёл через формы."
    voice "audio/Hamayumi/act_2/30.mp3"
    hamayumi "Обещание. Принятие. Пауза. Перепрошивка."

    "Вдалеке появляется силуэт ядра."
    "Не башня и не храм."
    "Скорее - точка сборки."
    "Место, где любые слова превращают в параметры."
    voice "audio/Hamayumi/act_2/31.mp3"
    hamayumi "Дальше - ядро."
    voice "audio/Hamayumi/act_2/32.mp3"
    hamayumi "И там уже не будет 'кажется'."
    voice "audio/Hamayumi/act_2/33.mp3"
    hamayumi "Там будет только то, что ты закрепил."

    jump act3_entry
