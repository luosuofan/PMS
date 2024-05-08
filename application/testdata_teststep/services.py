from application.testdata.models import Testdata


# 根据调试数据ID查询测试步骤列表
def getTestDataTestStepList(testdataId):
    sql = 'SELECT * FROM django_testdata_teststep WHERE testdata_id=%s'
    list = Testdata.objects.raw(sql, [testdataId])
    # 实例化测试步骤列表
    testStep_list = []
    if list:
        for v in list:
            item = {
                'no': v.no,
                'name': v.name,
                'result': v.result,
            }
            # 加入数组
            testStep_list.append(item)
    # 返回结果
    return testStep_list
