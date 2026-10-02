import time
import random
from function_utils import max_search

def study_performance(n, fn_to_study, max_value, x_len):
    time_list = []

    for i in range(n):
        start_time = time.time()
        x = random.sample(range(1, max_value), x_len) # generate a list of random numbers
        # call our function to search the largest number
        max_val, index_max = fn_to_study(x)
        print("max:", max_val, "index:", index_max)

        process_time = time.time() - start_time
        time_list.append(process_time)

    # print("Avg execution time of the function: ", sum(time_list)/n, " [s]")

    return sum(time_list)/n


def main():
    # study_performance(n=30, fn_to_study=max_search, max_value=50, x_len=20)
    avg_time = study_performance(n=30, fn_to_study=max_search, max_value=1000, x_len=100)
    print("Average time:", avg_time)

if __name__ == "__main__":
    main()

