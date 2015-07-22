# -*- coding: utf8 -*-
from gluon.tools import Service
from datetime import datetime


service = Service(globals())

@service.soap('getKeyPointPerson',returns={'result':str,'code':int},
                            args={'auth':str,'person_data' : {'full_name':str, 'email':str, 'cellphone':str,
                                                          'birth_date':str, 'city_person':int, 'keypoints': str}})
def getKeyPointPerson(auth,person_data):
    #person_data['birth_date'] = datetime.strptime(person_data['birth_date'], "%d/%m/%Y").strftime("%m-%d-%Y")
    if auth == '' or auth == None or person_data == None or person_data == '':
        return dict(result='NOT_VALID',code=0)
    else:
        #ret = db.executesql("""SELECT company.id AS company_id, auth_user.id AS user_id
                                #FROM auth_user, company
                                #WHERE last_name='{0}' AND 
                                #      auth_user.actived_user= 'T' AND 
                                #      first_name='webservice' LIMIT 1
                               #""".format(auth),as_dict=True)
        id_person = db.executesql("""INSERT INTO person (created, last_update, full_name, email, cellphone, birth_date, keypoints)
                                        VALUES ('{0}', '{0}', '{1}', '{2}', '{3}', '{4}', '{5}');
                                        """.format(datetime.now(),person_data['full_name'],person_data['email'],
                                                   person_data['cellphone'],person_data['birth_date'],
                                                   person_data['keypoints']))
        return dict(result='OK',code=id_person)
    #return dict(result='NOT_VALID',code=0)

def call():
    return service()

def test_soap_sub():
    from gluon.contrib.pysimplesoap.client import SoapClient, SoapFault
    client = SoapClient(wsdl="http://127.0.0.1:8000/TG/webservice/call/soap?WSDL")   


    response = client.getKeyPointPerson(auth='0DDEE29FAA57CF9DBEE480986E7B0686',
                                   person_data={'full_name':'Samara Cardoso dos Santos', 'email':'samara.cardoso@urbemobile.com.br', 
                                                'cellphone':'12988211378', 'birth_date':'03-27-1994',
                                                'keypoints':'5809500732421875'})
    try:
        result = response
    except SoapFault as e:
        result = e
    return dict(xml_request=client.xml_request, 
                xml_response=client.xml_response,
                result=result)