from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'tutorial'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ENDOWMENT_BLACK = 5
    ENDOWMENT_RED = 15
    ENDOWMENT_FUND = 19
    MULTIPLIER_BLACK = 0.1
    MULTIPLIER_RED = 1.0
    MULTIPLIER = 0.05
    CATASTROPH = 20
    INSTRUCTIONS_TEMPLATE = "tutorial/instructions.html"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    quiz1 = models.IntegerField(
        label='全体目標の提案が5人で(0,100,57,80,76)でした。どの値が目標に採択されますか',
        choices=[0,100,57,80,76]
        )
    quiz2 = models.FloatField(
        label='最終的に黒のチップを0枚、赤のチップを5枚、基金を19単位持ち、推測を1度的中しました。グループの貢献は合わせて75で、しきい値は64でした。報酬はいくらになりますか？',
        choices=[27.75, 28.75, 31.25],
    )

def creating_session(subsession):
    Player.participant.is_dropout = False
# PAGES
class Introduction(Page):
    pass

class Introduction_experiment(Page):
    pass

class experiment_test(Page):
    # timeout_seconds = 120
    # @staticmethod
    # def before_next_page(player, timeout_happened):
    #     if timeout_happened:
    #         player.pennyside = hogehoge
    form_model = 'player'
    form_fields = ['quiz1', 'quiz2']

    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(quiz1=76, quiz2=28.75)

        if values != solutions:
            return "答えが正しくありません"
    


page_sequence = [Introduction, Introduction_experiment, experiment_test]
