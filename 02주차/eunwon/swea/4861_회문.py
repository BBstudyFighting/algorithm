T = int(input())
for tc in range(1, T + 1):
	NM = list(map(int,input().split()))
	N = NM[0]
	M = NM[1]
	array = []
	for i in range(N):
		row = input()
		row_list = []
		for j in range(N):
			row_list.append(row[j])
		array.append(row_list)
		
	for i in range(N):
		
		for j in range(N-M+1):
			word_h = []
			word_v = []
			for k in range(M):
				word_h.append(array[i][k+j])
				word_v.append(array[j+k][i])
			reverse_word_h = word_h[::-1]
			print(word_h, word_v)
			if word_h == reverse_word_h:
				answer = "".join(word_h)
				break
			reverse_word_v = word_v[::-1]

			if word_v == reverse_word_v:
				answer = "".join(word_v)
				break

	print(f'#{tc} {answer}')
	
