Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class ClientPricelistDetailRouter extends Marionette.AppRouter
	appRoutes:
		"": "index"