from otree.api import *


doc = """
Cheating Paradigm game
"""

author = "Tim Bonowski"

class C(BaseConstants):
    #CORE CONSTANTS
    NAME_IN_URL = 'coin_flip'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 4

    TREATMENTS = ['Phone', 'Zoom', 'Email', 'Mailbox']

    PASSWORD_WIN = 'abc'
    PASSWORD_LOSE = 'xyz'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    communication_mode = models.StringField()
    password = models.StringField()

def creating_session(subsession):
    import itertools
    if subsession.round_number == 1:
        communication_modes = itertools.cycle(C.TREATMENTS)
        for player in subsession.get_players():
            participant = player.participant #fixed treatment on participant and not player so that it would not change between rounds
            participant.communication_mode = next(communication_modes) #need to add this field in setting.py


# PAGES
class Einfuehrung(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

class FlipCoin(Page):
    pass


class CommunicationMode(Page):
    form_model = 'player'
    form_fields = ['password']

    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        return dict(
            participant_communication_mode=participant.communication_mode,
        )
    @staticmethod
    def error_message(player, values):
        if values['password'] != C.PASSWORD_WIN and values['password'] != C.PASSWORD_LOSE:
            return f'Wrong password!'



class ResultsWaitPage(WaitPage):
    @staticmethod
    def after_all_players_arrive(group : Group):
        pass


class Results(Page):
    pass


page_sequence = [Einfuehrung,
                 FlipCoin,
                 CommunicationMode,
                 ResultsWaitPage,
                 Results]
