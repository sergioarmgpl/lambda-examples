import json

print('Loading function')

def lambda_handler(event, context):
	#1. Parse out query string params
	print("---------")
	print(event)
	print("---------")
	print(context)
	print("---------")
	par1 = event['queryStringParameters']['par1']
	par2 = event['queryStringParameters']['par2']

	print('par1=' + par1)
	print('par2=' + par2)

	#2. Construct the body of the response object
	transactionResponse = {}
	transactionResponse['par1'] = par1
	transactionResponse['par2'] = par2
	transactionResponse['add'] = str(int(par1)+int(par2))

	#3. Construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(transactionResponse)

	#4. Return the response object
	return responseObject
