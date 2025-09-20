# import tejapi
# tejapi.ApiConfig.api_key = "QxW2e4xTUE5b5bfcin7TT9hj0"
# data = tejapi.get('TWN/2330')

# info = tejapi.ApiConfig.info()

# import sys
# print(sys.path)

# import sys
# sys.path.append(r"C:\Users\shann\AppData\Local\Programs\Python\Python313\Lib\site-packages")

# import tejapi
# print(tejapi.__version__)

# import tejapi

# tejapi.ApiConfig.api_key = "QxW2e4xTUE5b5bfcin7TT9hjFbS6nV"  # 先替換成你自己的金鑰
# data = tejapi.get('TWN/AFACTO1D', paginate=True)  # 取得台灣月股價指數資料
# print(data.head())

# import tejapi

# tejapi.ApiConfig.api_key = "QxW2e4xTUE5b5bfcin7TT9hjFbS6nV"

# # 查詢你能存取的資料表
# available_tables = tejapi.list_datatables()
# print(available_tables)0







# import tejapi
# import pandas as pd
# import numpy as np
# # api_key=QxW2e4xTUE5b5bfcin7TT9hjFbS6nV
# tejapi.ApiConfig.api_key = "QxW2e4xTUE5b5bfcin7TT9hjFbS6nV"

# data = tejapi.get('TRAIL/TAPRCD', 
#                    coid='2603', 
#                 #  mdate={'gte':'2025-02-14', 'lte':'2025-03-14'},
#                    opts={'columns':['mdate','close_d', 'volume']},
#                    chinese_column_name=True
#                   )
# tejapi.ApiConfig.ignoretz = True
# data.set_index('年月日', inplace=True)







# import tejapi
# import pandas as pd
# import numpy as np

# # 設定 API 金鑰
# tejapi.ApiConfig.api_key = "QxW2e4xTUE5b5bfcin7TT9hjFbS6nV"

# try:
#     # 嘗試取得資料
#     data = tejapi.get(
#         'TRAIL/TAPRCD',
#         coid='2330',  # 公司代碼，這裡是台積電
#         mdate={'gte': '2025-02-14', 'lte': '2025-03-14'},
#         opts={'columns': ['mdate', 'close_d', 'volume']},
#         chinese_column_name=True
#     )

#     # 顯示返回的資料
#     print("返回的資料:")
#     print(data)  # 打印資料內容，檢查是否有返回資料

#     if data.empty:
#         print("沒有資料返回。")
#     else:
#         # 設定時間區間
#         tejapi.ApiConfig.ignoretz = True

#         # 設定索引
#         data.set_index('年月日', inplace=True)
#         print("處理後的資料:")
#         print(data.head())  # 顯示處理後的資料

# except Exception as e:
#     print(f"發生錯誤: {e}")






# data = tejapi.get('TRAIL/TAPRCD', coid='2330', opts={'columns': ['mdate', 'close_d', 'volume']})
# print(data.columns)

# data['mdate'] = pd.to_datetime(data['mdate'])
# data.set_index('mdate', inplace=True)
# print(data.head())


import tejapi
import pandas as pd

tejapi.ApiConfig.api_key = "QxW2e4xTUE5b5bfcin7TT9hjFbS6nV"

data = tejapi.get('TRAIL/TAPRCD',     #三因子模型：'TWN/AFACTO1D'
                  coid='2330', 
                  mdate={'gte': '2025-02-14', 'lte': '2025-03-14'},
                  opts={'columns': ['mdate', 'close_d', 'volume']},
                  chinese_column_name=True)

tejapi.ApiConfig.ignoretz = True
data.set_index('年月日', inplace=True)

print(data)