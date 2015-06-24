Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class CatalogSearchRouter extends Marionette.AppRouter
	appRoutes:
		"": "index"