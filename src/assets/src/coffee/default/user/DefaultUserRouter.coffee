Marionette = require 'backbone.marionette'
Backbone   = require 'backbone'


module.exports = class DefaultUserRouter extends Marionette.AppRouter
	appRoutes:
		"": "index"