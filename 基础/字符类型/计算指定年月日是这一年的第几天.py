"""
计算指定的年月日是这一年的第几天


设计思路
- 首先每年的天数 = 365 每个月的天数也是固定的， 但是闰年的二月份 = 29
    所以需要先判断 用户输入的年份是否是闰年
    - 闰年的判断标准为 普通闰年是4的倍数 且不能被100整出；世纪闰年:公历年份是整百数的，必须是400的倍数才是闰年
- 定义天数，分两个列表[[list1 = 非闰年],[list2 = 闰年]]
- 使用for循环遍历出 对应月份的天数 月天数 += 月天数
"""

def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


def main():
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))


if __name__ == '__main__':
    # main()

    a = 2004 % 400
    print(a)