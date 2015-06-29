$ = require 'jquery'
Backbone = require 'backbone'
Backbone.$ = $
logger = require 'loglevel'
csrfHandler = require './base/utils/csrfHandler'


$.ajaxSetup
    beforeSend: csrfHandler
    traditional: true

logger.setLevel(logger.levels.DEBUG)


DefaultUserApp = require 'default/user/DefaultUserApp'
ProductApp = require 'product/ProductApp'
CatalogItemsListApp = require 'catalog/items_list/CatalogItemsListApp'
CatalogSearchApp = require 'catalog/search/CatalogSearchApp'
ClientIndexApp = require 'client/index/ClientIndexApp'
ClientLoginApp = require 'client/login/ClientLoginApp'
ClientRegistrationApp = require 'client/registration/ClientRegistrationApp'
ClientProfileApp = require 'client/profile/ClientProfileApp'
ClientShopAddApp = require 'client/shop/add/ClientShopAddApp'
ClientShopDetailApp = require 'client/shop/detail/ClientShopDetailApp'
ClientWalletRefillApp  = require 'client/wallet/refill/ClientWalletRefillApp'
ClientPricelistDetailApp = require 'client/pricelist/detail/ClientPricelistDetailApp'


getEntryPoint = ->
    for script in document.getElementsByTagName('script')
        entryPoint = script.getAttribute('data-main')
        if entryPoint
            return entryPoint
    return 'default'


entryPoint = getEntryPoint()

entryPoints =
    'default': DefaultUserApp
    'catalog-items-list': CatalogItemsListApp
    'catalog-search': CatalogSearchApp
    'product-detail': ProductApp
    'client-index': ClientIndexApp
    'client-login': ClientLoginApp
    'client-registration': ClientRegistrationApp
    'client-profile': ClientProfileApp
    'client-shop-add': ClientShopAddApp
    'client-shop-detail': ClientShopDetailApp
    'client-wallet-refill': ClientWalletRefillApp
    'client-pricelist-detail': ClientPricelistDetailApp


if window.context != undefined
    context = JSON.parse window.context
else
    context = {}


initializeApp = () ->
    if entryPoint of entryPoints
        logger.debug "Starting #{entryPoint} app"
        new entryPoints[getEntryPoint()]({ context: context })

initializeApp()