class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        # Step 2: Create a max heap by using negative counts
        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)

        # Total time required
        time = 0

        # Step 3: Process tasks in cycles of size (n + 1)
        while maxHeap:

            # Temporary list to store remaining tasks
            temp = []

            # Set cycle size as cooldown + 1
            cycle = n + 1

            # Track number of tasks run in this cycle
            i = 0

            # Run up to (n+1) tasks or until heap is empty
            while i < cycle and maxHeap:

                # Get the task with highest remaining count
                count = heapq.heappop(maxHeap)

                # Decrease count since task used once
                count += 1  # since it's negative

                # If still tasks remaining, push to temp
                if count < 0:
                    temp.append(count)

                # Count 1 unit of time
                time += 1
                i += 1

            # Step 4: Push remaining tasks back into the heap
            for item in temp:
                heapq.heappush(maxHeap, item)

            # Step 5: Add idle time if heap still has tasks
            if maxHeap:
                time += (cycle - i)

        # Return total time taken
        return time
        