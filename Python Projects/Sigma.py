import tkinter as tk

def display_hacker_mask():
    mask = '''
         ___
     . -^   `--,
    /# =========`-_
   /# (--====___====\\
  /#   .- --.  . --.|
 /##   |  * ) (   * ),
 |##   \\    /\\ \\   / |
 |###   ---   \\ ---  |
 |####      ___)    #|
 |######           ##|
  \\##### ---------- /
   \\####           (
    `\\###          |
      \\###         |
       \\##        |
        \\###.    .)
         `======/
    '''
    mask_label.config(text=mask)

# Create the main window
root = tk.Tk()
root.title("Hacker Mask")

# Create a label to display the hacker mask
mask_label = tk.Label(root, font=("Courier", 10), justify="left")
mask_label.pack()

# Button to display the hacker mask
display_button = tk.Button(root, text="Display Hacker Mask", command=display_hacker_mask)
display_button.pack()

# Run the Tkinter event loop
root.mainloop()


