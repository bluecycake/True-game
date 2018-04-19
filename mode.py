class mode():
    def __init__(self,p_type):
        '''获取角色的性格'''
        self.p_type=p_type

    def f_mode(self):
        '''获取角色第一轮的决策'''
        if self.p_type=='echo':
            first_mode='t'
        if self.p_type=='pink':
            first_mode='t'
        if self.p_type=='faker':
            first_mode='f'
        if self.p_type=='iron':
            first_mode='t'
        if self.p_type=='spy':
            first_mode='t'
        return first_mode


    def next_mode(self,bout,rival_path):
        '''获取角色下轮的决策'''
        if self.p_type=='echo':#复读机性格，本轮决策为上轮对手的决策
            next_mode=rival_path[bout-1]
        if self.p_type=='pink':#小粉红性格，永远合作
            next_mode='t'
        if self.p_type=='faker':#老油条性格，永远欺骗
            next_mode='f'
        if self.p_type=='iron':#老铁性格，若对手合作，则一直合作，若对手欺骗，则永远不合作
            if 'f' in rival_path:
                next_mode='f'
            else:
                next_mode='t'
        if self.p_type=='spy':#福尔摩斯，先合作欺骗合作合作，如果对手有欺骗，则变成复读机，如果对手不欺骗，就变成老油条
            if bout==1:
                next_mode='f'
            elif bout==2 or bout==3:
                next_mode='t'
            elif 'f' not in rival_path[0:4]:
                next_mode='f'
            else:
                next_mode=rival_path[bout-1]
        return next_mode
