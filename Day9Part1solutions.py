points = []
with open(r"E:\advent\input.txt") as f:
    for line in f:
        x, y = map(int, line.strip().split(","))
        points.append((x, y))

max_area = 0

for i in range(len(points)):
    for j in range(i+1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]
        
        width  = abs(x1 - x2) + 1
        height = abs(y1 - y2) + 1
        
        area = width * height
        if area > max_area:
            max_area = area

print(max_area)
