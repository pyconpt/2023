from datetime import datetime
from os import walk

from django.shortcuts import render
from django.views import View

from config.settings.base import APPS_DIR
from pycon_portugal_2023.site.events import events


def default_view(request, menu="home", submenu=None):
    path = APPS_DIR.__str__() + "/content/" + menu + ("/" + submenu if submenu else "")
    page = ""
    ctx = dict(menu=(menu if not submenu else submenu).capitalize().replace("_", " "))
    files = []

    for dirpath, dirname, filenames in walk(path):
        files.extend(filenames)
        break

    ctx["files"] = []
    for f in sorted(files):
        content = "%s/%s" % (path, f)
        ctx["files"].append(content)

    if menu == "home":
        page += "pages/" + menu
    elif len(files) == 0:
        page += "404"
    else:
        page += "pages/" + "default"

    return render(request, page + ".html", ctx)


WORKSHOP_1 = "Workshop I"
WORKSHOP_2 = "Workshop II"
AUDITORIUM = "Auditorium"


class ScheduleView(View):
    def get(self, request, *args, **kwargs):
        day = kwargs.get("day", 7)
        room = kwargs.get("room", None)
        if day not in range(7, 10):
            return render(request, "404.html")

        # Make a copy so we don't mutate the original
        selected_events = events.copy()
        selected_events = [event for event in events if event["day"] == day]

        if room:
            if day != 9:
                return render(request, "404.html")

        if "1" in room:
            room = WORKSHOP_1
        elif "2" in room:
            room = WORKSHOP_2
        elif room.lower() == "auditorium":
            room = AUDITORIUM

        selected_events = [
            event for event in selected_events if event["room"] in [room, ""]
        ]
        # Transform start_time to datetime
        for event in selected_events:
            if type(event["start_time"]) == str:
                event["start_time"] = datetime.strptime(event["start_time"], "%H:%M")

        context = {
            "day": f"September {day}",
            "room": room.capitalize() if room else "Auditorium",
            "events": selected_events,
        }

        return render(request, "pages/schedule/schedule_content.html", context)
