import gradio as gr
import re

def check_password(password):
    score = 0
    feedback = []

    if password == "":
        return "Password is empty.\nPlease enter a password"

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password too short")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add number")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add special character")

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return f"Score: {score}\nStrength: {strength}\n" + ", ".join(feedback)


def toggle(show):
    return gr.update(type="text" if show else "password")


with gr.Blocks() as app:
    gr.Markdown("Password Strength Checker")
    password_input = gr.Textbox(label="Password", type="password")
    show_toggle = gr.Checkbox(label="Show password")
    output = gr.Textbox(label="Result")
    btn = gr.Button("Check")

    show_toggle.change(fn=toggle, inputs=show_toggle, outputs=password_input)
    btn.click(fn=check_password, inputs=password_input, outputs=output)


app.launch()
