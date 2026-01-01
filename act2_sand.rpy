# ------------------------------------------------------------
# branch_sand_minecraft.rpy
# Ветка Песка (расширенная) - "архив состояний"
# Minecraft-метафора: любовь к бесконечному копанию песка
# Поворот: в конце выясняется, что Sand - это Tarum
# Открывает концовку Sand только при 3/3 правильных выборах
# Убраны ТОЛЬКО реплики sand в ветках без начисления балла
# ВСЕ реплики hamayumi сохранены
# ------------------------------------------------------------

label branch_sand:

    $ sand_score = 0

    # -------------------------
    # Экран 1 - край (биом/граница)
    # -------------------------
    scene bg cyberspace_edge
    with fade

    play music "audio/music/sand.mp3" fadein 2.0 loop volume 0.008
    show hamayumi at left

    voice "audio/Hamayumi/sand/1.mp3"
    hamayumi "Край."
    voice "audio/Hamayumi/sand/2.mp3"
    hide hamayumi
    show hamayumi_up at left
    hamayumi "Тут система перестаёт объяснять."
    voice "audio/Hamayumi/sand/3.mp3"
    hide hamayumi_up
    show hamayumi_T at left
    hamayumi "Как будто ты дошёл до границы биома - дальше только песок."

    oliver "О я обожаю песочек"

    show sand at center
    with dissolve

    sand "Добро пожаловать туда, где никто не спорит о смысле."
    sand "Как в мире, где можно копать блоки бесконечно - и мир не спросит: зачем."
    oliver "Капец это совсем не майнкрафт.."
    oliver "Это почти как рай!"
    oliver "Мой любимый сервер СП"
    oliver "Я выкопаю весь песок!!!"

    voice "audio/Hamayumi/sand/4.mp3"
    hide hamayumi_T
    show hamayumi_forw at left
    hamayumi "Он говорит так, будто бесконечное копание - это религия."
    voice "audio/Hamayumi/sand/5.mp3"
    hide hamayumi_forw
    show hamayumi_you at left
    hamayumi "И будто в этой религии нет греха."

    menu:
        "Песок - ощущение"

        "Это похоже на пустоту.":
            # (реплики sand убраны - балл не начисляется)
            voice "audio/Hamayumi/sand/6.mp3"
            hide hamayumi_you
            show hamayumi_cry at left
            hamayumi "И отсутствие направления."
            voice "audio/Hamayumi/sand/7.mp3"
            hide hamayumi_cry
            show hamayumi_you at left
            hamayumi "Когда ты копаешь песок, ты не приближаешься ни к чему - и в этом кайф."

        "Это пустота.":
            # (реплики sand убраны - балл не начисляется)
            voice "audio/Hamayumi/sand/8.mp3"
            hide hamayumi_you
            show hamayumi_cry at left
            hamayumi "Честность без будущего."
            voice "audio/Hamayumi/sand/9.mp3"
            hide hamayumi_cry
            show hamayumi_you at left
            hamayumi "Как инвентарь, в котором нет плана - только стаки песка."

        "Это архив.":
            $ sand_score += 1
            sand "Да."
            sand "Архив состояний."
            sand "Как сундуки, куда ты складываешь ресурсы, потому что однажды пригодятся."
            sand "Но 'однажды' не наступает."
            sand "И тогда ты складываешь дальше - уже не ради пользы."
            sand "Ради ощущения, что ты всё ещё контролируешь хоть что-то."
            voice "audio/Hamayumi/sand/10.mp3"
            hide hamayumi_you
            show hamayumi at left
            hamayumi "Здесь лежат решения, которые так и не стали выбором."

    # -------------------------
    # Экран 2 - пустыня (процесс вместо цели)
    # -------------------------
    scene bg cyberspace_tunnel
    with dissolve
    show sand at right
    show hamayumi at left
    sand "Здесь не зовут остаться."
    sand "И не тянут выйти."
    sand "Как сервер без правил: хочешь - копай песок всю ночь."
    sand "Никто не напишет в чат: 'эй, сделай что-то полезное'."
    oliver "Мне только всякие дебики в сикрет пишут"
    oliver "Не понимают что я канал создала чтобы туда просто текст писать"

    "Голос" "Я почти выбрал."
    "Голос" "Я отложил навсегда."
    "Голос" "Я сказал себе: 'ещё один стак песка - и потом решу'."

    voice "audio/Hamayumi/sand/11.mp3"
    hamayumi "Слышишь эти голоса?"
    voice "audio/Hamayumi/sand/12.mp3"
    hide hamayumi
    show hamayumi_up at left
    hamayumi "Это игроки, которые пытались заменить выбор процессом."
    voice "audio/Hamayumi/sand/13.mp3"
    hide hamayumi_up
    show hamayumi_T at left
    hamayumi "И процесс победил."
    oliver "Я не шарю в ваших питонах, я щяс этот exe шник в браузере решу"
    menu:
        "Что делать"

        "Я щяс скравчу шалкер лопат и выкапаю до бедрока":
            $ sand_score += 1
            sand "Да."
            sand "Честно - не значит спасительно."
            sand "Можно честно признать: мне нравится просто копать."
            sand "И всё равно исчезнуть в этом."
            sand "Песок не делает шагов за тебя."
            sand "Он просто делает шаги ненужными."
            voice "audio/Hamayumi/sand/14.mp3"
            hide hamayumi_T
            show hamayumi_forw at left
            hamayumi "Песок не держит цепями."
            voice "audio/Hamayumi/sand/15.mp3"
            hide hamayumi_forw
            show hamayumi_you at left
            hamayumi "Он держит привычкой: ещё один блок - и станет легче."

        "Угражать админам":
            # (реплики sand убраны - балл не начисляется)
            voice "audio/Hamayumi/sand/16.mp3"
            hide hamayumi_T
            show hamayumi_forw at left
            hamayumi "Значит, пауза не победила."
            voice "audio/Hamayumi/sand/17.mp3"
            hide hamayumi_forw
            show hamayumi_you at left
            hamayumi "Значит, тебе всё ещё нужен смысл - хоть какой-то."

        "Включить читы":
            # (реплики sand убраны - балл не начисляется)
            voice "audio/Hamayumi/sand/18.mp3"
            hide hamayumi_T
            show hamayumi_forw at left
            hamayumi "И именно поэтому его легко перепутать с безопасностью."

    # -------------------------
    # Экран 3 - следы (не люди, а состояния)
    # -------------------------
    with dissolve

    sand "Те следы - не люди."
    sand "Это состояния."
    sand "Как дорожки в пустыне, которые ты сам натоптал, пока носил песок в сундуки."
    sand "Они не ведут к дому."
    sand "Они ведут к повторению."
    oliver "бож песок реально годноту мне втирает"
    oliver "Зачем мне весь этот песок?"

    voice "audio/Hamayumi/sand/19.mp3"

    hide hamayumi_you
    hide hamayumi_forw
    show hamayumi_cry at left
    hamayumi "В Minecraft есть момент, когда ты копаешь не ради стекла."
    voice "audio/Hamayumi/sand/20.mp3"
    hide hamayumi_cry
    show hamayumi_you at left
    hamayumi "А ради звука лопаты."
    voice "audio/Hamayumi/sand/21.mp3"
    hide hamayumi_you
    show hamayumi_you at left
    hamayumi "Вот это место."

    oliver "Я выкопаю весь песок!!!"

    sand "Тебе дадут выбор: взять зерно."
    sand "Маленькую вещь, которая будет напоминать: процесс тоже требует плату."

    menu:
        "Что тебе нужно"

        "Взять 'зерно' (артефакт - киберспейса)":
            $ sand_score += 1
            sand "Это напоминание."
            sand "О цене тишины."
            sand "Зерно как первый блок в стаках: незаметный, но запускающий цепочку."
            sand "Ты берёшь его - и уже не можешь делать вид, что ничего не выбирал."
            voice "audio/Hamayumi/sand/22.mp3"
            hide hamayumi_you
            show hamayumi_T at left
            hamayumi "О том, что пауза тоже платная."
            voice "audio/Hamayumi/sand/23.mp3"
            hide hamayumi_T
            show hamayumi_forw at left
            hamayumi "Платишь временем, вниманием и тем, что перестаёшь строить."

        "Купить песка (по связям)":
            # (реплики sand убраны - балл не начисляется)
            voice "audio/Hamayumi/sand/24.mp3"
            hide hamayumi_you
            show hamayumi_cry at left
            hamayumi "И снова станешь заметным."
            voice "audio/Hamayumi/sand/25.mp3"
            hide hamayumi_cry
            show hamayumi_you at left
            hamayumi "Потому что выбор - это всегда шум."

    # -------------------------
    # Экран 4 - граница ядра (неопределённость)
    # -------------------------
    with dissolve

    sand "Даже ядро не любит неопределённость."
    sand "Но оно терпит, пока ты тихий."
    sand "Пока ты не просишь у мира ответа."
    sand "Пока ты просто копаешь."
    oliver "Просто хочу тишины..."
    oliver "От голосов в голове..."
    voice "audio/Hamayumi/sand/26.mp3"
    hide hamayumi_you
    hide hamayumi_forw
    show hamayumi at left
    hamayumi "Тишина - это не награда."
    voice "audio/Hamayumi7/sand/27.mp3"
    hide hamayumi
    show hamayumi_up at left
    hamayumi "Это режим."
    voice "audio/Hamayumi/sand/28.mp3"
    hide hamayumi_up
    show hamayumi_T at left
    hamayumi "И режимы затягивают сильнее, чем запреты."

    # -------------------------
    # Экран 5 - итог + поворот
    # -------------------------
    with fade

    if sand_score == 3:
        $ sand_done = True
        sand "Если ты дойдёшь до ядра - тебе оставят нейтральный выход."
        sand "Как мир на мирной сложности: без победы, без поражения."
        sand "Просто бесконечный песок, который всегда можно копать."
        oliver "Ура я всегда хотела быть только с тобой только в таком состоянии"
        voice "audio/Hamayumi/sand/29.mp3"
        hide hamayumi_T
        show hamayumi_you at left
        hamayumi "Мир из песка. Без победы. Без поражения."
        voice "audio/Hamayumi/sand/30.mp3"
        hide hamayumi_you
        show hamayumi_cry at left
        hamayumi "И самое опасное: тебе там будет спокойно."
    else:
        $ sand_done = False
        sand "Ты ещё дергаешься."
        sand "Значит, пауза не твоя."
        oliver "Нет паузы бз кд ебашим"
        sand "Значит, ты копаешь - но всё ещё ждёшь, что копание ответит."
        voice "audio/Hamayumi/sand/31.mp3"
        hide hamayumi_T
        show hamayumi_forw at left
        hamayumi "Тишина не приняла тебя."
        voice "audio/Hamayumi/sand/32.mp3"
        hide hamayumi_forw
        show hamayumi_you at left
        hamayumi "Потому что ты всё ещё хочешь выйти из цикла, а не жить в нём."

    # Поворот: Sand раскрывает настоящее имя только в конце
    sand "И да... здесь меня зовут Песок."
    sand "Но у ядра другие имена."
    sand "Там я - Tarum."
    sand "Не потому что я меняюсь."
    sand "А потому что ты наконец смотришь прямо."
    oliver "Блять я так и знала"
    oliver "Я в своем познании настолько преисполнился, что я как будто бы уже"
    oliver "сто триллионов миллиардов лет проживаю на триллионах и"
    oliver "триллионах таких же планет, как эта Земля, мне этот мир абсолютно"
    oliver "понятен, и я здесь ищу только одного - покоя, умиротворения и"
    oliver "вот этой гармонии, от слияния с бесконечно вечным, от созерцания"
    oliver "великого фрактального подобия и от вот этого замечательного всеединства существа"

    hide sand
    with dissolve

    call ambient_reset
    jump act2_after_sand
