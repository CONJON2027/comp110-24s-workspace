import matplotlib as plt
from runtime_analysis_functions import evaluate_runtime


__author__ = "730665579"

START_SIZE: int = 0
END_SIZE: int = 1000

times = evaluate_runtime("selection_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Selection Sort - conjon")
plt.show()