def linearSearchProduct(productList,targetProduct):
  indices = []
  for index,product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices

#Example usage:
products=["shoes","boot","lofafer","shoes","sandal","shoes"]
target1 = "shoes"
target2 = "apple"
result = linearSearchProduct(products, target2)
print(result)
