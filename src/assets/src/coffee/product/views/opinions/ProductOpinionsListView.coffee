$ = require 'jquery'
Backbone = require 'backbone'
Marionette = require 'backbone.marionette'
ProductOpinionsItemView = require './ProductOpinionsItemView'


module.exports = class ProductOpinionsListView extends Marionette.CollectionView
    template: false

    initialize: (options) =>
        @channel = options.channel

    getChildView: (model) =>
        return ProductOpinionsItemView