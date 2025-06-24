import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
from model_predictor import predict_weight

def submit():
    try:
        inputs = {
            "Model Name": entry_name.get(),
            "Model Length": float(entry_length.get()),
            "Model Breadth": float(entry_breadth.get()),
            "Model Height": float(entry_height.get()),
            "Number of Vertical Separations in Model": int(entry_tiers.get()),
            "Number of Compartments in Model": int(entry_compartments.get()),
            "Material": entry_material.get()
        }

        inputs_for_prediction = inputs.copy()
        del inputs_for_prediction["Model Name"]

        predicted_weight = predict_weight(inputs_for_prediction)
        buffered_weight = round(predicted_weight, 2)

        inputs["Predicted Weight (with 10% buffer)"] = buffered_weight

        file_path = "File-Calculator.xlsx"
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
            df = pd.concat([df, pd.DataFrame([inputs])], ignore_index=True)
        else:
            df = pd.DataFrame([inputs])
        df.to_excel(file_path, index=False)

        messagebox.showinfo("Prediction!", f"Predicted Weight: {buffered_weight:.2f} kg")

    except Exception as e:
        messagebox.showerror("Error!", f"Invalid input:\n{str(e)}")

# Main UI
root = tk.Tk()
root.title("Model Weight Predictor")
root.geometry("500x600")
root.resizable(False, False)
root.configure(bg="#f0f4f7")

# Heading
title = tk.Label(root, text=" ACE Model Weight Predictor", font=("Arial", 18, "bold"), bg="#f0f4f7", pady=10)
title.pack()

# Form Frame
form_frame = tk.Frame(root, bg="#f0f4f7", padx=20)
form_frame.pack(pady=10)

# Labels and Entry widgets

fields = [
    ("Model Name", "entry_name"),
    ("Model Length (m)", "entry_length"),
    ("Model Breadth (m)", "entry_breadth"),
    ("Model Height (m)", "entry_height"),
    ("Number of Tiers", "entry_tiers"),
    ("Number of Compartments", "entry_compartments"),
    ("Material (Al or MS)", "entry_material"),
]

entries = {}

for label_text, var_name in fields:
    label = tk.Label(form_frame, text=label_text, anchor="w", bg="#f0f4f7", font=("Arial", 10))
    label.pack(fill="x")
    entry = tk.Entry(form_frame, width=40)
    entry.pack(pady=5)
    entries[var_name] = entry

# Assign entries
entry_name = entries["entry_name"]
entry_length = entries["entry_length"]
entry_breadth = entries["entry_breadth"]
entry_height = entries["entry_height"]
entry_tiers = entries["entry_tiers"]
entry_compartments = entries["entry_compartments"]
entry_material = entries["entry_material"]

# Submit Button
submit_btn = tk.Button(root, text="Predict Weight", command=submit, font=("Arial", 12), bg="#4caf50", fg="white", padx=10, pady=5)
submit_btn.pack(pady=20)

# Footer
footer = tk.Label(root, text="Property of ACE Switchboards©2025", font=("Arial", 8), bg="#f0f4f7", fg="gray")
footer.pack(side="bottom", pady=10)

root.mainloop()
