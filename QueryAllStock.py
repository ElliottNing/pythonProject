import baostock as bs
import pandas as pd

# 方法说明：获取指定交易日期所有股票列表。通过API接口获取证券代码及股票交易状态信息，
# 与日K线数据同时更新。可以通过参数‘某交易日’获取数据（包括：A股、指数），数据范围同
# 接口query_history_k_data_plus()。
#
# 返回类型：pandas的DataFrame类型。
#
# 更新时间：与日K线同时更新。

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取证券信息 ####
rs = bs.query_all_stock(day="2017-06-30")
print('query_all_stock respond error_code:'+rs.error_code)
print('query_all_stock respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

#### 结果集输出到csv文件 ####
result.to_csv("D:\\all_stock.csv", encoding="gbk", index=False)
print(result)

#### 登出系统 ####
bs.logout()