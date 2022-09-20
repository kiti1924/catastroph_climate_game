from re import A
from otree.api import *
import random
import numpy as np

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'ccg'
    PLAYERS_PER_GROUP = 5
    NUM_ROUNDS = 1
    ENDOWMENT_BLACK = 5
    ENDOWMENT_RED = 15
    ENDOWMENT_FUND = 19
    MULTIPLIER_BLACK = 0.1
    MULTIPLIER_RED = 1.0
    MULTIPLIER = 0.05
    THRESHOLD = random.randint(50,100)
    CATASTROPH = 20
    INSTRUCTIONS_TEMPLATE = "ccg/instructions.html"
    TIMEOUT_SEC = 60*2
    TIMEOUT_SEC_L = 60*4
    ESTIMATE_POINT = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    Target = models.IntegerField(initial=0)
    target1 = models.IntegerField(initial=0)
    target2 = models.IntegerField(initial=0)
    target3 = models.IntegerField(initial=0)
    target4 = models.IntegerField(initial=0)
    target5 = models.IntegerField(initial=0)
    prob_Target = models.FloatField(initial=0)

    Fpledge = models.IntegerField(initial=0)
    fpledge1 = models.IntegerField(initial=0)
    fpledge2 = models.IntegerField(initial=0)
    fpledge3 = models.IntegerField(initial=0)
    fpledge4 = models.IntegerField(initial=0)
    fpledge5 = models.IntegerField(initial=0)
    prob_Fpledge = models.FloatField(initial=0)

    Exante1 = models.FloatField(initial=0.1)
    Exante2 = models.FloatField(initial=0.1)
    Exante3 = models.FloatField(initial=0.1)
    Exante4 = models.FloatField(initial=0.1)
    Exante5 = models.FloatField(initial=0.1)

    Fcontribution = models.IntegerField(initial=0)
    fcontribution1_red = models.IntegerField(initial=0)
    fcontribution2_red = models.IntegerField(initial=0)
    fcontribution3_red = models.IntegerField(initial=0)
    fcontribution4_red = models.IntegerField(initial=0)
    fcontribution5_red = models.IntegerField(initial=0)
    fcontribution1_black = models.IntegerField(initial=0)
    fcontribution2_black = models.IntegerField(initial=0)
    fcontribution3_black = models.IntegerField(initial=0)
    fcontribution4_black = models.IntegerField(initial=0)
    fcontribution5_black = models.IntegerField(initial=0)
    prob_Fcontribution = models.FloatField(initial=0)

    Midterm1 = models.FloatField(initial=0.1)
    Midterm2 = models.FloatField(initial=0.1)
    Midterm3 = models.FloatField(initial=0.1)
    Midterm4 = models.FloatField(initial=0.1)
    Midterm5 = models.FloatField(initial=0.1)

    Scontribution = models.IntegerField(initial=0)
    scontribution1_red = models.IntegerField(initial=0)
    scontribution2_red = models.IntegerField(initial=0)
    scontribution3_red = models.IntegerField(initial=0)
    scontribution4_red = models.IntegerField(initial=0)
    scontribution5_red = models.IntegerField(initial=0)
    scontribution1_black = models.IntegerField(initial=0)
    scontribution2_black = models.IntegerField(initial=0)
    scontribution3_black = models.IntegerField(initial=0)
    scontribution4_black = models.IntegerField(initial=0)
    scontribution5_black = models.IntegerField(initial=0)
    prob_Scontribution = models.FloatField(initial=0)

    contributions = models.IntegerField(initial=0)
    contribution1 = models.IntegerField(initial=0)
    contribution2 = models.IntegerField(initial=0)
    contribution3 = models.IntegerField(initial=0)
    contribution4 = models.IntegerField(initial=0)
    contribution5 = models.IntegerField(initial=0)    

    Expost1 = models.FloatField(initial=0.1)
    Expost2 = models.FloatField(initial=0.1)
    Expost3 = models.FloatField(initial=0.1)
    Expost4 = models.FloatField(initial=0.1)
    Expost5 = models.FloatField(initial=0.1)

