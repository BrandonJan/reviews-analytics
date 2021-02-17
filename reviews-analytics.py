data =[]
count = 0
with open("reviews.txt", "r") as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print("檔案讀取完了，總共有", len(data), "筆資料")
sum_len = 0
for d in data:
    sum_len += len(d)  #sum_len = sum_len + len(d)
print("每篇留言平均長度為", sum_len/len(data))
new =[]
for d in data:
    if len(d) < 100:
        new.append(d)
print("一共有", len(new), "筆資料字數小於100")
good = []
for d in data: #以下四行等於 good = [d for d in data if "good in d"]
    if "good" in d:
        good.append(d)
print(good[0])
print("一共有", len(good), "筆留言提到good")

#計數功能
wc ={} #word_count
for d in data:
	words = d.split()#預設值 = 空白鍵
	for word in words:
		if word not in wc:
			wc[word] = 1
		elif word in wc:
			wc[word] += 1
	break
for word in wc:
    print(word, ":", wc[word])

while True:
    word = input("請問您想輸入甚麼字?")
    if word == "q":
        break
    if word not in wc:
        print("沒有這個字喔")
    elif word in wc:
        print(word, "出現了", wc[word], "次")

print("感謝使用此查詢功能")
