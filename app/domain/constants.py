from collections import namedtuple

WELCOME_MESSAGE = "Привет {}!\n" \
                  "Это бот с расписанием для GSTU\n\n" \
                  "Создатель - @dopefile\n" \
                  "Исходники - https://github.com/dop3file/schedule"

CHOOSE_GROUP_TEXT = "Выберите группу"
CHOOSE_SUBGROUP_TEXT = "Выберите подгруппу"

CHOOSE_GROUP_FINAL_TEXT = "Прекрасно!\nТеперь пропишите /start"
SETTINGS = "Еще"

DAYS = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница"
]

NUMBERS_EMOJI = {
    1: "1️⃣",
    2: "2️⃣",
    3: "3️⃣",
    4: "4️⃣",
    5: "5️⃣",
    6: "6️⃣"
}

TIME_BORDER = namedtuple("TIME_BORDER", "left_time_border right_time_border")

TIME_WINDOWS = {
    1: TIME_BORDER("8:20", "9:45"),
    2: TIME_BORDER("10:00", "11:25"),
    3: TIME_BORDER("11:35", "13:00"),
    4: TIME_BORDER("13:30", "14:55"),
    5: TIME_BORDER("15:05", "16:30")
}