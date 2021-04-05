import lab2
import math

T = 2471
K1 = 1
K2 = 3

def get_g_(revsys, sys):
    return round(revsys / sys, 2)

def common_(parameter, K):
    print('Common', parameter)
    q_revsystem = q_system / math.factorial(K + 1)
    p_revsystem = 1 - q_revsystem
    t_revsystem = round((-1) * T / math.log(p_revsystem))
    print("Preversed_system = ", p_revsystem)
    print("Qreversed_system = ", q_revsystem)
    print("Treversed_system = ", t_revsystem)

    g_q = get_g_(q_revsystem, q_system)
    g_p = get_g_(p_revsystem, p_system)
    g_t = get_g_(t_revsystem, t_system)
    print("G_q = ", g_q)
    print("G_p = ", g_p)
    print("G_t = ", g_t)


def distribute_(parameter, K):
    newP = []
    newQ = []
    print('Distribute', parameter)
    for i in range(len(lab2.P)):
        newP.append(1 - math.pow(1 - lab2.P[i], K + 1))
        newQ.append(1 - newP[i])
    lab2.P = newP
    p_revsystem = lab2.find_P_sys()
    q_revsystem = 1 - p_revsystem
    t_revsystem = round((-1) * T / math.log(p_revsystem))
    print("Preversed_system = ", p_revsystem)
    print("Qreversed_system = ", q_revsystem)
    print("Treversed_system = ", t_revsystem)

    g_q = get_g_(q_revsystem, q_system)
    g_p = get_g_(p_revsystem, p_system)
    g_t = get_g_(t_revsystem, t_system)
    print("G_q = ", g_q)
    print("G_p = ", g_p)
    print("G_t = ", g_t)

if __name__ == '__main__':
    p_system = lab2.Ptndv
    q_system = 1 - p_system
    t_system = round((-1) * T / math.log(p_system))
    print("Psystem: ", p_system)
    print("Qsystem: ", q_system)
    print("Tsystem: ", t_system)

    print("*" * 40)
    common_(parameter='unload', K=K1)
    print("*" * 40)
    distribute_(parameter='load', K=K2)
