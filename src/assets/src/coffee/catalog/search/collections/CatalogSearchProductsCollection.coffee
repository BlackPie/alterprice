CatalogProductsCollection = require 'catalog/items_list/collections/CatalogProductsCollection'

module.exports = class CatalogSearchProductsCollection extends CatalogProductsCollection

    url: "/api/product/search/"
