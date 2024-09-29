# 373. Find K Pairs with Smallest Sums
import heapq

def kSmallestPairs(nums1, nums2, k):
        if len(nums1)==0 or len(nums2)==0:
            return []
        min_heap=[]
        min_heap.append((nums1[0]+nums2[0],(nums1[0],nums2[0],0,0)))
        heapq.heapify(min_heap)

        result_arr=[]
        memory=set() # whether visited before or not

        while len(result_arr)<k and len(min_heap)!=0:
            # pop first
            smallest = heapq.heappop(min_heap)
            i = smallest[1][2]
            j = smallest[1][3]
            result_arr.append([smallest[1][0], smallest[1][1]])
            # add new items into the heap
            # judging range first
            if i + 1 < len(nums1) and (i + 1,j)not in memory:
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], (nums1[i + 1], nums2[j], i + 1, j)))
                memory.add((i+1,j))
            if j + 1 < len(nums2) and (i,j + 1) not in memory:
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], (nums1[i], nums2[j + 1], i, j + 1)))
                memory.add((i,j+1))
        return result_arr


if __name__ == '__main__':
    num1=[1,7,11]
    num2=[2,4,6]
    print(kSmallestPairs(num1,num2,3))

    # elements = [(1, 0), (1, 9), (0, 0), (2, 8)]
    # print((1,9) in elements)
    # heap = [(a + b, (a, b)) for a, b in elements]
    # heapq.heapify(heap)
    # print(heap)
    # smallest = heapq.heappop(heap)
    # print(smallest)

