import matplotlib.pyplot as plt
categories = ["Category A", "Category B", "Category C", "Category D"]
percetages = [25, 30, 15, 30]
explode = [0, 0.1, 0, 0]
colors =  ['red', 'green', 'blue', 'yellow']
plt.pie(percetages, explode = explode, labels = categories, colors = colors, shadow = True)
plt.title("Percentages Division")
plt.legend(categories)
plt.show()

