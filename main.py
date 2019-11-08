'''
Federal University of Amazonas
Telephony Discipline
Prof. M.Sc. David Alan de O. Ferreira
'''


from libs.phone.telephony_sizing_lib import TelephonySizingLib as TP

if __name__ == '__main__':
    tplib = TP()
    
    A = 75.5
    C = 50
    
    GoS = tplib.erlang_b(A, C)
    print('GoS =', GoS*100, '%')
