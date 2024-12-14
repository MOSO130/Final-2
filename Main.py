import tkinter as tk
from tkinter import messagebox


def calculate_savings():
    """Calculate the savings based on the inputs."""
    try:
        paycheck = float(paycheck_entry.get())
        percentage = float(percentage_entry.get())

        if paycheck <= 0:
            messagebox.showerror("Input Error", "Paycheck amount must be greater than 0.")
            return
        if percentage < 0 or percentage > 100:
            messagebox.showerror("Input Error", "Percentage must be between 0 and 100.")
            return

        # Calculate savings
        amount_to_save = (percentage / 100) * paycheck
        result_label.config(
            text=f"You should save ${amount_to_save:.2f} from your paycheck of ${paycheck:.2f}.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")


# Create the main application window
app = tk.Tk()
app.title("Savings Calculator")
app.geometry("400x300")

# Create labels and entry fields
paycheck_label = tk.Label(app, text="Paycheck Amount:")
paycheck_label.pack(pady=5)
paycheck_entry = tk.Entry(app)
paycheck_entry.pack(pady=5)

percentage_label = tk.Label(app, text="Percentage to Save (0-100):")
percentage_label.pack(pady=5)
percentage_entry = tk.Entry(app)
percentage_entry.pack(pady=5)

# Create calculate button
calculate_button = tk.Button(app, text="Calculate", command=calculate_savings)
calculate_button.pack(pady=10)

# Create result label
result_label = tk.Label(app, text="", fg="blue")
result_label.pack(pady=10)

# Run the application
app.mainloop()