class Player(BasePlayer):
    Pis_dropout = models.BooleanField(initial=False)
    target = models.IntegerField(
        label="提案する全体目標を入力してください", 
        choices=[n for n in range(0,101)]
    )
    first_pledge = models.IntegerField(
        label="誓約する赤と黒のチップの合計貢献量を入力してください", 
        choices=[n for n in range(C.ENDOWMENT_RED + C.ENDOWMENT_BLACK +1)]
    )
    estimate = models.IntegerField(
        label="他参加者4人の平均貢献額の予測を入力してください。", 
        choices=[n for n in range(0,21)]
    )
    ex_ante1 = models.IntegerField(
        label="P1に対する評価を入力してください", 
        choices=[n+1 for n in range(6)],
        widget=widgets.RadioSelectHorizontal
    )
    ex_ante2 = models.IntegerField(
        label="P2に対する評価を入力してください", 
        choices=[n+1 for n in range(6)],
        widget=widgets.RadioSelectHorizontal
    )
    ex_ante3 = models.IntegerField(
        label="P3に対する評価を入力してください", 
        choices=[n+1 for n in range(6)],
        widget=widgets.RadioSelectHorizontal
    )
    ex_ante4 = models.IntegerField(
        label="P4に対する評価を入力してください", 
        choices=[n+1 for n in range(6)],
        widget=widgets.RadioSelectHorizontal
    )
    ex_ante5 = models.IntegerField(
        label="P5に対する評価を入力してください", 
        choices=[n+1 for n in range(6)],
        widget=widgets.RadioSelectHorizontal
    )

    first_contribution_red = models.IntegerField(
        label="1回目の赤のチップの貢献量を入力してください", 
        choices=[n for n in range(C.ENDOWMENT_RED +1)], 
        initial=0
    )
    first_contribution_black = models.IntegerField(
        label="1回目の黒のチップの貢献量を入力してください", 
        choices=[n for n in range(C.ENDOWMENT_BLACK +1)],
        initial=0
    )
    

    mid_term1 = models.IntegerField(
        label="P1に対する評価を入力してください", 
        choices=[n+1 for n in range(6)],
        widget=widgets.RadioSelectHorizontal
    )
    mid_term2 = models.IntegerField(
        label="P2に対する評価を入力してください", 
        choices=[n+1 for n in range(6)],
        widget=widgets.RadioSelectHorizontal
    )
    mid_term3 = models.IntegerField(
        label="P3に対する評価を入力してください", 
        choices=[n+1 for n in range(6)],
        widget=widgets.RadioSelectHorizontal
    )
    mid_term4 = models.IntegerField(
        label="P4に対する評価を入力してください", 
        choices=[n+1 for n in range(6)],
        widget=widgets.RadioSelectHorizontal
    )
    mid_term5 = models.IntegerField(
        label="P5に対する評価を入力してください", 
        choices=[n+1 for n in range(6)],
        widget=widgets.RadioSelectHorizontal
    )    

    second_contribution_red = models.IntegerField(
        label="2回目の赤のチップの貢献量を入力してください", 
        choices=[n for n in range(C.ENDOWMENT_RED +1)], 
        initial=0
    )
    second_contribution_black = models.IntegerField(
        label="2回目の黒のチップの貢献量を入力してください", 
        choices=[n for n in range(C.ENDOWMENT_BLACK +1)], 
        initial=0
    )
    avg_contribution = models.FloatField(initial=0)

    ex_post1 = models.IntegerField(
        label="P1に対する評価を入力してください", 
        choices=[n+1 for n in range(6)],
        widget=widgets.RadioSelectHorizontal
    )
    ex_post2 = models.IntegerField(
        label="P2に対する評価を入力してください", 
        choices=[n+1 for n in range(6)],
        widget=widgets.RadioSelectHorizontal
    )
    ex_post3 = models.IntegerField(
        label="P3に対する評価を入力してください", 
        choices=[n+1 for n in range(6)],
        widget=widgets.RadioSelectHorizontal
    )
    ex_post4 = models.IntegerField(
        label="P4に対する評価を入力してください", 
        choices=[n+1 for n in range(6)],
        widget=widgets.RadioSelectHorizontal
    )
    ex_post5 = models.IntegerField(
        label="P5に対する評価を入力してください", 
        choices=[n+1 for n in range(6)],
        widget=widgets.RadioSelectHorizontal
    )    



