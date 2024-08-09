import re

def reg_search(text, regex_list):
    result = []
    for regex_dict in regex_list:
        match_dict = {}
        for key, pattern in regex_dict.items():
            if key == '标的证券':
                match = re.search(r'股票代码：(\d{6}\.\w{2})', text)
                if match:
                    match_dict[key] = match.group(1)
            elif key == '换股期限':
                match = re.findall(r'(\d{4} 年 \d{1,2} 月 \d{1,2} 日)', text)
                if match:
                    match_dict[key] = [m.replace(' ', '').replace('年', '-').replace('月', '-').replace('日', '') for m in match]
        if match_dict:
            result.append(match_dict)
    return result

# 示例测试
text = '''
标的证券：本期发行的证券为可交换为发行人所持中国长江电力股份
有限公司股票（股票代码：600900.SH，股票简称：长江电力）的可交换公司债券。
换股期限：本期可交换公司债券换股期限自可交换公司债券发行结束
之日满 12 个月后的第一个交易日起至可交换债券到期日止，即 2023 年 6 月 2
日至 2027 年 6 月 1 日止。
'''

regex_list = [{
    '标的证券': '*自定义*',
    '换股期限': '*自定义*'
}]

result = reg_search(text, regex_list)
print(result)
