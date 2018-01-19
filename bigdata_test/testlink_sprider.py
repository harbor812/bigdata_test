# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 16:22:40 2017

@author: Brianzhu
"""

import testlink
import db_mysql,datetime
url='http://192.168.120.80/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
key='84539af99306e470cb2b45117e4a8a17'

tlc=testlink.TestlinkAPIClient(url,key)


def get_information_test_project():
    print("Number of Projects      in TestLink: %s " % tlc.countProjects())
    print("Number of Platforms  (in TestPlans): %s " % tlc.countPlatforms())
    print("Number of Builds                   : %s " % tlc.countBuilds())
    print("Number of TestPlans                : %s " % tlc.countTestPlans())
    print("Number of TestSuites               : %s " % tlc.countTestSuites())
    print("Number of TestCases (in TestSuites): %s " % tlc.countTestCasesTS())
    print("Number of TestCases (in TestPlans) : %s " % tlc.countTestCasesTP())
    tlc.listProjects()
    
            
def get_test_case(test_case_id,date,nm1,db,typename):
    print "######################"
    try:
        test_case = tlc.getTestCase(None, testcaseexternalid=test_case_id)
        print "#######################"
        print 'test_case:',test_case_id
        for i in test_case:
            nm=i.get("name")
            ct=i.get("creation_ts")
            mt=i.get("modification_ts")
            afn=i.get("author_first_name")
            aln=i.get("author_last_name")
            ufn=i.get("updater_first_name")
            uln=i.get("updater_last_name")
            caseid=i.get("full_tc_external_id")
            create_name=''
            updater_name=''
            if aln:
                create_name=aln.encode('utf-8')+afn.encode('utf-8')
            if uln:
                updater_name=uln.encode('utf-8')+ufn.encode('utf-8')
            
    #        print "测试用例",caseid,":",nm.encode('utf-8'),ct,create_name
    #        print mt,updater_name
    #        print "测试用例名字：",nm,nm1  UnicodeDecodeError
            print "caseid"
            print caseid
            print "ct"
            print ct
            print "mt"
            print mt
            print "测试用例名字：",nm
            if caseid:                
                print "caseid 不为NONE"
                if ct > date:
                   
                   cn=db.testcase_sel(caseid,date)
                   if cn[0] == 0:
                       db.testcase_save(caseid,nm.encode('utf-8'),create_name,updater_name,ct,mt,typename)                  
                       print 'ct:'+ct+create_name
                       print caseid 
                       return "ture"
                elif  mt > date:
                   
                   cn=db.testcase_sel(caseid,date)
                   if cn[0] > 0:
                       db.testcase_save(caseid,nm.encode('utf-8'),updater_name,mt)   
                       print 'MT:'+mt+updater_name
                       print caseid 
                   return "ture"
                else:
                   print "时间不在范围内",caseid
                   return "ture"

    except UnicodeDecodeError,e:
             print e
             return "false"
             
#        print "序列", "执行步骤", "预期结果"
#        print 
#        for m in i.get("steps"):
#            sn=m.get("step_number")
#            ac=m.get("actions")
#            er=m.get("expected_results")
#            un=m.get("updater_first_name")
#            nm=m.get("name")
#            print sn,ac.encode('utf-8'),er.encode('utf-8')
#        print i

def get_test_suite():
    projects = tlc.getProjects()
    top_suites = tlc.getFirstLevelTestSuitesForTestProject(projects[0]["id"])
    for suite in top_suites:
        eid=suite["id"]
        name=suite["name"]
        print eid,name.encode('utf-8')

#get_test_case("test-1213190840")
#get_test_suite()
#get_information_test_project()

if __name__ == '__main__':
   date = datetime.date.today()
   date = str(date)
#   print date
   date='2017-12-01'
   t='true'
   i=1212100000
   db=db_mysql.dbmysql()
   #测试产品：测试
   while t != 'false': 
       typename="小葫芦"
       caseid='小葫芦-'+str(i)
       t=get_test_case(caseid,date,t,db,typename)
       i=i+1
     
       