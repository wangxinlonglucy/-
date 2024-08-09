import requests
from bs4 import BeautifulSoup
import pandas as pd

# 访问页面并获取HTML内容
url = "https://iftp.chinamoney.com.cn/english/bdInfo/"
response = requests.get(url)
response.encoding = 'utf-8'

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 寻找目标表格数据
table = soup.find('table')  # 假设页面中有且只有一个表格

# 解析表格数据
rows = table.find_all('tr')
data = []
for row in rows[1:]:  # 跳过表头
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    bond_type = cols[3]  # Bond Type
    issue_year = cols[4].split('-')[0]  # Issue Date的年份
    if bond_type == 'Treasury Bond' and issue_year == '2023':
        data.append([cols[0], cols[1], cols[2], bond_type, cols[4], cols[5]])

# 创建DataFrame并保存为CSV文件
columns = ['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating']
df = pd.DataFrame(data, columns=columns)
df.to_csv('bond_data_2023.csv', index=False, encoding='utf-8')
