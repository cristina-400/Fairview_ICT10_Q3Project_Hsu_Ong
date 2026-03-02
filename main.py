from js import document, window

def sign_up(e):
    # Clear previous output
    document.getElementById("output").innerHTML = ''

    # Get values from input fields
    username = document.getElementById('username').value.strip()
    password = document.getElementById('password').value

    username_length = len(username)
    password_length = len(password)

    # Username validation
    if username_length < 7:
        document.getElementById('output').innerHTML = "❌ Username must be at least 7 characters."
        return

    # Password validation
    if password_length < 10:
        remaining = 10 - password_length
        document.getElementById("output").innerHTML = f"❌ Password must be at least 10 characters. Add {remaining} more."
        return

    # Success message
    document.getElementById("output").innerHTML = "✅ Account Created Successfully!"

#List of teams and their corresponding images
teams = {
    "Green Hornets": "https://www.pngkit.com/png/full/272-2723135_green-hornets-green-hornets-logo.png",
    "Blue Bears": "https://i.pinimg.com/1200x/99/40/c3/9940c3a4e6ad5602f8cc278766ae2b5f.jpg",
    "Yellow Tigers": "https://i.pinimg.com/736x/e1/f8/46/e1f8468b389002c1a0410989a7709a11.jpg",
    "Red Bulldogs": "https://i.pinimg.com/1200x/4a/3f/95/4a3f9536e803edc15cdae53682d6d3a3.jpg"
}

def sign_up(event=None):
    reg = document.querySelector('input[name="registration"]:checked')
    med = document.querySelector('input[name="medical"]:checked')
    grade = document.getElementById("grade").value
    section = document.getElementById("section").value

    output = document.getElementById("output2")

    if not reg or not med or grade == "Enter Grade" or section == "Enter Section":
        output.innerHTML = "⚠️ Please complete all fields!"
        return

    if reg.value == "yes" and med.value == "yes":
        team = random.choice(list(teams.keys())) #Randomly assigns a team 
        image_url = teams[team]
        output.innerHTML = f"""
            🎉 Congratulations! You are part of the {team}! <br>
            <img src='{image_url}' alt='{team}' style='width:200px; margin-top:10px;'>
        """
    else:
        output.innerHTML = "⚠️ You must finish registration and have medical clearance first."
