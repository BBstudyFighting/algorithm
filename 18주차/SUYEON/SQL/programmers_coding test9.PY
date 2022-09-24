# 최소직사각형
# 각 w, h를 비교해서 둘 중 큰 값을 한 리스트에 넣고 나머지를 리스트로 만든다. 두 개의 리스트 중 가장 큰 값을 뽑아서 곱하면 된다.

# w, h 리스트를 만든다.
# for문을 돌면서 w, h 중 큰 값은 w리스트 작은 값은 h리스트에 담는다.
# 두 개의 리스트에서 가장 큰 값이 곱한 값이 답이다.

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)

def solution(sizes):
    answer = 0
    
    sizes = [sorted(size, reverse=True) for size in sizes]
    
    widths = [size[0] for size in sizes]
    heights = [size[1] for size in sizes]
    
    width, height = max(widths), max(heights)
    
    answer = width * height
    
    return answer
