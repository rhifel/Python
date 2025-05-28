import matplotlib.pyplot as pyplot                                                                              

labels = ('DSA', 'Physics', 'Calculus', 'History')
sizes = [48, 12, 18, 22]

pyplot.pie(sizes,
           labels=labels,
           autopct='%1.1f%%',
           counterclock=True,
           startangle=105)

pyplot.show()
