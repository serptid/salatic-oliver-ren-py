# ------------------------------------------------------------
# branch_hospital.rpy
# Ветка Больницы (расширенная) - "перепрошивка интерпретации"
# Открывает концовку Hospital только при 3/3 правильных выборах
# Добавлено: трудности, сюжетный поворот, "двойная интерпретация"
# ------------------------------------------------------------

label branch_hospital:

    # локальный счётчик правильных выборов
    $ hospital_score = 0

    # локальный флаг поворота (не обязателен, но пригодится для актов дальше)
    $ hospital_twist_seen = False

    scene bg hospital
    with fade

    play music "audio/music/durka.mp3" fadein 2.0 loop volume 0.008

    oliver "Белый свет."
    oliver "Слишком реальный."

    voice "audio/Hamayumi/klinika/1.mp3"
    show hamayumi at left
    hamayumi "Это пробой."
    voice "audio/Hamayumi/klinika/2.mp3"
    hide hamayumi
    show hamayumi_up at left
    hamayumi "Если ты примешь его - киберспейс отступит."

    oliver "Если это всё симптом..."
    oliver "Тогда я могу остановить это."

    voice "audio/Hamayumi/klinika/3.mp3"
    hide hamayumi_up
    show hamayumi_T at left
    hamayumi "Ты уверен, что хочешь, чтобы тебя 'починили'?"
    voice "audio/Hamayumi/klinika/4.mp3"
    hide hamayumi_T
    show hamayumi_forw at left
    hamayumi "Иногда чинят не боль - а память о ней."

    # -------------------------
    # Экран 2 - Кабинет врача
    # -------------------------
    with dissolve

    show doctor at right
    with dissolve

    doctor "Салатик Оливер."
    doctor "Расскажите, что вы видите."
    doctor "Без художественных деталей. Только факты."

    voice "audio/Hamayumi/klinika/5.mp3"
    hide hamayumi_forw
    show hamayumi_break at left
    hamayumi "Слышишь?"
    voice "audio/Hamayumi/klinika/6.mp3"
    hide hamayumi_break
    show hamayumi_cry at left
    hamayumi "Факты - это форма контроля."
    voice "audio/Hamayumi/klinika/7.mp3"
    hide hamayumi_cry
    show hamayumi_you at left
    hamayumi "Но иногда она спасает."

    menu:
        "Ответ врачу"

        "Я видел taruma":
            doctor "Хорошо."
            doctor "Мы назовём это и перестанем подпитывать."
            voice "audio/Hamayumi/klinika/8.mp3"
            hide hamayumi_you
            show hamayumi at left
            hamayumi "Иногда название - это клетка."
            voice "audio/Hamayumi/klinika/9.mp3"
            hide hamayumi
            show hamayumi_up at left
            hamayumi "Если ты назвал - тебя можно отучать."

        "Я видел Quins.":
            doctor "Мы разберём это позже."
            doctor "Сначала закрепим реальность."
            voice "audio/Hamayumi/klinika/10.mp3"
            hide hamayumi_you
            show hamayumi at left
            hamayumi "Ты спрятал смысл в имени."
            voice "audio/Hamayumi/klinika/11.mp3"
            hide hamayumi
            show hamayumi_up at left
            hamayumi "Имя удобно: его можно объявить симптомом."

        "Я видел NightASS.":
            doctor "Это реакция на стресс."
            doctor "Мозг достраивает среду, чтобы выдержать нагрузку."
            voice "audio/Hamayumi/klinika/12.mp3"
            hide hamayumi_you
            show hamayumi_T at left
            hamayumi "И всё же город реагирует на тебя."
            voice "audio/Hamayumi/klinika/13.mp3"
            hide hamayumi_T
            show hamayumi_forw at left
            hamayumi "Симптомы не задают вопросов."

        "Я не уверен. Но это влияет на выбор.":
            $ hospital_score += 1
            doctor "Это честный ответ."
            doctor "Сомнение - не провал. Это наблюдение."
            voice "audio/Hamayumi/klinika/14.mp3"
            hide hamayumi_you
            show hamayumi_break at left
            hamayumi "Честность держит тебя целым."

    doctor "Мы попробуем простую штуку."
    doctor "Я дам вам 'якорь'."
    doctor "Если начнёт уносить - держитесь за него."

    doctor "Скажите: какая сегодня дата?"

    menu:
        "Якорь"

        "Я не помню. Но я могу проверить.":
            $ hospital_score += 1
            doctor "Правильно."
            doctor "Не фантазировать. Проверять."
            voice "audio/Hamayumi/klinika/15.mp3"
            hide hamayumi_break
            show hamayumi_T at left
            hamayumi "Проверка - это выбор, который не зависит от страха."

        "Любая. Здесь время не важно.":
            doctor "Для вас - важно."
            doctor "Это основа ориентации."
            voice "audio/Hamayumi/klinika/16.mp3"
            hide hamayumi_break
            show hamayumi_cry at left
            hamayumi "Он ставит рамку."
            voice "audio/Hamayumi/klinika/17.mp3"
            hide hamayumi_cry
            show hamayumi_you at left
            hamayumi "Рамки помогают. И ломают."

        "Сегодня... (назвать любую)":
            doctor "Хорошо."
            doctor "Но мы это зафиксируем по карте."
            voice "audio/Hamayumi/klinika/18.mp3"
            hide hamayumi_break
            show hamayumi_forw at left
            hamayumi "Удобно."
            voice "audio/Hamayumi/klinika/19.mp3"
            hide hamayumi_forw
            show hamayumi_break at left
            hamayumi "Когда за тебя фиксируют - ты перестаёшь держать сам."

    doctor "Ещё вопрос."
    doctor "Кто такой Хамаюми?"

    menu:
        "О Хамаюми"

        "Это мой внутренний голос, и он меня удерживает.":
            $ hospital_score += 1
            doctor "Понял."
            doctor "Мы не будем спорить с ним."
            doctor "Мы научимся проверять его."
            voice "audio/Hamayumi/klinika/20.mp3"
            hide hamayumi_break
            show hamayumi_cry at left
            hamayumi "Он не пытается меня убить."
            voice "audio/Hamayumi/klinika/21.mp3"
            hide hamayumi_cry
            show hamayumi_you at left
            hamayumi "Он пытается поставить мне правила."

        "Его нет.":
            doctor "Хорошо."
            doctor "Тогда вам будет проще."
            voice "audio/Hamayumi/klinika/22.mp3"
            hide hamayumi_break
            show hamayumi_cry at left
            hamayumi "Ложь ради простоты."
            voice "audio/Hamayumi/klinika/23.mp3"
            hide hamayumi_cry
            show hamayumi_you at left
            hamayumi "Так начинаются удобные исчезновения."

        "Это часть киберпространства.":
            doctor "Тогда тем более нужно якорение."
            voice "audio/Hamayumi/klinika/24.mp3"
            hide hamayumi_you
            show hamayumi_T at left
            hamayumi "И тем более тебе страшно признать, что я - часть тебя."

        "Он моя тульпа":
            doctor "Тогда тем более нужно якорение."
            doctor "Он тебя портит"

    hide doctor
    with dissolve

    # -------------------------
    # Экран 3 - Палата
    # -------------------------
    scene bg hospital
    with dissolve

    voice "audio/Hamayumi/klinika/25.mp3"
    hide hamayumi_T
    show hamayumi_break at left
    hamayumi "Ты стираешь меня словами."
    voice "audio/Hamayumi/klinika/26.mp3"
    hide hamayumi_break
    show hamayumi_cry at left
    hamayumi "Но пока не до конца."

    oliver "Тогда почему ты всё ещё здесь?"

    voice "audio/Hamayumi/klinika/27.mp3"
    hide hamayumi_cry
    show hamayumi at left
    hamayumi "Потому что ты не просто веришь."
    voice "audio/Hamayumi/klinika/28.mp3"
    hide hamayumi
    show hamayumi_up at left
    hamayumi "Ты привык."
    voice "audio/Hamayumi/klinika/29.mp3"
    hide hamayumi_up
    show hamayumi_T at left
    hamayumi "А привычка сильнее аргументов."

    "Тишина" "Пииии-"
    "Тишина" "Пииии-"

    oliver "Монитор..."
    oliver "Он звучит как таймер."

    voice "audio/Hamayumi/klinika/30.mp3"
    hide hamayumi_T
    show hamayumi_forw at left
    hamayumi "Это и есть таймер."
    voice "audio/Hamayumi/klinika/31.mp3"
    hide hamayumi_forw
    show hamayumi_break at left
    hamayumi "У тебя будет момент, когда станет легче."
    voice "audio/Hamayumi/klinika/32.mp3"
    hide hamayumi_break
    show hamayumi_cry at left
    hamayumi "И ты решишь, что победил."
    voice "audio/Hamayumi/klinika/33.mp3"
    hide hamayumi_cry
    show hamayumi_you at left
    hamayumi "Вот тогда ты проиграешь."

    menu:
        "Что делать?"

        "Позвать врача и попросить удалить кибспек":
            voice "audio/Hamayumi/klinika/34.mp3"
            hide hamayumi_you
            show hamayumi_break at left
            hamayumi "..."
            "Тишина становится слишком удобной."
            "В голове появляется мысль: 'пусть решат за меня'."

        "Остановиться и провести проверку Хамаюми":
            $ hospital_score += 1
            voice "audio/Hamayumi/klinika/35.mp3"
            hide hamayumi_you
            show hamayumi_forw at left
            hamayumi "Тогда ты ещё держишься."
            voice "audio/Hamayumi/klinika/36.mp3"
            hide hamayumi_forw
            show hamayumi_T at left
            hamayumi "Поверить - не значит подчиниться."
            voice "audio/Hamayumi/klinika/37.mp3"
            hide hamayumi_T
            show hamayumi_cry at left
            hamayumi "Значит признать: часть тебя защищается так, как умеет."

        "Стерпеть":
            voice "audio/Hamayumi/klinika/38.mp3"
            hide hamayumi_you
            show hamayumi_break at left
            hamayumi "Понял."
            "Молчание не выбирает сторону."
            "Но молчание - идеальная почва для чужих выводов."

    # -------------------------
    # Экран 4 - Поворот
    # -------------------------
    with fade

    "Голос по громкой связи" "Пациент Оливер. Подготовка к процедуре. Палата 12."

    oliver "Процедуре?"
    oliver "Мне никто не говорил..."

    voice "audio/Hamayumi/klinika/39.mp3"
    hide hamayumi_break
    show hamayumi_up at left
    hamayumi "Момент, где реальность становится сценой."

    show nurse at center
    with dissolve

    nurse "Пойдёмте."
    nurse "Это займёт немного времени."
    nurse "После этого станет проще."

    voice "audio/Hamayumi/klinika/40.mp3"
    hide hamayumi_up
    show hamayumi_forw at left
    hamayumi "Слушай формулировки."
    voice "audio/Hamayumi/klinika/41.mp3"
    hide hamayumi_forw
    show hamayumi_break at left
    hamayumi "'Проще' - это не 'лучше'."

    oliver "Что за процедура?"

    nurse "Коррекция интерпретации."
    nurse "Чтобы вы перестали придавать значение... лишним конструкциям."

    voice "audio/Hamayumi/klinika/42.mp3"
    hide hamayumi_break
    show hamayumi_cry at left
    hamayumi "Слышишь?"
    voice "audio/Hamayumi/klinika/43.mp3"
    hide hamayumi_cry
    show hamayumi_you at left
    hamayumi "Они не лечат киберспейс."
    voice "audio/Hamayumi/klinika/44.mp3"
    hide hamayumi_you
    show hamayumi_T at left
    hamayumi "Они лечат твою способность сопротивляться удобному объяснению."

    $ hospital_twist_seen = True

    menu:
        "Идти?"

        "Согласиться. Пусть делают.":
            nurse "Хорошо."
            nurse "Не беспокойтесь."
            voice "audio/Hamayumi/klinika/45.mp3"
            hide hamayumi_T
            show hamayumi_break at left
            hamayumi "Это выбор."
            voice "audio/Hamayumi/klinika/46.mp3"
            hide hamayumi_break
            show hamayumi_cry at left
            hamayumi "Просто не твой."

        "Попросить объяснить и записать согласие.":
            $ hospital_score += 1
            nurse "Мы можем объяснить."
            nurse "Но вы уверены, что хотите деталей?"
            voice "audio/Hamayumi/klinika/47.mp3"
            hide hamayumi_cry
            show hamayumi_forw at left
            hamayumi "Правильный ход."
            voice "audio/Hamayumi/klinika/48.mp3"
            hide hamayumi_forw
            show hamayumi_you at left
            hamayumi "Детали возвращают власть."

        "Отказаться и вернуться в палату.":
            nurse "Вы можете отказаться."
            nurse "Но тогда будет сложнее."
            voice "audio/Hamayumi/klinika/49.mp3"
            hide hamayumi_you
            show hamayumi_T at left
            hamayumi "Сложнее - значит: тебе придётся выдерживать себя самому."

    hide nurse
    with dissolve

    # -------------------------
    # Экран 5 - Процедурная
    # -------------------------
    scene bg hospital
    with dissolve
    show hamayumi at left

    oliver "Здесь холоднее."

    voice "audio/Hamayumi/klinika/50.mp3"
    hamayumi "И свет другой."
    voice "audio/Hamayumi/klinika/51.mp3"
    hide hamayumi
    show hamayumi_up at left
    hamayumi "Он похож на твой киберспейс."
    voice "audio/Hamayumi/klinika/52.mp3"
    hide hamayumi_up
    show hamayumi_T at left
    hamayumi "Только замаскирован под стерильность."

    "Система" "Нормализация контекста..."
    "Система" "Снижение значимости символических связей..."
    "Система" "Отключение вторичных нарративов..."

    oliver "Это... звучит как холодильник."
    oliver "пять ночей... но это похоже на ядро..."

    voice "audio/Hamayumi/klinika/53.mp3"
    hide hamayumi_T
    show hamayumi_forw at left
    hamayumi "Потому что это и есть ядро."
    voice "audio/Hamayumi/klinika/54.mp3"
    hide hamayumi_forw
    show hamayumi_break at left
    hamayumi "Только в белом халате."

    menu:
        "Последняя опора"

        "Держаться за якорь: проверять, что реально.":
            $ hospital_score += 1
            oliver "Дата. Место. Имя. ЯКОРЬ..."
            oliver "Я проверяю, а не угадываю."
            voice "audio/Hamayumi/klinika/55.mp3"
            hide hamayumi_break
            show hamayumi_you at left
            hamayumi "Вот это перепрошивка."
            voice "audio/Hamayumi/klinika/56.mp3"
            hide hamayumi_you
            show hamayumi_forw at left
            hamayumi "Не стирание. Настройка."

        "Сдаться и позволить выключить 'лишнее'.":
            "Тепло разливается по голове."
            "Мысли становятся мягкими."
            voice "audio/Hamayumi/klinika/57.mp3"
            hide hamayumi_break
            show hamayumi_cry at left
            hamayumi "Вот так и делают 'легко'."
            voice "audio/Hamayumi/klinika/58.mp3"
            hide hamayumi_cry
            show hamayumi_break at left
            hamayumi "Когда легко - ты перестаёшь держать форму."

        "Закричать, вырваться, сломать.":
            "Руки дрожат."
            "Свет режет."
            voice "audio/Hamayumi/klinika/59.mp3"
            hide hamayumi_break
            show hamayumi_T at left
            hamayumi "Сопротивление без направления."
            voice "audio/Hamayumi/klinika/60.mp3"
            hide hamayumi_T
            show hamayumi_forw at left
            hamayumi "Ты тратишь силы, не удерживая смысл."

    # -------------------------
    # Экран 6 - Итог ветки
    # -------------------------
    scene bg hospital_room
    with fade

    if hospital_score >= 3:
        $ hospital_done = True
        oliver "Если я перестану давать этому власть - оно ослабнет."
        oliver "Но я не обязан стирать часть себя, чтобы жить."
        voice "audio/Hamayumi/klinika/61.mp3"
        hide hamayumi_forw
        show hamayumi_you at left
        hamayumi "Тогда в ядре у тебя останется только реальность."
        voice "audio/Hamayumi/klinika/62.mp3"
        hide hamayumi_you
        show hamayumi_T at left
        hamayumi "Не та, что удобна системе."
        voice "audio/Hamayumi/klinika/63.mp3"
        hide hamayumi_T
        show hamayumi_forw at left
        hamayumi "Та, что проверена тобой."
    else:
        $ hospital_done = False
        voice "audio/Hamayumi/klinika/64.mp3"
        hide hamayumi_forw
        show hamayumi_break at left
        hamayumi "Ты сомневаешься."
        voice "audio/Hamayumi/klinika/65.mp3"
        hide hamayumi_break
        show hamayumi_cry at left
        hamayumi "Значит, связь ещё держится."
        voice "audio/Hamayumi/klinika/66.mp3"
        hide hamayumi_cry
        show hamayumi_you at left
        hamayumi "И они будут продолжать предлагать 'проще'."
        "Но ответа ты так и не оформил."

    call ambient_reset
    jump act2_transition
