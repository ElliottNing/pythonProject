import time
import baostock as bs
import pandas as pd


def download_data(date):
    bs.login()

    # 获取指定日期的指数、股票数据
    stock_rs = bs.query_all_stock(date)
    stock_df = stock_rs.get_data()
    data_df = pd.DataFrame()
    curr = time.time() * 1000
    print('\033[31m当前时间：', curr)

    for code in stock_df["code"]:
        print("Downloading :" + code)
        k_rs = bs.query_history_k_data_plus(code, "date,code,open,high,low,close", date, date)
        data_df = data_df.append(k_rs.get_data())
    print('\033[31m结束时间：', time.time() * 1000 - curr, "ms")
    bs.logout()
    data_df.to_csv("D:\\demo_assignDayData.csv", encoding="gbk", index=False)
    print(data_df)


if __name__ == '__main__':
    # 获取指定日期全部股票的日K线数据
    download_data("2021-09-27")
