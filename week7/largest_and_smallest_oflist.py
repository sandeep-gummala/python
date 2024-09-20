def lar_and_small(li):
    return max(li),min(li)
results=lar_and_small([2,5,7,9])
print(f'largest: {results[0]}')
print(f'smallest: {results[1]}')
