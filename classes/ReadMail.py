from classes.Commands import OpenMail, DeleteGatheringReport, SelectExploreMail, ClickTelescope, ClickPresentIcon
from classes.Commands import ClickOnNida, ClickInvestigation, SendScoutButton, ClaimPrize, RemoveOldCaveMessage
from classes.Commands import RemoveWarReport, ClickReport, RemoveActionPointRefund
from time import sleep


class ReadMail:
    def __init__(self):
        pass

    @staticmethod
    def start():
        OpenMail().do_work()
        ClickReport().do_work()
        DeleteGatheringReport().do_work()
        RemoveActionPointRefund().do_work()
        RemoveOldCaveMessage().do_work()
        RemoveWarReport().do_work()
        SelectExploreMail().do_work()
        ClaimPrize().do_work()
        ClickTelescope().do_work()
        ClickPresentIcon().do_work()
        ClickOnNida().do_work()
        ClickInvestigation().do_work()
        SendScoutButton().do_work()
