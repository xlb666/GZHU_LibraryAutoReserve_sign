infos = [
    {
        'sno': '32106100110',         # 学号
        'pwd': 'Xlb021208.',         # 密码
        'devName': '103-020',   # 预约的座位号（不足3位数的要补零）
        'name': 'GG',        # 随便起个名字
        'periods': (            # 预约时间段（每段时间不能超过4小时）
            ('12:00:00', '16:00:00'),
            ('16:15:00', '20:15:00')
        ),
        'pushplus': '653749a946d142e581b00bc9a49469b8',         # pushplus 的 token（用于推送消息到微信）
    },

    # 如果只是一个人预约座位，不需要帮别人预约签到，则可把下面三个字典注释/删除
    {
        'sno': '32106100110',  # 学号
        'pwd': 'Xlb021208.',  # 密码
        'devName': '103-021',  # 预约的座位号（不足3位数的要补零）
        'name': 'GG',  # 随便起个名字
        'periods': (  # 预约时间段（每段时间不能超过4小时）
            ('12:00:00', '16:00:00'),
            ('16:15:00', '20:15:00')
        ),
        'pushplus': '653749a946d142e581b00bc9a49469b8',  # pushplus 的 token（用于推送消息到微信）
    },
    {
        'sno': '32106100110',  # 学号
        'pwd': 'Xlb021208.',  # 密码
        'devName': '103-011',  # 预约的座位号（不足3位数的要补零）
        'name': 'GG',  # 随便起个名字
        'periods': (  # 预约时间段（每段时间不能超过4小时）
            ('12:00:00', '16:00:00'),
            ('16:15:00', '20:15:00')
        ),
        'pushplus': '653749a946d142e581b00bc9a49469b8',  # pushplus 的 token（用于推送消息到微信）
    },
    {
        'sno': '32106100110',  # 学号
        'pwd': 'Xlb021208.',  # 密码
        'devName': '103-031',  # 预约的座位号（不足3位数的要补零）
        'name': 'GG',  # 随便起个名字
        'periods': (  # 预约时间段（每段时间不能超过4小时）
            ('12:00:00', '16:00:00'),
            ('16:15:00', '20:15:00')
        ),
        'pushplus': '653749a946d142e581b00bc9a49469b8',  # pushplus 的 token（用于推送消息到微信）
    },
]
