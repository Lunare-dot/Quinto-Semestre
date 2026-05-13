from typing import List, Tuple

def listOrd(inter: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    inter.sort(key=lambda x: x[0])
    list: List[Tuple[int, int]] = []
    
    cStart, cEnd = inter[0]
    for start, end in inter[1:]:
        if start <= cEnd:
            cEnd = max(cEnd, end)
        else:
            list.append((cStart, cEnd))
            cStart, cEnd = start, end
        
    list.append((cStart, cEnd))
    return list
    
def main():
    uInter = [(1, 4), (2, 5), (7,9)]
    print(listOrd(uInter))
    
if __name__ == "__main__":
    main()