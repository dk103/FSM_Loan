from pydispatch import dispatcher
import threading
import time
import random


TAXFILING_SIGNAL='taxfiling_signal'
TAXFILING_SENDER='taxfiling_sender'
PORTAL_SIGNAL='portal_signal'
PORTAL_SENDER='portal_sender'

class TaxFiling:

    def __init__(self,amtPaid,taxAmt,panNumber):
        self._amtPaid=  amtPaid
        self._taxAmt =  taxAmt
        self._panNumber = panNumber



    @property
    def amtPaid(self):
        return self._amtPaid

    @property
    def taxAmt(self):
        return self._taxAmt

    @property
    def panNumber(self):
        return self._panNumber

    def __str__(self):
        return str(self.__dict__)


class TaxFilingService():

    def __init__(self):
        self._status = 'NOT-FILED'
        dispatcher.connect(self.filing_dispatcher_receive, signal=PORTAL_SIGNAL, sender=PORTAL_SENDER)
        self.taxFiling()


    @property
    def status(self):
        return self._status

    def getTaxAmtStatus(self):
        if self.settleMentStatus:
            return "REFUND"
        else:
            return "DEPOSIT"

    def filing_dispatcher_receive(self,taxInfo=None,message=None):
        if message :
            print(message)
        else:

            amt = 0
            if taxInfo.taxAmt > taxInfo.amtPaid:
                result_status = 'DEPOSIT'
                amt = taxInfo.taxAmt - taxInfo.amtPaid

            elif taxInfo.amtPaid > taxInfo.taxAmt:
                result_status = 'REFUND'
                amt = taxInfo.amtPaid - taxInfo.taxAmt

            dispatcher.send(message = (result_status,amt,taxInfo.panNumber), signal=TAXFILING_SIGNAL, sender=TAXFILING_SENDER)

    def taxFiling(self):
        while (1):
            dispatcher.send(message='******************please Fill before August 21*****************', signal=TAXFILING_SIGNAL, sender=TAXFILING_SENDER)
            time.sleep(15)



class PortalUserFeedService():

    def __init__(self):
        dispatcher.connect(self.portal_dispatcher_receive, signal=TAXFILING_SIGNAL, sender=TAXFILING_SENDER)
        self.userFeedService()


    def portal_dispatcher_receive(self,message):

        if not isinstance(message,str):
            print('------File Status for {} is {} for an amt {}----------'.format(message[2],message[0],message[1]))
            dispatcher.send(message="IT Return complete ", signal=PORTAL_SIGNAL, sender=PORTAL_SENDER)
        else:
            print("******************************* IMP: NEW **********************")
            print("*********" +message+"**********")


    def userFeedService(self):
        flag = ["deposit", "refund"]
        while (1):
            print('portal service is on')
            dispatcher.send(taxInfo=self.getUserRandomTaxInfo(flag[random.randint(0,1)]), signal=PORTAL_SIGNAL, sender=PORTAL_SENDER)
            time.sleep(20)

    @staticmethod
    def getUserRandomTaxInfo(flag):
        amtPaid = 0
        taxableAmt = random.randint(600, 1000)
        if flag == 'deposit':
            amtPaid = random.randint(400, 600)

        else:
            amtPaid = random.randint(1000, 1200)

        panNumber = "BLHPM"+ str(random.randint(1111,2334))

        taxUser= TaxFiling(amtPaid,taxableAmt,panNumber)
        print("user Created -"+ str(taxUser))
        return taxUser

if __name__ == '__main__':
        portal_thread = threading.Thread(target=PortalUserFeedService)
        portal_thread.start()
        filing_thread = threading.Thread(target=TaxFilingService)
        filing_thread.start()


