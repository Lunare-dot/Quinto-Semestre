from typing import List, Dict

def fCount(values: List[int], threshold: int) -> List[int]:
    count: Dict[int, int] = {}
    
    for num in values:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            
    x: List[int] = []
    for num, freq in count.items():
        if freq >= threshold:
            x.append(num)
        
    return x
    
    
def main():
    uList = [1, 2, 2, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 8]
    print(fCount(uList, 3))
    
if __name__ == "__main__":
    main()