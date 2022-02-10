from otree.api import *

author = 'Tim Bonowski'

doc = """
Demographic Survey
"""

class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    LIKERT_CHOICES = [ (0, 'Strongly disagree'), (1, ''), (2, ''), (3, ''), (4, ''), (5,''),
                        (6, 'Strongly agree')]

    MORAL_IDENTITY = dict(
        feelgood='It would make me feel good to be a person who has these characteristics',
        important='Being someone who has those characteristics is an important part of who I am',
        clothes='I often where clothes that identify me as having these characteristics',
        ashamed='I would be ashamed to be a person who had these characteristics',
        hobby='The type of things I do in my spare time (e.g. hobbies) clearly identify me as having these characteristics',
        books='The kind of books and magazines that I read identify me as having these characteristics',
        having='Having these characteristics is not really important to me',
        membership='The fact that I have these characteristics is communicated to others by my membership in certain organizations',
        activities='I am actively involved in activities that communicate to others that I have these characteristics',
        desire='I strongly desire to have these characteristics',
    )

    MORAL_DISENGAGEMENT = dict(
        rumor='It is okay to spread rumors to defend those you care about',
        borrow='Taking something without the owner permission is okay as long as you\'re just borrowing it.',
        mispresent='Considering the way people grossly mispresenting themselves it\'s hardly a sin to inflate your credentials a bit.',
        questionable='People shouldn\'t be held accountable for doing questionable things',
        othertoo='People can can\'t be blamed for doing things that are technically wrong when others are doing that too.',
        credit='Taking personal credits for ideas that you do not own is no big idea',
        lack='Some people have to be treated roughly because they lack feelings that can be hurt',
        mistreat='People who get mistreated has usually done something to bring it on themselves'
    )


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def make_field(default):
    return models.StringField(
        choices=C.LIKERT_CHOICES,
        widget=widgets.RadioSelectHorizontal,
        label=C.LIKERT_CHOICES,
        default=default
    )

class Player(BasePlayer):

    #Moral Identity
    feelgood = make_field(C.MORAL_IDENTITY.get('feelgood'))
    important = make_field(C.MORAL_IDENTITY.get('important'))
    clothes = make_field(C.MORAL_IDENTITY.get('clothes'))
    ashamed = make_field(C.MORAL_IDENTITY.get('ashamed'))
    hobby = make_field(C.MORAL_IDENTITY.get('hobby'))
    books = make_field(C.MORAL_IDENTITY.get('books'))
    having = make_field(C.MORAL_IDENTITY.get('having'))
    membership = make_field(C.MORAL_IDENTITY.get('membership'))
    activities = make_field(C.MORAL_IDENTITY.get('activities'))
    desire = make_field(C.MORAL_IDENTITY.get('desire'))


    #Moral Disengagement
    rumor = make_field(C.MORAL_DISENGAGEMENT.get('rumor'))
    borrow = make_field(C.MORAL_DISENGAGEMENT.get('borrow'))
    mispresent = make_field(C.MORAL_DISENGAGEMENT.get('mispresent'))
    questionable = make_field(C.MORAL_DISENGAGEMENT.get('questionable'))
    othertoo = make_field(C.MORAL_DISENGAGEMENT.get('othertoo'))
    credit = make_field(C.MORAL_DISENGAGEMENT.get('credit'))
    lack = make_field(C.MORAL_DISENGAGEMENT.get('lack'))
    mistreat = make_field(C.MORAL_DISENGAGEMENT.get('mistreat'))
    #for i,k in enumerate(C.MORAL_IDENTITY.keys()):
        #k = make_field([v for v in C.MORAL_IDENTITY.values()][i] )
        #print([key for key in C.MORAL_IDENTITY.keys()][i])
    #del i,k

    #for i in range(len(C.MORAL_IDENTITY)):
        #[k for k in C.MORAL_IDENTITY.keys()][i] = make_field([v for v in C.MORAL_IDENTITY.values()][i])
    #del i


# PAGES
class MoralIdentity(Page):
    form_model = 'player'
    form_fields = [k for k in C.MORAL_IDENTITY.keys()]
    #form_fields = [ [k for k in C.MORAL_IDENTITY.keys()][i] for i in range(len(C.MORAL_IDENTITY)) ]
    #first list comprehension create a list of keys, then subscript them to refer to them in the second list comprehension


class MoralDisengagement(Page):
    form_model = 'player'
    form_fields = [k for k in C.MORAL_DISENGAGEMENT.keys()]

class ResultSurvey(Page):
    @staticmethod
    def vars_for_template(player):
        return dict(
            feelgood=player.feelgood,
            rumor=player.rumor,
        )


page_sequence = [MoralIdentity,
                MoralDisengagement,
                ResultSurvey]
