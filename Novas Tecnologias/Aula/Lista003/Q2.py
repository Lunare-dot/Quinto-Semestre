def fCount(list, min):
    count = {}
    
    for num in list:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
            
    x = []
    for num, freq in count.items():
        if freq >= min:
            x.append(num)
            
    return x
    
    
def main():
    uList = [1, 2, 2, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 8]
    print(fCount(uList, 3))
    
if __name__ == "__main__":
    main()