import re

def max_stocks_dp(size, stockValues, total):
    
    #Checks if size is the same as the stocksValues length 
    if size != len(stockValues):
        raise ValueError("The array size does not match the provided list")
    
    #Initialize the DP Table 
    dp = [[0 for a in range(total + 1)] for b in range(size + 1)]

    #Filling the DP Table
    for i in range(1, size + 1):
        for j in range(1, total + 1):
            stock_count, stock_value = stockValues[i - 1]
            if stock_value <= j:
                #Max of including or not including the current stock
                dp[i][j] = max(dp[i - 1][j], stock_count + dp[i-1][j-stock_value])
            else:
                #Cannot include the current stock
                dp[i][j] = dp[i-1][j]
    
    return dp[size][total]

###### TEST CASE PARSING ######
def parse_test_case(testCase_str):
    lines = testCase_str.strip().split("\n")
    cases = int(lines[1].strip())

    #Using an expression to find all the pairs in the [x,y] format
    stocksValues_str = lines[2].strip()
    stocks_and_values = re.findall(r'\[(\d+),\s*(\d+)\]', stocksValues_str)
    stocks_and_values = [[int(x), int(y)] for x, y in stocks_and_values]

    amount = int(lines[3].strip())
    return cases, stocks_and_values, amount

def run_test_cases(file_path, test_function):
    with open(file_path, 'r') as file:
        test_cases_content = file.read()

    test_cases = test_cases_content.split("Case ")[1:]  #Split and Remove the first empty line 
    results = []
    for test_case_str in test_cases:
        N, stocks_and_values, amount = parse_test_case(test_case_str)
        result = test_function(N, stocks_and_values, amount)
        results.append(result)
    
    return results

file = 'Input_testCases.txt' 
results = run_test_cases(file, max_stocks_dp)  

# Print the results
for caseNumber, result in enumerate(results, start=1):
    print(f"Test Case {caseNumber}: Result = {result}")