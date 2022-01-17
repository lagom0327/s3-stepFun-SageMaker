exports.handler = async (event) => {
    console.log(event)
    const objectPath = event['object']

    const [fileName] = objectPath.split('/').slice(-1) 
    const fileNameWithoutExtension = fileName.split('.')[0]
    const batchId = Number(fileNameWithoutExtension.split('partition_').slice(-1)[0])
    console.log('id', batchId)


	if(!Number.isInteger(batchId)) {
    	const response = {
        statusCode: 400,
        error: "batch_id is not integer",
    	}
        console.log(response)
        return response
    }

	const response = {
      statusCode: 200,
      body: {
        batch_id: batchId
      },
    }
     
	console.log(response)
    return response;
};
