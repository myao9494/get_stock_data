from alpha_vantage.timeseries import TimeSeries
import datetime,time
ts = TimeSeries(key='25JBS8HQYNAQ0EIU', output_format='pandas')


def get_stock_data_1min(symbol):
    print(datetime.datetime.now())
    data, meta_data = ts.get_intraday(symbol=symbol,interval='1min')
    print(datetime.datetime.now())
    print(data)

if __name__ == "__main__":
    symbol="7974.T"
    time.sleep(60*60*3)

    i=0
    while True:
        now = datetime.datetime.now()
        if now.second==0 or now.second==30 :
            get_stock_data_1min(symbol)
            time.sleep(2)
        i += 1
        time.sleep(0.9)
        # print(i)

        if i==100000:
            break

    
    