@staticmethod
def set_Target(group: Group):
    players = group.get_players()
    targets = [p.target for p in players]
    group.Target=np.median(targets)
    if group.Target <=50:
        group.prob_Target=100
    else :
        group.prob_Target=100-((group.Target - 50)*2)
    (group.target1, group.target2, group.target3, group.target4, group.target5)=targets
    
@staticmethod
def set_First_pledge(group: Group):
    players = group.get_players()
    first_pledges = [p.first_pledge for p in players]
    group.Fpledge = sum(first_pledges)
    (group.fpledge1, group.fpledge2, group.fpledge3, group.fpledge4, group.fpledge5)=first_pledges
    if group.Fpledge <=50:
        group.prob_Fpledge=100
    else :
        group.prob_Fpledge=100-((group.Target - 50)*2)
    
@staticmethod
def set_Ex_ante(group):
    players = group.get_players()
    exantes_1 = [p.ex_ante1 for p in players]
    del exantes_1[0]
    group.Exante1 = sum(exantes_1)/(C.PLAYERS_PER_GROUP -1)
    exantes_2 = [p.ex_ante2 for p in players]
    del exantes_2[1]
    group.Exante2 = sum(exantes_2)/(C.PLAYERS_PER_GROUP -1)
    exantes_3 = [p.ex_ante3 for p in players]
    del exantes_3[2]
    group.Exante3 = sum(exantes_3)/(C.PLAYERS_PER_GROUP -1)
    exantes_4 = [p.ex_ante4 for p in players]
    del exantes_4[3]
    group.Exante4 = sum(exantes_4)/(C.PLAYERS_PER_GROUP -1)
    exantes_5 = [p.ex_ante5 for p in players]
    del exantes_5[4]
    group.Exante5 = sum(exantes_5)/(C.PLAYERS_PER_GROUP -1)
    
@staticmethod
def set_First_contribution(group: Group):
    players = group.get_players()
    first_contributions_red = [p.first_contribution_red for p in players]
    first_contributions_black = [p.first_contribution_black for p in players]
    group.Fcontribution = sum(first_contributions_red)+sum(first_contributions_black)
    (group.fcontribution1_red, group.fcontribution2_red, group.fcontribution3_red, group.fcontribution4_red, group.fcontribution5_red)=first_contributions_red
    (group.fcontribution1_black, group.fcontribution2_black, group.fcontribution3_black, group.fcontribution4_black, group.fcontribution5_black)=first_contributions_black
    if group.Fcontribution <=50:
        group.prob_Fcontribution=100
    else :
        group.prob_Fcontribution=100-((group.Fcontribution - 50)*2)
    
@staticmethod
def set_Mid_term(group):
    players = group.get_players()
    midterms_1 = [p.mid_term1 for p in players]
    del midterms_1[0]
    group.Midterm1 = sum(midterms_1)/(C.PLAYERS_PER_GROUP -1)
    midterms_2 = [p.mid_term2 for p in players]
    del midterms_2[1]
    group.Midterm2 = sum(midterms_2)/(C.PLAYERS_PER_GROUP -1)
    midterms_3 = [p.mid_term3 for p in players]
    del midterms_3[2]
    group.Midterm3 = sum(midterms_3)/(C.PLAYERS_PER_GROUP -1)
    midterms_4 = [p.mid_term4 for p in players]
    del midterms_4[3]
    group.Midterm4 = sum(midterms_4)/(C.PLAYERS_PER_GROUP -1)
    midterms_5 = [p.mid_term5 for p in players]
    del midterms_5[4]
    group.Midterm5 = sum(midterms_5)/(C.PLAYERS_PER_GROUP -1)

