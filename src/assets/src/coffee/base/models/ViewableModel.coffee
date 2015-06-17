Backbone   = require 'backbone'

module.exports = class ViewableModel extends Backbone.Model

    parse: (response) =>
        if response.data
          return response.data
        response


    getViewURL: () =>
      throw new Error "View URL not overriden"