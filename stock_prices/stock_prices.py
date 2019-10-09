#!/usr/bin/python
import argparse

prices = [1050, 270, 1540, 3800, 2]
def find_max_profit(prices):
    # Get current min and max
    for i in range(0, len(prices)-1):
        current_min = min(prices)
        current_max = 0
        if prices[i] > current_max:
            current_max = prices[i]
return profit
		i += 1
		else:
			print('No shorting allowed')
  # if index of max > min: subtract numbers and return result
  # else: return


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')

    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    # parser.add_argument('-l', '--list', type=list, action='store', dest='list',help='<Required> Set flag')
    args = parser.parse_args()

    profit = find_max_profit(args.integers)

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
