# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations
from samba.dcerpc.winreg import KeySecurityAttribute
from gluon.tools import Service
from datetime import datetime
from pip._vendor.requests.sessions import session
#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################



def index():
    return dict(key=session.key)

def insert_person():
    if request.args(0)=='submit':
            print(request.vars)  
            id_person = db.executesql(""" INSERT INTO person(created, last_update, full_name, email, cellphone, birth_date, keypoints, last_user)
                                      VALUES ('{0}','{0}', '{1}','{2}','{3}','{4}','{5}',{6}) RETURNING id;
                                    """.format(datetime.now(),request.vars.full_name,request.vars.email,
                                               request.vars.cellphone,request.vars.birth_date,
                                               request.vars.keypoints,1))
            print(id_person)
    return dict()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)



service = Service(globals())

@service.soap('getKeyPointPerson',returns={'result':str,'code':int},
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
    #        id_person = db.executesql(""" INSERT INTO person(created, last_update, full_name, email, cellphone, birth_date, keypoints, last_user)
    #                                      VALUES ('{0}','{0}', '{1}','{2}','{3}','{4}','{5}',{6}) RETURNING id;
    #                                    """.format(datetime.now(),person_data['full_name'],person_data['email'],
    #                                               person_data['cellphone'],person_data['birth_date'],
    #                                               person_data['keypoints'],ret[0]['user_id']))
    #        if len(id_person) >= 1:
    #            return dict(result='OK',code=1)
    #        else:
    #            return dict(result='NOT_VALID',code=0)
    
    session.key = person_data['keypoints']
    #print(person_data['keypoints'])
    return dict(result='OK',code=1)
    
    
            
    #

def call():
    return service()








