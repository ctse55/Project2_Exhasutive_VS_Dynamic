import re

def max_stocks_exhaustive(size, stocksValues, total):
    max_stocks = 0

    #Ensure that size = stocks_and_values
    if size != len(stocksValues):
        raise ValueError("Size of the array does not match the provided list")

    #Go through all possible combinations 
    for combo in range(1 << size):
        total_cost = 0
        total_stocks = 0

        for i in range(size):
            #Check if the ith stock is included in the current combination
            if combo & (1 << i):
                total_cost += stocksValues[i][1]
                total_stocks += stocksValues[i][0]
        
        #Check if this combination is within the budget and maximizes the stocks 
        if total_cost <= total:
            max_stocks = max(max_stocks, total_stocks)
    
    return max_stocks

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
results = run_test_cases(file, max_stocks_exhaustive)  

# Print the results
for caseNumber, result in enumerate(results, start=1):
    print(f"Test Case {caseNumber}: Result = {result}")
