from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='年齢を教えてください', min=13, max=125)
    gender = models.StringField(
        choices=[['男', '男'], ['女', '女'], ["その他", "その他"],["回答なし", "回答なし"]],
        label='性別を教えてください',
        widget=widgets.RadioSelect,
    )
    pd = models.StringField(
        choices=[['はい', 'はい'], ['いいえ', 'いいえ']],
        label='「ゲーム理論」、あるいは「囚人のジレンマ」を知っていますか？',
        widget=widgets.RadioSelect,
    )
    satisfaction = models.StringField(
        choices = [[1, "全く満足していない"],[2, "あまり満足していない"],[3, "どちらともいえない"],[4, "満足している"],[5, "非常に満足している"]],
        label='他の参加者の行動に満足していますか？',
        widget=widgets.RadioSelect,
    )
    enough = models.StringField(
        choices = [[1, "不十分だった"],[2, "少し不十分だった"],[3, "普通だった"],[4, "それなりであった"],[5, "十分であった"]],
        label='実験における自らのグループへの貢献は十分だったと考えていますか？',
        widget=widgets.RadioSelect,
    )

    check = models.LongStringField(
    label="ルールが分からないなど、実験中に何かトラブルなどはありませんでしたか？(自由回答)", blank=True
    )
    free = models.LongStringField(
    label="実験について感想やコメントがあれば、ご自由にお書きください。(自由回答)", blank=True
    )

    crt_bat = models.IntegerField(
        label='''
        1本のバットとボールが合計22ドルで売られています。
        バットは20ドルボールより高いです。
        ボールはいくらですか？'''
    )
    crt_widget = models.IntegerField(
        label='''
        製品を5個作るのに5分かかる機械があります。
        100台の機械で製品を100個作るには何分かかりますか？
        '''
    )
    crt_lake = models.IntegerField(
        label='''
        池に睡蓮の葉が浮かんでいます。
        毎日、その睡蓮は大きさが2倍に成長します。
        もし、池全体を覆うのに48日かかるとしたら、池の半分を覆うには何日かかりますか？
        '''
    )



# FUNCTIONS
# PAGES
class dropout(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.participant.is_dropout

class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget', 'crt_lake']

    @staticmethod
    def vars_for_template(player):
        participant = player.participant
        payoff=cu(participant.Final_REWARD)
        participant.Final_REWARD_JPY=payoff.to_real_world_currency(player.session)

class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender',"pd","satisfaction","enough","check","free"]
 

page_sequence = [dropout, CognitiveReflectionTest, Demographics]
