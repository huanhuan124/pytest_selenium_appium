# 预生产环境登录
from datetime import datetime

import requests
import json


class login_demo:
    def attendance(self):
        data = {
            "employeeCode": "50000324",
            'beginDate': '2021-01-01',
            'endDate': '2021-12-31'

        }
        # http://api.sap.zuche.com/ucarsap/getCheckInfoList?employeeCode=50001204&beginDate=2021-01-01&endDate=2022-12-30
        # re = requests.post("http://caradmintest.zuche.com/system/login.do_", data=data)
        re = requests.post("http://api.sap.zuche.com/ucarsap/getCheckInfoList",data=data)
        print("考勤接口返回的结果：")
        print(re.text)
        # print(type(re.text))
        text = json.loads(re.text)
        # print(type(text))

        datas = text['data']
        # print(datas)
        # print(len(datas))
        checkin_count = 0
        duration_count = 0
        work_extra = '00:00:00'
        total_extra = (datetime.strptime('00:00:00', '%H:%M:%S') - datetime.strptime('00:00:00', '%H:%M:%S'))
        for data in datas:
            # print(data)
            checkDate = data['checkDate']
            checkinTime = data['checkinTime']
            duration = data ['duration']

            print(f"{data['checkDate']}早上打卡时间：{data['checkinTime']}")
            # if data['checkinTime'] >= '09:31:00' and data['checkDate'] > '2021-06-28':
            # if data['checkinTime'] >= '09:35:00' and data['checkDate'] > '2021-01-07':
            if checkinTime >= '09:31:00' :
                checkin_count = checkin_count +1
            print(f"早上迟到打卡天数：{checkin_count}天")

            if duration >= '09:00:00':
                duration_count = duration_count + 1
                # 将 'str' 时间通过格式化模式转化为 'datetime.datetime' 时间戳, 然后再进行比较
                print(f'当天上班持续时间：{duration}')
                # print(datetime.strptime('09:00:00','%H:%M:%S'))
                # print(datetime.strptime(duration,'%H:%M:%S'))
                difference = (datetime.strptime(duration,'%H:%M:%S') - datetime.strptime('09:00:00','%H:%M:%S'))
                print(f'加班时间：{difference}')
                total_extra = difference + total_extra
                # print(f'加班的时候加班分钟数{total_extra}')

            print(f'全年加班总分钟数：{total_extra}')
            print(f"上班持续时间超过9小时天数：{duration_count}天")


        return checkin_count



'''
》=9:31
曾欢 50001204：76  上班持续时间超过10小时：71   全年加班总分钟数：7 days, 17:10:10
李良云 10002112：180  上班持续时间超过10小时：55   全年加班总分钟数：6 days, 7:11:15
2021-6-29到2021-12-31
殷晓丹 10002715：125   上班持续时间超过10小时：13     全年加班总分钟数：1 day, 13:34:32
贾丹 10006037：46  上班持续时间超过10小时：39    全年加班总分钟数：6 days, 9:37:22
王春飞 50000033：42  上班持续时间超过10小时：65   全年加班总分钟数：7 days, 3:19:44
张鸣朔 10006048：30  上班持续时间超过10小时：65   全年加班总分钟数：7 days, 12:57:04
李蛟 10006025 ：92  上班持续时间超过10小时：39   全年加班总分钟数：5 days, 14:36:06
李润琪 50000324 ：19  上班持续时间超过10小时：47    全年加班总分钟数：6 days, 19:30:25

》=9:35
曾欢 50001204：28
李良云10002112 ：159
2021-6-29到2021-12-31
殷晓丹 10002715：120
贾丹 10006037：14
王春飞 50000033：28
张鸣朔 10006048 ：17
李蛟 10006025 ：72
李润琪 50000324 ：9
'''
login = login_demo()
work_attendance = login.attendance()



