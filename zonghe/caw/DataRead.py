# @Time : 2021/2/23 10:24
# @Author:曹晶晶
# 　＠File : DataRead.py

'''读取数据的文件'''
import configparser
import os

# 绝对路径
import yaml


def get_project_path():
    '''
    获取工作路径
    :return:D:\ApiAutoTest\zonghe\test_env\env.ini
    '''

    # 获取当前文件路径realpath
    file_path = os.path.realpath(__file__)
    # print("当前文件路径：", file_path)

    # 通过当前文件获得所在的目录，
    # 当前文件所在的目录
    dir_path = os.path.dirname(file_path)
    # print("当前文件目录", dir_path)

    # 通过当前目录所在的位置，所得父目录，
    # 再上一级目录,返回当前目录的上一级目录
    dir_path = os.path.dirname(dir_path)
    # print(dir_path)

    # 最后拼\\
    return dir_path + "\\"


def read_ini(file_path, key):
    '''
    :param file_path: 配置文件的路径
    :param key:配置文件中的key，比如URL
    :return:返回key对应的value
    '''
    # python中的内置对象 configparser 是用来读取配置文件
    config = configparser.ConfigParser()  # 初始化
    file_path = get_project_path() + file_path
    config.read(file_path)
    # env对应文件ini中的[env]
    value = config.get("env", key)
    return value


# 读取yaml文件: 普通文件读取方式 with open
# 内容加载:yaml.load(file_content,Loader=yaml.FullLoader)
def read_yaml(file_path):
    '''
    :param file_path: yaml文件路径
    :return: 文件的内容
    '''
    file_path = get_project_path() + file_path
    # 读取
    with open(file_path, "r", encoding="utf8") as file:
        file_content = file.read()
        content = yaml.load(file_content, Loader=yaml.FullLoader)
        return content


if __name__ == '__main__':
    value = read_ini(r"test_env\env.ini", "url")
    print(type(value))
    print(value)
    file_content = read_yaml(r"test_data\register_fail.yaml")
    print(file_content)
    print(file_content[0]['expect'])
