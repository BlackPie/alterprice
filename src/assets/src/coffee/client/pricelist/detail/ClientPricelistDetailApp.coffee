BaseApp = require 'base/BaseApp'
ClientPricelistDetailController = require './ClientPricelistDetailController'
ClientPricelistDetailRouter = require './ClientPricelistDetailRouter'


module.exports = class ClientPricelistDetailApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: ClientPricelistDetailController
	routerClass: ClientPricelistDetailRouter
	urlRoot: "/"