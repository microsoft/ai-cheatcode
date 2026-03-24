targetScope = 'subscription'

@minLength(1)
@maxLength(64)
@description('Name of the environment (e.g., dev, prod)')
param environmentName string

@minLength(1)
@description('Primary location for all resources')
param location string

@description('Azure OpenAI model deployment name')
param openAiModelName string = 'gpt-4o'

@description('Azure OpenAI model version')
param openAiModelVersion string = '2024-08-06'

@description('Azure AI Search SKU')
param searchSku string = 'basic'

var abbrs = loadJsonContent('abbreviations.json')
var resourceToken = toLower(uniqueString(subscription().id, environmentName, location))
var tags = { 'azd-env-name': environmentName, 'project': 'cheat-code-pdf-agent' }

resource rg 'Microsoft.Resources/resourceGroups@2022-09-01' = {
  name: '${abbrs.resourceGroup}${environmentName}'
  location: location
  tags: tags
}

module storage 'modules/storage.bicep' = {
  name: 'storage'
  scope: rg
  params: {
    name: '${abbrs.storageAccount}${resourceToken}'
    location: location
    tags: tags
  }
}

module search 'modules/search.bicep' = {
  name: 'search'
  scope: rg
  params: {
    name: '${abbrs.searchService}${resourceToken}'
    location: location
    tags: tags
    sku: searchSku
  }
}

module openai 'modules/openai.bicep' = {
  name: 'openai'
  scope: rg
  params: {
    name: '${abbrs.openAiAccount}${resourceToken}'
    location: location
    tags: tags
    modelName: openAiModelName
    modelVersion: openAiModelVersion
  }
}

module functions 'modules/functions.bicep' = {
  name: 'functions'
  scope: rg
  params: {
    name: '${abbrs.functionApp}${resourceToken}'
    location: location
    tags: tags
    storageAccountName: storage.outputs.name
    storageAccountKey: storage.outputs.key
    searchEndpoint: search.outputs.endpoint
    searchAdminKey: search.outputs.adminKey
    searchIndexName: 'pdf-documents'
    openAiEndpoint: openai.outputs.endpoint
    openAiKey: openai.outputs.key
    openAiDeployment: openai.outputs.deploymentName
  }
}

output AZURE_RESOURCE_GROUP string = rg.name
output AZURE_STORAGE_ACCOUNT string = storage.outputs.name
output AZURE_STORAGE_CONNECTION_STRING string = storage.outputs.connectionString
output AZURE_SEARCH_ENDPOINT string = search.outputs.endpoint
output AZURE_SEARCH_INDEX string = 'pdf-documents'
output AZURE_OPENAI_ENDPOINT string = openai.outputs.endpoint
output AZURE_OPENAI_DEPLOYMENT string = openai.outputs.deploymentName
output AZURE_FUNCTION_URL string = functions.outputs.url
output SERVICE_API_URI string = functions.outputs.url
