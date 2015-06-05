Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class CatalogItemsListRouter extends Marionette.AppRouter
	appRoutes:
		"": "index"