@staticmethod
def set_Second_contribution(group: Group):
    players = group.get_players()
    second_contributions_red = [p.second_contribution_red for p in players]
    second_contributions_black = [p.second_contribution_black for p in players]
    fred = [p.first_contribution_red for p in players]
    fblack = [p.first_contribution_black for p in players]
    contributions =[fr + fb + sr + sb for (fr,fb,sr,sb) in zip(fred,fblack,second_contributions_red,second_contributions_black)]
    (group.contribution1, group.contribution2, group.contribution3, group.contribution4, group.contribution5)=contributions

    group.Scontribution = sum(second_contributions_red)+sum(second_contributions_black)+group.Fcontribution
    (group.scontribution1_red, group.scontribution2_red, group.scontribution3_red, group.scontribution4_red, group.scontribution5_red)=second_contributions_red
    (group.scontribution1_black, group.scontribution2_black, group.scontribution3_black, group.scontribution4_black, group.scontribution5_black)=second_contributions_black
    if group.Scontribution <=50:
        group.prob_Scontribution=100
    else :
        group.prob_Scontribution=100-((group.Scontribution - 50)*2)

@staticmethod
def set_Ex_post(group):
    players = group.get_players()
    exposts_1 = [p.ex_post1 for p in players]
    del exposts_1[0]
    group.Expost1 = sum(exposts_1)/(C.PLAYERS_PER_GROUP -1)
    exposts_2 = [p.ex_post2 for p in players]
    del exposts_2[1]
    group.Expost2 = sum(exposts_2)/(C.PLAYERS_PER_GROUP -1)
    exposts_3 = [p.ex_post3 for p in players]
    del exposts_3[2]
    group.Expost3 = sum(exposts_3)/(C.PLAYERS_PER_GROUP -1)
    exposts_4 = [p.ex_post4 for p in players]
    del exposts_4[3]
    group.Expost4 = sum(exposts_4)/(C.PLAYERS_PER_GROUP -1)
    exposts_5 = [p.ex_post5 for p in players]
    del exposts_5[4]
    group.Expost5 = sum(exposts_5)/(C.PLAYERS_PER_GROUP -1)

    


# PAGES
class ExperimentWaitPage(WaitPage):
    group_by_arrival_time = True


class Pledge_Target(Page):
    form_model = "player"
    form_fields = ["target"]
    timeout_seconds = C.TIMEOUT_SEC

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        player.Pis_dropout = False
        participant.is_dropout = player.Pis_dropout
        if timeout_happened:
            player.target = 0
            player.Pis_dropout = True
            participant.is_dropout = player.Pis_dropout



class TargetWaitPage(WaitPage):
    after_all_players_arrive = set_Target


class Target_Pledge_individual(Page):
    form_model = "player"
    form_fields = ["first_pledge"]
    @staticmethod
    def get_timeout_seconds(player):
        if player.Pis_dropout:
            return 1  # instant timeout, 1 second
        else:
            return C.TIMEOUT_SEC

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if timeout_happened:
            player.first_pledge = 0
            player.Pis_dropout = True
            participant.is_dropout = player.Pis_dropout



class FpledgeWaitPage(WaitPage):
    after_all_players_arrive = set_First_pledge


class estimate_ex_ante_review(Page):
    form_model = "player"
    form_fields = ["ex_ante1", "ex_ante2", "ex_ante3", "ex_ante4", "ex_ante5", "estimate"]
    @staticmethod
    def get_timeout_seconds(player):
        if player.Pis_dropout:
            return 1  # instant timeout, 1 second
        else:
            return C.TIMEOUT_SEC_L

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if timeout_happened:
            player.ex_ante1 = 6
            player.ex_ante2 = 6
            player.ex_ante3 = 6
            player.ex_ante4 = 6
            player.ex_ante5 = 6
            player.estimate = 100
            player.Pis_dropout = True
            participant.is_dropout = player.Pis_dropout

