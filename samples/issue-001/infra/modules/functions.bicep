@description('Function app name')
param name string

@description('Resource location')
param location string

@description('Resource tags')
param tags object

@description('Storage account name for Functions runtime')
param storageAccountName string

@description('Storage account key')
param storageAccountKey string

@description('Azure AI Search endpoint')
param searchEndpoint string

@description('Azure AI Search admin key')
param searchAdminKey string

@description('Azure AI Search index name')
param searchIndexName string

@description('Azure OpenAI endpoint')
param openAiEndpoint string

@description('Azure OpenAI key')
param openAiKey string

@description('Azure OpenAI deployment name')
param openAiDeployment string

var abbrs = loadJsonContent('../abbreviations.json')
var resourceToken = toLower(uniqueString(subscription().id, name))

resource logAnalytics 'Microsoft.OperationalInsights/workspaces@2022-10-01' = {
  name: '${abbrs.logAnalyticsWorkspace}${resourceToken}'
  location: location
  tags: tags
  properties: {
    sku: { name: 'PerGB2018' }
    retentionInDays: 30
  }
}

resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: '${abbrs.applicationInsights}${resourceToken}'
  location: location
  tags: tags
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: logAnalytics.id
  }
}

resource hostingPlan 'Microsoft.Web/serverfarms@2023-01-01' = {
  name: '${abbrs.appServicePlan}${resourceToken}'
  location: location
  tags: tags
  sku: {
    name: 'Y1'
    tier: 'Dynamic'
  }
  properties: {
    reserved: true
  }
}

resource functionApp 'Microsoft.Web/sites@2023-01-01' = {
  name: name
  location: location
  tags: union(tags, { 'azd-service-name': 'api' })
  kind: 'functionapp,linux'
  properties: {
    serverFarmId: hostingPlan.id
    httpsOnly: true
    siteConfig: {
      pythonVersion: '3.11'
      linuxFxVersion: 'Python|3.11'
      appSettings: [
        { name: 'AzureWebJobsStorage', value: 'DefaultEndpointsProtocol=https;AccountName=${storageAccountName};AccountKey=${storageAccountKey};EndpointSuffix=${environment().suffixes.storage}' }
        { name: 'FUNCTIONS_EXTENSION_VERSION', value: '~4' }
        { name: 'FUNCTIONS_WORKER_RUNTIME', value: 'python' }
        { name: 'APPLICATIONINSIGHTS_CONNECTION_STRING', value: appInsights.properties.ConnectionString }
        { name: 'SCM_DO_BUILD_DURING_DEPLOYMENT', value: 'true' }
        { name: 'AZURE_SEARCH_ENDPOINT', value: searchEndpoint }
        { name: 'AZURE_SEARCH_KEY', value: searchAdminKey }
        { name: 'AZURE_SEARCH_INDEX', value: searchIndexName }
        { name: 'AZURE_OPENAI_ENDPOINT', value: openAiEndpoint }
        { name: 'AZURE_OPENAI_KEY', value: openAiKey }
        { name: 'AZURE_OPENAI_DEPLOYMENT', value: openAiDeployment }
        { name: 'AZURE_OPENAI_EMBEDDING_DEPLOYMENT', value: 'text-embedding-ada-002' }
        { name: 'AZURE_STORAGE_ACCOUNT', value: storageAccountName }
        { name: 'AZURE_STORAGE_KEY', value: storageAccountKey }
        { name: 'PDF_CONTAINER', value: 'pdfs' }
      ]
    }
  }
}

output name string = functionApp.name
output url string = 'https://${functionApp.properties.defaultHostName}'
