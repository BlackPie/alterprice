PrettyPrice = require 'base/utils/PrettyPrice'

template = (locals) =>
    price = PrettyPrice.format locals.price


    return """
        <div class="item-card-block block-1-x first-inline">
            <a target="_blank" href="#{locals.click_url}">
                <div class="title">#{locals.name}</div>
            </a>
            <div class="price">от <span>#{price}</span> руб</div>
            <div class="shop">В <a target="_blank" href="#{locals.click_url}">#{locals.shop.name}</a></div>
            <div class="offer-shop">
                <a target="_blank" href="#{locals.click_url}" class="btn btn-purple-border btn-full-width">В магазин</a>
            </div>
        </div>
    """

#    <div class=\"shop\">В <a href=\"#\">#{locals.offer.name}</a><br>ещё <a href=\"#\">#{locals.offers_count} предложений</a></div>


module.exports = template
