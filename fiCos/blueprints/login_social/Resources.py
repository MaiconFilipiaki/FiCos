from flask import current_app, redirect, url_for
from flask_dance.contrib.facebook import facebook


@current_app.route('/facebook')
def login_social_by_facebook():
    if not facebook.authorized:
        return redirect(url_for("facebook.login"))
    resp = facebook.get("https://graph.facebook.com/me?fields=id,name,email")
    assert resp.ok, resp.text
    return "You are {name} on Facebook".format(name=resp.json()["name"])
