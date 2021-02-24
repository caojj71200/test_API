# @Time : 2021/2/24 10:59
# @Author:曹晶晶
#　＠File : Check.py
import  pytest_check as check
def equal(real,expect,keys):
    '''
    :param real: 实际结果,字典格式
    :param expect: 预期结果，字典格式
    检查俩字典中key对应的value是否一致
    Check.equal(r.json,fail_data['expect'],'code,status,msg')
    不推荐直接判等
    1.结果中有一些不关键的信息，后面有变化时，会导致脚本执行不通过
    2.结构中有时间戳这类变化的信息，每次校验的结果不同，需要变更数据，比如查询所有用户中包含时间戳
    3.结构可能很长，顺序发生变化，不方便维护，比如查询所有用户，数量10w
    :param keys: 对比关键字
    :return:
    '''
    ks=keys.split(',') # 切割字符串
    for k in ks:
        r = str(real.get(k)) # 根据k取到value
        e = str(expect.get(k)) # 根据k取预期结果中的value，并转换为字符串
        try:
            check.equal(r,e)
            print(f"检验{k}成功")
        except Exception as e:
            print(f"校验{k}失败，出现异常{e}")
