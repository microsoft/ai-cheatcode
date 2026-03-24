@description('Search service name')
param name string

@description('Resource location')
param location string

@description('Resource tags')
param tags object

@description('Search SKU')
param sku string = 'basic'

resource search 'Microsoft.Search/searchServices@2023-11-01' = {
  name: name
  location: location
  tags: tags
  sku: { name: sku }
  properties: {
    replicaCount: 1
    partitionCount: 1
    hostingMode: 'default'
  }
}

output name string = search.name
output endpoint string = 'https://${search.name}.search.windows.net'
output adminKey string = search.listAdminKeys().primaryKey
