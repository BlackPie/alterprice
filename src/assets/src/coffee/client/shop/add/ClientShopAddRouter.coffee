Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class ClientShopAddRouter extends Marionette.AppRouter
	appRoutes:
		"": "index"