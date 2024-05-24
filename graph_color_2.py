def generate_timetable(subjects, clashes):
    def chromatic_number(graph):
        colors = {}
        for node in graph:
            neighbor_colors = set(colors.get(neigh, None) for neigh in graph[node])
            color = 1
            while color in neighbor_colors:
                color += 1
            colors[node] = color
        return colors, max(colors.values())

    graph = {}
    for subject, clash_list in clashes.items():
        graph[subject] = set(clash_list)

    coloring, num_colors = chromatic_number(graph)

    timetable = {i: [] for i in range(1, num_colors + 1)}
    for subject, color in coloring.items():
        timetable[color].append(subject)

    return timetable, num_colors

subjects = input("Enter subjects separated by commas: ").split(',')
clashes = {}
for subject in subjects:
    clashes[subject] = input(f"Enter subjects {subject} clashes with separated by commas (or leave blank if none): ").split(',')

timetable, chromatic_num = generate_timetable(subjects, clashes)
print("Timetable:")
for slot, subjects in timetable.items():
    print(f"Slot {slot}: {', '.join(subjects)}")
print("Chromatic number:", chromatic_num)
