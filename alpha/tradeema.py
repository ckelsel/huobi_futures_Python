# -*- coding:utf-8 -*-

import pandas as pd
from alpha.kline import Kline
from alpha.utils import logger

class TradeEMA:
    def __init__(self):
        self.calc_kline_timestamp = pd.Timestamp.now()
        self.calc_kline_firsttime = True

        self.df=pd.DataFrame(columns=['date', 'close'])
        self.df.set_index('date', inplace=True)


    def on_klines_update(self, kline: Kline):
        tt = pd.to_datetime(str(kline.timestamp),unit='ms')
        # 每隔5分钟计算一次乖离率，
        if tt.minute % 2 == 0:
            logger.info("kline update:", kline, caller=self)

            mytime=pd.Timestamp(tt.year, tt.month, tt.day, tt.hour, tt.minute)
            self.df.loc[mytime, 'close']=kline.close
            logger.info(self.df.reset_index().to_json(orient="records"))

