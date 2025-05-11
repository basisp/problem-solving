import sys

def main():
    H, W = map(int, input().split())

    height = list(map(int,input().split()))

    left, right = 0, W-1
    left_max, right_max = 0, 0
    ans =0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                ans += left_max - height[left]
            left +=1

        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                ans += right_max - height[right]
            right-=1
    
    print(ans)




if __name__ == "__main__":
    main()