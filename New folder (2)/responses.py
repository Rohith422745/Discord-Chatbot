from random import choice,randint


def get_response(user_input: str) -> str: 
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well,You are very silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'fine what about you'
    elif 'bye' in lowered:
        return 'thank you! come again'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,7)}'
    elif 'sing me a song' in lowered:
        return 'search in google'
    else:
        return choice(['What! i do not understand....',
                       'Can you repeat it I cannot understand it?',
                       'just search in google okay?'])