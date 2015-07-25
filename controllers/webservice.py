# -*- coding: utf8 -*-
from gluon.tools import Service
from datetime import datetime


service = Service(globals())

@service.soap('getKeyPointPerson',returns={'result':str},
                            args={'auth':str,'person_data' : {'full_name':str, 'email':str, 'cellphone':str,
                                                          'birth_date':str,'keypoints': str}})
def getKeyPointPerson(auth,person_data):
    print('passou aqui')
    #person_data['birth_date'] = datetime.strptime(person_data['birth_date'], "%d/%m/%Y").strftime("%m-%d-%Y")
    #if auth == '' or auth == None or person_data == None or person_data == '':
    #    return dict(result='NOT_VALID',code=0)
    #else:
    #    ret = db.executesql("""SELECT auth_user.id AS user_id
    #                            FROM auth_user, company
    #                            WHERE last_name='{0}' AND 
    #                                  auth_user.actived_user= 'T' AND 
    #                                  first_name='webservice' LIMIT 1
    #                           """.format(auth),as_dict=True)
    #    if len(ret) <= 0:
    #        return dict(result='ERRO',code=0)
    #    else:
    #        id_person = db.executesql("""INSERT INTO person (created, last_update, last_user, full_name, email, cellphone, birth_date, keypoints)
    #                                    VALUES ('{0}', '{0}', {1}, '{2}', '{3}', '{4}', '{5}','{5}')RETURNING id;;
    #                                    """.format(datetime.now(),ret[0]['user_id'],person_data['full_name'],person_data['email'],
    #                                               person_data['cellphone'],person_data['birth_date'],
    #                                               person_data['keypoints']))
    
    print(person_data['keypoints'])
    
    
    return dict(result=person_data['keypoints'])
    #return dict(result='NOT_VALID',code=0)

def call():
    return service()



    
