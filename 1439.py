 def kthSmallest(self, mat: List[List[int]], k: int) -> int:
    	#Maintain a minimum heap
        minh = []
        # m 
        m = len(mat)
        #n column
        n = len(mat[0])

        #The current position of each line, the first combination, we all go to the first position
        index = [0]*m

		#Find the sum of the index
        def getSum(mat, index):
            total = 0
            m = 0
            for i in index:
                total += mat[m][i]
                m+=1
            return total

		#Turn the index into a decimal number, it is convenient to add the set to verify whether it has been visited
        def convert(index):
            ci = 0
            for i in index:
                ci = ci*10 + i                
            return ci

        visited = set()
        visited.add(convert(index))
        collections._heapq.heappush(minh, (getSum(mat, index), index))
        while k > 0 and len(minh) > 0:
            current = collections._heapq.heappop(minh)
            k -=1
            index = current[1]
            #Move one line, join the heap
            for i in range(m):
                if index[i] == n-1:
                    continue
                ic = index.copy()
                ic[i] +=1
				#If you have already visited, then no longer join
                if convert(ic) in visited:
                    continue
                collections._heapq.heappush(minh, (getSum(mat, ic), ic))
                visited.add(convert(ic))

        return current[0]
