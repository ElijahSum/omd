# Guido van Rossum <guido@python.org>
def options_checker():
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    return options[option]


def step2_umbrella():
    print('По дороге в бар вы видите гусыню, совсем замерзшую от дождя.'
          ' Предложить ли ей укрыться под зонтом от дождя?')
    if options_checker():
        print('Утка завела нового друга! Теперь вы направляетесь вместе в бар,'
              ' обсуждая малярное дело')
    else:
        print('🦆 проходит мимо, отправляется в бар в грустном одиночестве.'
              ' После второй пинты было принято решение вернуться домой')


def step2_no_umbrella():
    print('Наша немного промокшая утка всё же решает продолжить путь. '
          'Стоит ли найти кого-то с зонтиком?')
    if options_checker():
        print('Утка теперь под зонтиком и с новым другом!'
              ' Теперь вы направляетесь вместе в бар,')
    else:
        print('Дождь усиливается. Утка 🦆 понимает, '
              'что нет смысла продолжать идти без зонта. '
              'Придется вернуться домой')


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    print('Утка 🦆 идет в сторону бара, как вдруг начинается дождик')
    if options_checker():
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
