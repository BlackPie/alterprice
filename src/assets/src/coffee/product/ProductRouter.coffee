Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class ProductRouter extends Marionette.AppRouter
	appRoutes:
		"": "index"