label act2_entry:
    scene cyberspace_city
    with dissolve

    hamayumi "Точка выбора — не меню."
    hamayumi "Это маршрут."

    "Город сжимается и ведёт тебя туда, где меньше шума."

    jump branch_quins


label act2_after_quins:
    scene cyberspace_city
    with dissolve

    "После Quins город кажется строже."
    "Как будто тебя измерили и отпустили."

    hamayumi "Ты заплатил не деньгами."

    jump branch_nighstess


label act2_after_nighstess:
    scene cyberspace_pause
    with dissolve

    "Спокойствие ложится ровным слоем."
    "Слишком ровным."

    hamayumi "Так выглядит согласие."

    jump branch_sand


label act2_after_sand:
    scene cyberspace_edge
    with dissolve

    "Пауза тянется дольше, чем нужно."
    "Мир ждёт, пока ты снова станешь заметным."

    hamayumi "Тебя возвращают."

    jump branch_hospital


label act2_transition:
    scene cyberspace_city
    with fade

    "Все линии сходятся."
    "Город снова целый."

    hamayumi "Акт закрывается."
    hamayumi "Дальше — ядро."

    jump act3_entry
