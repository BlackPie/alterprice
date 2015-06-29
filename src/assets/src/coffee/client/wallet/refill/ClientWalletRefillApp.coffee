BaseApp = require 'base/BaseApp'
ClientWalletRefillController = require './ClientWalletRefillController'
ClientWalletRefillRouter = require './ClientWalletRefillRouter'


module.exports = class ClientWalletRefillApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: ClientWalletRefillController
	routerClass: ClientWalletRefillRouter
	urlRoot: "/"