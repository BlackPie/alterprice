BaseApp = require 'base/BaseApp'
ProductController = require './ProductController'
ProductRouter = require './ProductRouter'


module.exports = class ProductApp extends BaseApp

	channelName: 'defaultChannel'
	controllerClass: ProductController
	routerClass: ProductRouter
	urlRoot: "/"