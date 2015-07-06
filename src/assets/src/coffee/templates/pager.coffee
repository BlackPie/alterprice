template = (locals) =>
    result = ''

    if locals.countPages > 1
        for page in [1..locals.countPages]
            if page == locals.currentPage
                result = "#{result}<li class=\"active\"><a href=\"#\" class=\"toPage\" data-page=\"#{page}\">#{page}</a></li>"
            else
                result = "#{result}<li><a href=\"#\" class=\"toPage\" data-page=\"#{page}\">#{page}</a></li>"

        if locals.currentPage > 1
            prevPage = locals.currentPage - 1
            result = "<li class=\"prev\"><a href=\"#\" data-page=\"#{prevPage}\">&lt; Предыдущая</a></li>#{result}"
        else
            result = "<li class=\"prev hide\"><a href=\"#\" data-page=\"0\">&lt; Предыдущая</a></li>#{result}"
        if locals.currentPage < locals.countPages
            nextPage = locals.currentPage + 1
            result = "#{result}<li class=\"next\"><a href=\"#\" data-page=\"#{nextPage}\">Следующая &gt;</a></li>"
        else
            nextPage = locals.currentPage + 1
            result = "#{result}<li class=\"next hide\"><a href=\"#\" data-page=\"#{nextPage}\">Следующая &gt;</a></li>"
        result = "<div class=\"pager\"><ul>#{result}</ul></div>"
        return result
    else
        ""


module.exports = template