template = (locals) =>
    #return "<div><div id=\"catalog-search-categories-list-view\" class=\"categories-filter\"><div class=\"category-tabs\"></div></div></div>"
    return "<div id=\"catalog-search-categories-list-view\" class=\"categories-filter category-tabs\"></div>
    <a href=\"#\" class=\"show-all\" style=\"display: none;\">Все 1 категорий</a>"


module.exports = template