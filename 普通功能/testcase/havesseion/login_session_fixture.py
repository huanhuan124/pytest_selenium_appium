# 预生产环境登录
import requests
import json
import pytest

# test环境创建车辆  依赖登录接口传cookie
frameNo = "JMETERCAR49529191"
engineNo = "JMETERCAR49529191"


def test_createVehicle_session(login_do_session):
    # 由于直接抓取的接口参数是java的json，包含null类型，Python不认，需要先转成字符串（使用''''''方法），然后转成Python的json

    session = login_do_session
    datapre = ''' {	"baseInfoVo": {
    		"vehicleId": "",
    		"companyId": 46,
    		"brandId": 67,
    		"vehicleSeriesId": 560,
    		"vehiclenoCityId": "",
    		"vehiclenoCityName": "",
    		"vehicleNo": "",
    		"frameNo": "frameNo",
    		"engineNo": "engineNo",
    		"engineType": "",
    		"envStandard": 3,
    		"modelId": 1221,
    		"vehicleLicensemode": "",
    		"vehicleModel300Name": "2015款 宝马5系GT(进口) 528i 领先型",
    		"color": 3,
    		"registerNo": "",
    		"useNature": 0,
    		"carUseType": 0,
    		"vehicleRemark": "",
    		"checkTime": "",
    		"ownerStatus1st": 10,
    		"ownerStatus2nd": 1001,
    		"ownerStatus3rd": "",
    		"contractNo": "llypreht001"
    	},
    	"operatingInfoVo": {
    		"shortModelId": 718,
    		"shortModelName": "长租车型（特殊）",
    		"businessType": 1,
    		"isUCar": 0,
    		"isHertz": 0,
    		"isLease": 0,
    		"onLineTime": "",
    		"lastQuitRunTime": "",
    		"handleTime": "",
    		"ucarRentType": "",
    		"oilVolume": null,
    		"batteryVolume": null,
    		"batteryPercentage": 0,
    		"oilVolumeLatticeNum": 0,
    		"orderCar": 0,
    		"cityId": 1,
    		"nowCityId": 1,
    		"nowCityName": "北京",
    		"parkCityId": 1,
    		"departmentId": 75405,
    		"nowDepartmentId": 75405,
    		"parkDeptId": 75405,
    		"runMilesInput": "100",
    		"nextInspecteTime": "",
    		"regTime": "",
    		"firstLevelStatus": 100000,
    		"selfFirstLevelStatus": 100000,
    		"nowDepartmentName": "花家地门店"
    	},
    	"assetInfoVo": {
    		"bussLineId": 1,
    		"bussLineTime": "",
    		"willBussLineId": "",
    		"willBussLineTime": "",
    		"checkResultName": "",
    		"allocationStatusName": "",
    		"isInsideScrapName": "",
    		"lastApproveSaleTime": "",
    		"firstTransferOwnershipTime": "",
    		"vehicleNoBeforeTransfer": ""
    	},
    	"financeInfoVo": {
    		"carOwnerId": 87,
    		"purchasePrice": "150000",
    		"registrationAndPettyExpenses": "",
    		"taxAmount": "",
    		"incrementTaxExpenses": "3000",
    		"monthDepreciationRate": "",
    		"originalValue": "153000",
    		"taxInvoiceDate": "",
    		"purchaseDate": "2021-12-02",
    		"remainderPrice": "",
    		"vehicleAndVesselTax": "",
    		"estimatedRemainderPrice": "",
    		"realHandlePrice": "",
    		"handlePettyExpenses": "",
    		"realSellOutPrice": "",
    		"handlePettyIncrementTax": "",
    		"invoiceNo": "2022012001"
    	},
    	"garageInfoVo": {
    		"lastTimeAttendMile": "",
    		"nextTimeAttendMile": "",
    		"vehicleFrom": ""
    	},
    	"deviceInfoVo": {
    		"gps": 0,
    		"deviceNo": "",
    		"deviceType": ""
    	},
    	"noInfoPo": {
    		"vehicleNoColor": ""
    	},
    	"colorPo": {
    		"interiorColorId": ""
    	},
    	"takeoverPo": {
    		"compulsoryInsurance": 1,
    		"needInsured": 1,
    		"insuranceBeginDate": "2022-01-01",
    		"insuranceEndDate": "2023-01-02"
    	},
    	"insurancePos": [{
    		"createTime": 1642660788023,
    		"insuranceTypeName": "第三者责任险",
    		"needAmount": 0,
    		"insuranceAmount": null
    	}, {
    		"createTime": 1642661000825,
    		"insuranceTypeName": "车辆损失险",
    		"needAmount": 1,
    		"insuranceAmount": "100"
    	}],
    	"modifyEmpName": null,
    	"createEmpName": null,
    	"createTime": null,
    	"modifyTime": null
    }
        '''
    mydata = json.loads(datapre)
    # print(mydata)
    # print(type(mydata))
    mydata["baseInfoVo"]["frameNo"] = frameNo
    mydata["baseInfoVo"]["engineNo"] = engineNo


    # 当参数是json格式的时候，需要使用json格式传参，不能使用data
    re = session.post(
        "http://**",
        json=mydata)
    print(re.text)
    assert 200 == re.status_code

# login = login_fixture()
# frameNo = "JMETERCAR49529191"
# engineNo = "JMETERCAR49529191"
#
# login.createVehicle(frameNo,engineNo)
