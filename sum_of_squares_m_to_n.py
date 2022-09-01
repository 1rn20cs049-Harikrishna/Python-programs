def sum_of_squares_m_to_n(m, n):
    tot_sum = 0
    for i in range(m,n+1):
        tot_sum += i ** 2
    print(tot_sum)
        

m = int(input())
n = int(input())
# Call the sum_of_squares_m_to_n function
sum_of_squares_m_to_n(m,n)
