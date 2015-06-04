Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class DefaultRouter extends Marionette.AppRouter
	appRoutes:
		"": "index"