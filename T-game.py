from mode import mode
import createplayers as cp

players_name=cp.create_player(15)
players=cp.mould_player(players_name)

condition = {'t_t': (2, 2), 't_f': (-1, 3), 'f_t': (3, -1), 'f_f': (0, 0)}#4种不同的出拳状况以及得到的金钱，t为合作，f为欺骗
def oncegame(a,b):
    p_1=mode(a['t'])
    p_2=mode(b['t'])
    a_now_mode=p_1.f_mode()#获取本次出拳状况
    b_now_mode=p_2.f_mode()
    a_path=''
    b_path=''
    for i in range(1,11):
        bout=i
        a_path+=a_now_mode#记录本次出拳状况，
        b_path+=b_now_mode
        a['m']+=condition[str(a_now_mode)+'_'+str(b_now_mode)][0]#根据出拳形式分配金钱
        b['m']+=condition[str(a_now_mode)+'_'+str(b_now_mode)][1]
        a_now_mode=p_1.next_mode(bout,b_path)#根据对手的出钱状况判断下一次出拳状况
        b_now_mode=p_2.next_mode(bout,a_path)
    print(a_path,b_path)


oncegame(players[players_name[0]],players[players_name[2]])
print (players[players_name[0]],players[players_name[2]])
