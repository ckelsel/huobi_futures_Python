# -*— coding:utf-8 -*-

"""
Huobi Swap Demo.

Author: QiaoXiaofeng
Date:   2020/1/10
Email:  andyjoe318@gmail.com
"""


import sys
import pandas as pd
import talib as ta

def initialize():
    from strategy import MyStrategy
    MyStrategy()


def main():
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
    else:
        config_file = None

    from alpha.quant import quant
    quant.initialize(config_file)
    initialize()
    quant.start()

from datetime import datetime, timedelta

if __name__ == '__main__':
    main()
    # now=datetime.now()
    # ts1 = int(datetime.timestamp(now) * 1000)
    # print(ts1)

    # one_day=now-timedelta(days=1)
    # ts1 = int(datetime.timestamp(one_day) * 1000)
    # print(ts1)
    # df=pd.DataFrame(columns=['date', 'close'])
    # df.set_index('date', inplace=True)
    # symbol = 'BTC_USDT'

    # p = {symbol:df}

    # symbol = ["aa", "bb", symbol]
    # for s in symbol:
    #     p[s] = df

    # print(p)
