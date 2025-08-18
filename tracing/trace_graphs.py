import csv

def get_num_stats(line: list[str]) -> list[int]:
	stats = []
	word_mapping = {
		'true': 1,
		'false': 0,
		'exec()': 0,
		'fork()': 1,
		'exit()': 2,
		'malloc()': 3,
		'free()': 4,
		'realloc()': 5
	}
	for element in line:
		if element == '':
			continue
		elif element in word_mapping:
			stats.append(word_mapping[element])
		else:
			stats.append(int(element) if element.isdigit() else float(element))
	return stats

# list format: timestamp, tid, isMain, operation, stat1, stat2, stat3, stat4
# operations: exec() marks the start of main thread, fork() marks start of child thread,
# 		malloc(), realloc(), free()
# ismain: 0 == False, 1 == True
# represent operations by int:
# 		exec() = 0, fork() = 1, exit() = 2, malloc() = 3, free() = 4, realloc() = 5
# stats by operation:
# 		malloc: stat1 = process heap size, stat2 = thread heap size, stat3 = size of malloc()
# 		realloc: stat1 = process heap size, stat2 = thread heap size, stat3 = old size, stat4 = new size
# 		free(): stat1 = process heap size, stat2 = thread heap size, stat3 = size freed
trace_stats = []

with open("tracing/trace_results.csv", 'r') as trace_csv:
	trace_reader = csv.reader(trace_csv)
	next(trace_reader)

	for line in trace_reader:
		if len(line) == 0:
			continue
		trace_stats.append(get_num_stats(line))

for i in range(len(trace_stats)-5, len(trace_stats)):
	print(trace_stats[i])