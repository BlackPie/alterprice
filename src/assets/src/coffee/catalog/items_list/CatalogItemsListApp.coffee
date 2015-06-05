BaseApp = require 'base/BaseApp'
CatalogItemsListController = require './CatalogItemsListController'
CatalogItemsListRouter = require './CatalogItemsListRouter'


module.exports = class CatalogItemsListApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: CatalogItemsListController
	routerClass: CatalogItemsListRouter
	urlRoot: "/"