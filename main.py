from pyscript import document, display
from js import localStorage
import random
import json


# TEAM ASSIGNMENT SECTION

teams = {
    "Green Hornets": "https://www.pngkit.com/png/full/272-2723135_green-hornets-green-hornets-logo.png",
    "Blue Bears": "https://i.pinimg.com/1200x/99/40/c3/9940c3a4e6ad5602f8cc278766ae2b5f.jpg",
    "Yellow Tigers": "https://i.pinimg.com/736x/e1/f8/46/e1f8468b389002c1a0410989a7709a11.jpg",
    "Red Bulldogs": "https://i.pinimg.com/1200x/4a/3f/95/4a3f9536e803edc15cdae53682d6d3a3.jpg"
}


# CREATE ACCOUNT FUNCTION

def create_account(event=None):
    output = document.getElementById("output")
    output.innerHTML = ""

    username = document.getElementById('username').value.strip()
    password = document.getElementById('password').value

    if len(username) < 7:
        output.innerHTML = "❌ Username must be at least 7 characters."
        return

    if len(password) < 10:
        remaining = 10 - len(password)
        output.innerHTML = f"❌ Password must be at least 10 characters. Add {remaining} more."
        return

    # Save username to localStorage
    players_json = localStorage.getItem("players")
    if players_json:
        players = json.loads(players_json)
    else:
        players = []

    players.append(username)
    localStorage.setItem("players", json.dumps(players))

    output.innerHTML = "✅ Account Created Successfully!"


# SEATWORK TEAM ASSIGNMENT

def assign_team(event=None):
    reg = document.querySelector('input[name="registration"]:checked')
    med = document.querySelector('input[name="medical"]:checked')
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    output = document.getElementById("output2")

    if not reg or not med or grade == "Enter Grade" or section == "Enter Section":
        output.innerHTML = "⚠️ Please complete all fields!"
        return

    if reg.value == "yes" and med.value == "yes":
        team = random.choice(list(teams.keys()))
        image_url = teams[team]

        output.innerHTML = f"""
            🎉 Congratulations! You are part of the {team}! <br>
            <img src='{image_url}' alt='{team}' style='width:200px; margin-top:10px;'>
        """
    else:
        output.innerHTML = "⚠️ You must finish registration and have medical clearance first."



# PLAYERS CHECKER

def check_players(event=None):
    players_json = localStorage.getItem("players")

    if players_json:
        players = json.loads(players_json)
        output_text = "<h3>Players Signed Up:</h3><ol>"
        for p in players:
            output_text += f"<li>{p}</li>"
        output_text += "</ol>"
    else:
        output_text = "<p>No players have signed up yet.</p>"

    display(output_text, target="output3")
