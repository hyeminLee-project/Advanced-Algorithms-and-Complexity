# python3

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    # 첫 번째 줄: N과 t 입력
    N = int(data[0])
    t = int(data[1])

    # 두 번째부터 N개의 줄까지 리스트 A 처리
    good_dict = {}
    for i in range(2, 2 + N):
        k, g = map(int, data[i].split())
        good_dict[k] = g

    # N개의 줄 이후부터 리스트 B 처리
    for i in range(2 + N, 2 + 2 * N):
        k, b = map(int, data[i].split())
        # 바로 좋은 일과 나쁜 일의 차이를 계산
        good_dict[k] -= b

    # 마지막 두 줄: 쿼리 수와 요청 ID 리스트
    q = int(data[2 + 2 * N])
    query_ids = map(int, data[3 + 2 * N].split())

    # 결과 계산
    result = []
    for k in query_ids:
        if good_dict[k] >= t:
            result.append(1)
        else:
            result.append(0)

    # 결과 출력
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()

