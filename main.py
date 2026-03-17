from random import randint
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Нанесение урона противнику."""
    if char_class == 'warrior':
        damage: int = 5 + randint(3, 5)
        return (f'{char_name} нанёс урон противнику равный {damage}')
    if char_class == 'mage':
        damage: int = 5 + randint(5, 10)
        return (f'{char_name} нанёс урон противнику равный {damage}')
    if char_class == 'healer':
        damage: int = 5 + randint(-3, -1)
        return (f'{char_name} нанёс урон противнику равный {damage}')
    return (f'{char_name} не нанёс урон противнику')


def defence(char_name: str, char_class: str) -> str:
    """Защита от урона."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return (f'{char_name} не блокировал урон')


def special(char_name: str, char_class: str) -> str:
    """Применение специальных умений."""
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение «Выносливость 105»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака 45»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита 40»')
    return (f'{char_name} не применил специальные умения')


def start_training(char_name: str, char_class: str) -> str:
    """Тренировка."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    text: str = ('Введи одну из команд: attack — чтобы атаковать противника, '
                 'defence — чтобы блокировать атаку противника '
                 'или special — чтобы использовать свою суперсилу.')
    print(text)
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Выбор персонажа."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        text_1: str = ('Введи название персонажа, за которого хочешь играть: '
                       'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        char_class = input(text_1)
        if char_class == 'warrior':
            text_warrior: str = ('Воитель — дерзкий воин ближнего боя. '
                                 'Сильный, выносливый и отважный.')
            print(text_warrior)
        if char_class == 'mage':
            text_mage: str = ('Маг — находчивый воин дальнего боя.'
                              ' Обладает высоким интеллектом.')
            print(text_mage)
        if char_class == 'healer':
            text_healer: str = ('Лекарь — могущественный заклинатель. '
                                'Черпает силы из природы, веры и духов.')
            print(text_healer)
        input_text: str = ('Нажми (Y), чтобы подтвердить выбор, '
                           'или любую другую кнопку, чтобы выбрать другого '
                           'персонажа ')
        approve_choice = input(input_text).lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
