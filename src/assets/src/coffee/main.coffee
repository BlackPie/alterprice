$ = require 'jquery'
Backbone = require 'backbone'
Backbone.$ = $
logger = require 'loglevel'
csrfHandler = require './base/utils/csrfHandler'


$.ajaxSetup
    beforeSend: csrfHandler
    traditional: true

logger.setLevel(logger.levels.DEBUG)


DefaultApp = require 'default/DefaultApp'
ProductApp = require 'product/ProductApp'
CatalogItemsListApp = require 'catalog/items_list/CatalogItemsListApp'


getEntryPoint = ->
    for script in document.getElementsByTagName('script')
        entryPoint = script.getAttribute('data-main')
        if entryPoint
            return entryPoint
    return 'default'


entryPoint = getEntryPoint()

entryPoints =
    'default': DefaultApp
    'catalog-items-list': CatalogItemsListApp
    'product-detail': ProductApp


if window.context != undefined
    context = JSON.parse window.context
else
    context = {}


initializeApp = () ->
    if entryPoint of entryPoints
        logger.debug "Starting #{entryPoint} app"
        new entryPoints[getEntryPoint()]({ context: context })

initializeApp()