data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
			print('-----------')

print('檔案讀取完了，總共有', len(data),'筆資料')

wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 100:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('Enter the word you want to search for: ')
	if word not in wc:
		print('error')
		continue
	if word == 'q':
		break
	else:
		print(wc[word])



'''sum_len = 0
for d in data:
	sum_len += len(d)

total = len(data)
average = sum_len / total

print('average = ', average)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)

print('commit < len(100) :', len(new)) 

check_string = 'good'
checkbox = []

#for d in data:
#	if check_string in d:
#		checkbox.append(d)
#
#print(len(checkbox))

checkbox = [d + '123' for d in data if check_string in d]
bad = ['bad' in d for d in data]
print(bad)'''