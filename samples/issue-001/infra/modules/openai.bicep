@description('OpenAI account name')
param name string

@description('Resource location')
param location string

@description('Resource tags')
param tags object

@description('Model name to deploy')
param modelName string

@description('Model version')
param modelVersion string

resource openai 'Microsoft.CognitiveServices/accounts@2023-10-01-preview' = {
  name: name
  location: location
  tags: tags
  kind: 'OpenAI'
  sku: { name: 'S0' }
  properties: {
    customSubDomainName: name
    publicNetworkAccess: 'Enabled'
  }
}

resource deployment 'Microsoft.CognitiveServices/accounts/deployments@2023-10-01-preview' = {
  parent: openai
  name: modelName
  sku: {
    name: 'Standard'
    capacity: 30
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: modelName
      version: modelVersion
    }
  }
}

resource embeddingDeployment 'Microsoft.CognitiveServices/accounts/deployments@2023-10-01-preview' = {
  parent: openai
  name: 'text-embedding-ada-002'
  sku: {
    name: 'Standard'
    capacity: 30
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: 'text-embedding-ada-002'
      version: '2'
    }
  }
  dependsOn: [deployment]
}

output name string = openai.name
output endpoint string = openai.properties.endpoint
output key string = openai.listKeys().key1
output deploymentName string = deployment.name
output embeddingDeploymentName string = embeddingDeployment.name
