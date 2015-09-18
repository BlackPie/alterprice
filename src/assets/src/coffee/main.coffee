$ = require 'jquery'
Backbone = require 'backbone'
Backbone.$ = $
logger = require 'loglevel'
csrfHandler = require './base/utils/csrfHandler'
LogoFooterMagic = require 'logo_footer_magic'

logoFooterMagic = new LogoFooterMagic
  elem: 'footer-copy'
  color: '#a5a5a5'
  prefix: 'w-'

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
ClientPasswordResetApp = require 'client/password_reset/ClientPasswordResetApp'
ClientRegistrationApp = require 'client/registration/ClientRegistrationApp'
ClientProfileApp = require 'client/profile/ClientProfileApp'
ClientShopAddApp = require 'client/shop/add/ClientShopAddApp'
ClientShopDetailApp = require 'client/shop/detail/ClientShopDetailApp'
ClientWalletRefillApp  = require 'client/wallet/refill/ClientWalletRefillApp'
ClientPricelistDetailApp = require 'client/pricelist/detail/ClientPricelistDetailApp'
ClientWalletBalanceApp = require 'client/wallet/balance/ClientWalletBalanceApp'
ClientStatisticsApp = require 'client/statistics/ClientStatisticsApp'


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
    'client-reset-password': ClientPasswordResetApp
    'client-wallet-balance': ClientWalletBalanceApp
    'client-statistics': ClientStatisticsApp

if window.context != undefined
    context = JSON.parse window.context
else
    context = {}


initializeApp = () ->
    if entryPoint of entryPoints
        logger.debug "Starting #{entryPoint} app"
        new entryPoints[getEntryPoint()]({ context: context })

initializeApp()
