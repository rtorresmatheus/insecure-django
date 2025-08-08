
from django.shortcuts import render, redirect
import traceback
import json
from base64 import b64encode, b64decode
from django.core import signing
import logging

logger = logging.getLogger(__name__)



def common_home(request):
    return render(request, 'common-home.html')


def index(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")


        user = {"first_name": first_name, "last_name": last_name}
        response = redirect('/xploitpickl/dashboard')
        # Serializa em JSON e assina o valor
        user_json = json.dumps(user)
        signed_user = signing.dumps(user_json)
        response.set_cookie('user', signed_user)
        return response

    return render(request, 'index.html')


def dashboard(request):
    try:
        if request.COOKIES.get('user'):
            signed_user = request.COOKIES.get('user')
            try:
                user_json = signing.loads(signed_user)
                user = json.loads(user_json)
            except Exception:
                logger.error("Cookie de usuário inválido ou adulterado")
                return redirect("/")
            context = {"app_user": user}
            return render(request, 'dashboard.html', context)
        else:
            return redirect("/")
    except KeyError:
        logger.error("Key error")
        return redirect("/")

    except ValueError:
        logger.error("Val error")
        logger.error(traceback.format_exc())
        return redirect("/")

    except Exception as e:
        logger.error(f"{str(e)}\n{traceback.format_exc()}")
        return redirect("/")
