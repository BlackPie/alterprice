BaseApp = require 'base/BaseApp'
ClientShopAddController = require './ClientShopAddController'
ClientShopAddRouter = require './ClientShopAddRouter'


module.exports = class ClientShopAddApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: ClientShopAddController
	routerClass: ClientShopAddRouter
	urlRoot: "/"