BaseApp = require 'base/BaseApp'
CatalogSearchController = require './CatalogSearchController'
CatalogSearchRouter = require './CatalogSearchRouter'


module.exports = class CatalogSearchApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: CatalogSearchController
	routerClass: CatalogSearchRouter
	urlRoot: "/"