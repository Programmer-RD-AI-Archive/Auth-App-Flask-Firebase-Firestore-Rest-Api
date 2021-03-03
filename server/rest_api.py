from server import *
from server.db.auth import *


def sign_in_api(info):
    try:
        si = Sign_In(
            user_name_or_email=info["User Name or Email"], password=info["Password"]
        )
        result = si.check()
        print(f"Sign In Result : {result}")
        return result
    except:
        return [False, "An Error Occured ! "]


def sign_up_api(info):
    try:
        su = Sign_Up(
            email=info["Email"], password=info["Password"], user_name=info["User Name"]
        )
        result = su.add_to_db()
        print(f"Sign Up Result : {result}")
        return result
    except:
        return [False, "An Error Occured ! "]


def send_email_api(info):
    try:
        result = send_mail(
            to_email=info["To Email"], subject=info["Subject"], body=info["Body"]
        )
        print(f"Send Email Result : {result}")
        return result
    except:
        return [False, "An Error Occured ! "]


sign_up_api_info = reqparse.RequestParser()
sign_up_api_info.add_argument(name="User Name", required=True, type=str)
sign_up_api_info.add_argument(name="Password", required=True, type=str)
sign_up_api_info.add_argument(name="Email", required=True, type=str)


class Sign_Up_Api(Resource):
    def get(self):
        try:
            if "User Name" in session and "Password" in session:
                return redirect("/Sign/In")
            info = dict(request.headers)
            add_info(info=info)
            info = sign_up_api_info.parse_args()
            result = sign_up_api(info=info)
            if result[0]:
                session["User Name"] = info["User Name"]
                session["Password"] = info["Password"]
                return redirect("/Sign/In")
            return {"result": result}
        except:
            return {"result": [False, "An error occured ! "]}

    def post(self):
        try:
            if "User Name" in session and "Password" in session:
                return redirect("/Sign/In")
            info = dict(request.headers)
            add_info(info=info)
            info = sign_up_api_info.parse_args()
            result = sign_up_api(info=info)
            if result[0]:
                session["User Name"] = info["User Name"]
                session["Password"] = info["Password"]
                return redirect("/Sign/In")
            return {"result": result}
        except:
            return {"result": [False, "An error occured ! "]}


sign_in_api_info = reqparse.RequestParser()
sign_in_api_info.add_argument(name="User Name or Email", required=True, type=str)
sign_in_api_info.add_argument(name="Password", required=True, type=str)


class Sign_In_Api(Resource):
    def get(self):
        try:
            info = dict(request.headers)
            add_info(info=info)
            if "User Name" in session and "Password" in session:
                result = sign_in_api(
                    info={
                        "User Name or Email": session["User Name"],
                        "Password": session["Password"],
                    }
                )
                session.pop("User Name", None)
                session.pop("Password", None)
                if result[0]:
                    session["Auth"] = True
                return {"result": result}
            info = sign_in_api_info.parse_args()
            result = sign_in_api(info=info)
            if result[0]:
                session["Auth"] = True
            return {"result": result}
        except:
            return {"result": [False, "An error occured ! "]}

    def post(self):
        try:
            info = dict(request.headers)
            add_info(info=info)
            if "User Name" in session and "Password" in session:
                result = sign_in_api(
                    info={
                        "User Name or Email": session["User Name"],
                        "Password": session["Password"],
                    }
                )
                session.pop("User Name", None)
                session.pop("Password", None)
                if result[0]:
                    session["Auth"] = True
                return {"result": result}
            info = sign_in_api_info.parse_args()
            result = sign_in_api(info=info)
            if result[0]:
                session["Auth"] = True
            return {"result": result}
        except:
            return {"result": [False, "An error occured ! "]}


send_email_api_info = reqparse.RequestParser()
send_email_api_info.add_argument(name="To Email", required=True, type=str)
send_email_api_info.add_argument(name="Subject", required=True, type=str)
send_email_api_info.add_argument(name="Body", required=True, type=str)


class Send_Email_Api(Resource):
    def get(self):
        try:
            info = dict(request.headers)
            add_info(info=info)
            info = send_email_api_info.parse_args()
            result = send_email_api(info=info)
            return {"result": result}
        except:
            return {"result": [False, "An error occured ! "]}

    def post(self):
        try:
            info = dict(request.headers)
            add_info(info=info)
            info = send_email_api_info.parse_args()
            result = send_email_api(info=info)
            return {"result": result}
        except:
            return {"result": [False, "An error occured ! "]}


class Help(Resource):
    def get(self):
        try:
            info = dict(request.headers)
            add_info(info=info)
            return {
                "result": "/Sign/Up => parms = {'User Name':'Your User Name','Password':'Your Password','Email':'Your Email'} \n /Sign/In => parms = {'User Name or Email':'Your User Name or Email','Password':'Your Password'} \n /Send/Email(s) => First you need to sign in then you can send a get request to the /Send/Email(s) | parmas = {'To Email':'To Email','Subject','Subject':'Subject of the Email','Body':'Body of the Email'} \n if you have any problem please send a email to go2ranuga@gmail.com \n /Log/Out to Log out \n Thank you \n Requests Accepted == 'GET' and 'POST' requests"
            }
        except:
            return ["An error occured ! "]

    def post(self):
        try:
            info = dict(request.headers)
            add_info(info=info)
            return {
                "result": "/Sign/Up => parms = {'User Name':'Your User Name','Password':'Your Password','Email':'Your Email'} \n /Sign/In => parms = {'User Name or Email':'Your User Name or Email','Password':'Your Password'} \n /Send/Email(s) => First you need to sign in then you can send a get request to the /Send/Email(s) | parmas = {'To Email':'To Email','Subject','Subject':'Subject of the Email','Body':'Body of the Email'} \n if you have any problem please send a email to go2ranuga@gmail.com \n /Log/Out to Log out \n Thank you \n Requests Accepted == 'GET' and 'POST' requests"
            }
        except:
            return ["An error occured ! "]

api.add_resource(Help, "/")
api.add_resource(Sign_In_Api, "/Sign/In")
api.add_resource(Sign_Up_Api, "/Sign/Up")
api.add_resource(Send_Email_Api, "/Send/Email(s)")
