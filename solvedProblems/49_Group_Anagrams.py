class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for string in strs:
            

            counter_list = [0]*26
            for char in string:
                counter_list[ord(char) - ord('a')] += 1

            print(tuple(counter_list))
            result[tuple(counter_list)].append(string)


        return list(result.values())


        # map_list =[]

        # for item in strs:
            
        #     counter_map = {}
        #     for char in item:
        #         if char in counter_map:
        #             counter_map[char] += 1
        #         else:
        #             counter_map[char] = 1
        #     map_list.append(counter_map)


        # counter_map_2 = defaultdict(list)
        # for index,item in enumerate(map_list):
        #     counter_map_2[tuple(sorted(item.items()))].append(index)

        # final_list = []
        # for item in list(counter_map_2.values()):
        #     list_1 = []
        #     for item_inner in item:
        #         list_1.append(strs[item_inner])
        #     final_list.append(list_1)
   
        # return final_list



