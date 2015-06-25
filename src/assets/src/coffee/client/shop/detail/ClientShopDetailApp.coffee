BaseApp = require 'base/BaseApp'
ClientShopDetailController = require './ClientShopDetailController'
ClientShopDetailRouter = require './ClientShopDetailRouter'


module.exports = class ClientShopDetailApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: ClientShopDetailController
	routerClass: ClientShopDetailRouter
	urlRoot: "/"