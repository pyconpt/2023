from datetime import datetime
from os import walk

from django.shortcuts import render
from django.views import View

from config.settings.base import APPS_DIR
from pycon_portugal_2023.site.events import W1, W2, A, events


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


class ScheduleView(View):
    def get(self, request, *args, **kwargs):
        day = kwargs.get("day", 7)
        room = kwargs.get("room", None)
        if day not in range(7, 10):
            return render(request, "404.html")

        # Make a copy so we don't mutate the original
        selected_events = events.copy()
        selected_events = [event for event in selected_events if event["day"] == day]

        if room:
            if day != 9:
                return render(request, "404.html")

        if room == "1":
            room = W1
        elif room == "2":
            room = W2
        elif not room:
            room = ""
        elif room.lower() == "auditorium":
            room = A

        selected_events = [
            event for event in selected_events if room == "" or room == event["room"]
        ]

        # Transform start_time to datetime
        for event in selected_events:
            if type(event["start_time"]) == str:
                event["start_time"] = datetime.strptime(event["start_time"], "%H:%M")

        # Sort by start_time
        selected_events = sorted(selected_events, key=lambda k: k["start_time"])

        context = {
            "day": f"September {day}",
            "room": room,
            "events": selected_events,
        }

        return render(request, "pages/schedule/schedule_content.html", context)
