#!/usr/bin/python
import argparse


def find_max_profit(prices):
	# Get current min and max
	current_min = 0
	current_max = 1
	for i in range(0, len(prices)-1):
		if prices[i] < current_min:
			current_min = prices[i]
		elif prices[i] > current_max:
			current_max = prices[i]
    
  # Check if the index of max > min
  # if index of max > min: subtract numbers and return result
  # else: return
	pass


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    profit = find_max_profit(args.integers)

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