class ExanteWaitPage(WaitPage):
    after_all_players_arrive = set_Ex_ante


class ex_ante_fcontribution(Page):
    @staticmethod
    def vars_for_template(player):
        Exante_MAX = max(player.group.Exante1, player.group.Exante2, player.group.Exante3, player.group.Exante4, player.group.Exante5)
        Exante_min = min(player.group.Exante1, player.group.Exante2, player.group.Exante3, player.group.Exante4, player.group.Exante5)
        return dict(
        Exante_MAX = Exante_MAX, 
        Exante_min = Exante_min
        )
    form_model = "player"
    form_fields = ["first_contribution_red", "first_contribution_black"]
    @staticmethod
    def get_timeout_seconds(player):
        if player.Pis_dropout:
            return 1  # instant timeout, 1 second
        else:
            return C.TIMEOUT_SEC

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if timeout_happened:
            player.first_contribution_red = 0
            player.first_contribution_black = 0
            player.Pis_dropout = True
            participant.is_dropout = player.Pis_dropout
class FcontributionWaitPage(WaitPage):
     after_all_players_arrive = set_First_contribution



class fcontribution_mid_term_review(Page):
    form_model = "player"
    form_fields = ["mid_term1", "mid_term2", "mid_term3", "mid_term4", "mid_term5"]
    @staticmethod
    def get_timeout_seconds(player):
        if player.Pis_dropout:
            return 1  # instant timeout, 1 second
        else:
            return C.TIMEOUT_SEC_L

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if timeout_happened:
            player.mid_term1 = 6
            player.mid_term2 = 6
            player.mid_term3 = 6
            player.mid_term4 = 6
            player.mid_term5 = 6
            player.Pis_dropout = True
            participant.is_dropout = player.Pis_dropout

class MidtermWaitPage(WaitPage):
    after_all_players_arrive = set_Mid_term


class mid_term_scontribution(Page):
    @staticmethod
    def vars_for_template(player):
        Midterm_MAX = max(player.group.Midterm1, player.group.Midterm2, player.group.Midterm3, player.group.Midterm4, player.group.Midterm5)
        Midterm_min = min(player.group.Midterm1, player.group.Midterm2, player.group.Midterm3, player.group.Midterm4, player.group.Midterm5)
        return dict(
        Midterm_MAX = Midterm_MAX, 
        Midterm_min = Midterm_min
        )
    form_model = "player"
    form_fields = ["second_contribution_red", "second_contribution_black"]

    @staticmethod
    def get_timeout_seconds(player):
        if player.Pis_dropout:
            return 1  # instant timeout, 1 second
        else:
            return C.TIMEOUT_SEC

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if timeout_happened:
            player.second_contribution_red = 0
            player.second_contribution_black = 0
            player.Pis_dropout = True
            participant.is_dropout = player.Pis_dropout
    @staticmethod    
    def error_message(player, values):
        if values["second_contribution_red"] + player.first_contribution_red >= C.ENDOWMENT_RED +1:
            return "貢献の合計が所持している赤のチップの枚数を超えています"
        elif values["second_contribution_black"] + player.first_contribution_black >= C.ENDOWMENT_BLACK+1:
            return "貢献の合計が所持している黒のチップの枚数を超えています"
        #この函数の動作が明確におかしい

class ScontributionWaitPage(WaitPage):
    after_all_players_arrive = set_Second_contribution

