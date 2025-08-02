#
import random

projects = ["Project A", "Project B", "Project C"]
weights = [0.1, 0.7, 0.2]  # Ưu tiên Project B
print("Dự án ngẫu nhiên (có trọng số):", random.choices(projects, weights=weights, k=1)[0])
