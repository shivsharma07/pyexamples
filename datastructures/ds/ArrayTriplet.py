def triplet_sum(input1,input2,input3):

#Write code here
    input1.sort()
    i=0
    while(i < input2-2):
        l = i+1
        r = input2-1
        while(l<r):
            if input1[i] + input1[l] + input1[r] == input3:
                return True
            elif input1[i] + input1[l] + input1[r] < input3:
                l = l+1
            else:
                r = r-1

    return False

print triplet_sum([4,2,12,18,6],4,12)