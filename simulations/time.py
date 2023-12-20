from ursina import *

app = Ursina()
window.color = color.white  # Start with a white background

# Time tracking variables
time_elapsed = 13.85
max_time = 100
time_scale = 1 * 0.001

# On-screen Text to display time
time_text = Text(text=str(time_elapsed), color=color.black, position=(-0.95, 0.45), scale=2)

def lerp_color(color1, color2, t):
    # Manually interpolate the RGB values
    new_r = (1 - t) * color1.r + t * color2.r
    new_g = (1 - t) * color1.g + t * color2.g
    new_b = (1 - t) * color1.b + t * color2.b
    # Create a new Color with the interpolated values
    return Color(new_r, new_g, new_b, 1)

def update():
    global time_elapsed
    # Update the time
    time_elapsed += time.dt * time_scale
    # Keep time in the range [0, max_time]
    if time_elapsed > max_time:
        time_elapsed = 0
    
    # Update the on-screen text
    time_text.text = f"Time: {time_elapsed:.2f} B Years"

    # Calculate the lerp value
    lerp_value = time_elapsed / max_time
    # Update the background color using the manual lerp
    window.color = lerp_color(color.gray, color.black, lerp_value)
    time_text.color = lerp_color(color.black, color.white, lerp_value)

app.run()

