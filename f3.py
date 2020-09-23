import json

print('Loading function')

def lambda_handler(event, context):
	#1. Parse out query string params
	par1 = event['queryStringParameters']['par1']
	par2 = event['queryStringParameters']['par2']

	r = 0
	a = int(par1)
	b = int(par2)
	print("antes del if")
	if event['path'] == "/add2":
		r = a + b
	elif event['path'] == "/sus2":
		r = a - b
	print("todo bien")
	#2. Construct the body of the response object
	transactionResponse = {}
	transactionResponse['par1'] = par1
	transactionResponse['par2'] = par2
	transactionResponse['result'] = str(r)

	#3. Construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(transactionResponse)

	#4. Return the response object
	return responseObject