class scontribution_ex_post_review(Page):
    form_model = "player"
    form_fields = ["ex_post1", "ex_post2", "ex_post3", "ex_post4", "ex_post5"]
    @staticmethod
    def get_timeout_seconds(player):
        if player.Pis_dropout:
            return 1  # instant timeout, 1 second
        else:
            return C.TIMEOUT_SEC_L

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        contribution=[player.group.contribution1, player.group.contribution2, player.group.contribution3, player.group.contribution4, player.group.contribution5]
        del contribution[player.id_in_group -1]
        player.avg_contribution = sum(contribution)/(C.PLAYERS_PER_GROUP -1)
        if player.estimate < player.avg_contribution -1 or player.estimate > player.avg_contribution +1:
            participant.hit_estimate = False
        else:
            participant.hit_estimate = True
    
        if timeout_happened:
            player.ex_post1 = 6
            player.ex_post2 = 6
            player.ex_post3 = 6
            player.ex_post4 = 6
            player.ex_post5 = 6
            player.Pis_dropout = True
            participant.is_dropout = player.Pis_dropout

class ExpostWaitPage(WaitPage):
    after_all_players_arrive = set_Ex_post



class ex_post_wheel(Page):
    @staticmethod
    def is_displayed(player):
        return player.Pis_dropout == False
    @staticmethod
    def vars_for_template(player):
        Expost_MAX = max(player.group.Expost1, player.group.Expost2, player.group.Expost3, player.group.Expost4, player.group.Expost5)
        Expost_min = min(player.group.Expost1, player.group.Expost2, player.group.Expost3, player.group.Expost4, player.group.Expost5)
        return dict(
        Expost_MAX = Expost_MAX, 
        Expost_min = Expost_min
        )

class wheel_result(Page):
    @staticmethod
    def is_displayed(player):
        return player.Pis_dropout == False
    @staticmethod
    def vars_for_template(player):
        participant=player.participant
        participant.Final_CONTRIBUTION = player.group.Scontribution
        participant.Final_BLACK = C.ENDOWMENT_BLACK - (player.first_contribution_black + player.second_contribution_black)
        participant.Final_RED = C.ENDOWMENT_RED - (player.first_contribution_red + player.second_contribution_red)
        if participant.Final_CONTRIBUTION > C.THRESHOLD:
            if participant.hit_estimate:
                participant.Final_REWARD = (player.participant.Final_BLACK * C.MULTIPLIER_BLACK) + (player.participant.Final_RED * C.MULTIPLIER_RED) + (player.participant.Final_CONTRIBUTION * C.MULTIPLIER) + C.ENDOWMENT_FUND + C.ESTIMATE_POINT
            else:
                participant.Final_REWARD = (player.participant.Final_BLACK * C.MULTIPLIER_BLACK) + (player.participant.Final_RED * C.MULTIPLIER_RED) + (player.participant.Final_CONTRIBUTION * C.MULTIPLIER) + C.ENDOWMENT_FUND
        else:
            if participant.hit_estimate:
                participant.Final_REWARD = (player.participant.Final_BLACK * C.MULTIPLIER_BLACK) + (player.participant.Final_RED * C.MULTIPLIER_RED) + (player.participant.Final_CONTRIBUTION * C.MULTIPLIER) + C.ENDOWMENT_FUND - C.CATASTROPH + C.ESTIMATE_POINT
            else:
                participant.Final_REWARD = (player.participant.Final_BLACK * C.MULTIPLIER_BLACK) + (player.participant.Final_RED * C.MULTIPLIER_RED) + (player.participant.Final_CONTRIBUTION * C.MULTIPLIER) + C.ENDOWMENT_FUND - C.CATASTROPH

page_sequence = [ExperimentWaitPage, 
Pledge_Target, TargetWaitPage, 
Target_Pledge_individual, FpledgeWaitPage, 
estimate_ex_ante_review, ExanteWaitPage, 
ex_ante_fcontribution, FcontributionWaitPage, 
fcontribution_mid_term_review, MidtermWaitPage,
mid_term_scontribution, ScontributionWaitPage,
scontribution_ex_post_review, ExpostWaitPage,
ex_post_wheel, wheel_result]
