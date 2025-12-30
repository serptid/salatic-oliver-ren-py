init python:
    SW = config.screen_width
    SH = config.screen_height
#Фоны
image bg hospital_room = Transform("gui/images/bg/hospital.png", xysize=(SW, SH))
image bg cyberspace_city = Transform("gui/images/bg/cyberspace_city.png", xysize=(SW, SH))
image bg cyberspace_void = Transform("gui/images/bg/cyberspace_void.png", xysize=(SW, SH))
image bg hospital_office = Transform("images/hospital_office.png", xysize=(SW, SH))
image bg cyberspace_market = Transform("images/cyberspace_market.png", xysize=(SW, SH))


#Персонажи
image nurse = Transform(
    "gui/images/ch/nurse.png",
    ysize=int(config.screen_height * 0.9)
)
image hamayumi = Transform(
    "gui/images/ch/Hamayumi/norm.png",
    ysize=int(config.screen_height * 0.9),
    xysize=(int(config.screen_width * 0.5), int(config.screen_height * 0.9))
)
image quins = Transform(
    "gui/images/ch/quins/quins.png",
    ysize=int(config.screen_height * 0.9),
    xysize=(int(config.screen_width * 0.5), int(config.screen_height * 0.9))
)
image zombi = Transform(
    "gui/images/ch/zombi/norm.png",
    ysize=int(config.screen_height * 0.9),
    xysize=(int(config.screen_width * 0.5), int(config.screen_height * 0.9))
)
image nighstess = Transform(
    "gui/images/ch/nighstess/norm.png",
    ysize=int(config.screen_height * 0.9),
    xysize=(int(config.screen_width * 0.5), int(config.screen_height * 0.9))
)