'''
Federal University of Amazonas
Telephony Discipline
Prof. M.Sc. David Alan de O. Ferreira
'''


class TelephonySizingLib:


    def __init__(self):
        pass


    def __factorial(self, n):
        fact = 1
        for i in range(2, n+1):
            fact *= i

        return fact


    def erlang_b(self, A, C):
        # Erlang B formula for sizing the
        # number of trunks in a telephone system.
        num = (A ** C)/self.__factorial(C)

        den = 0
        for k in range(C+1):
            den += (A ** k)/self.__factorial(k)

        GoS = num/den
        
        return GoS
