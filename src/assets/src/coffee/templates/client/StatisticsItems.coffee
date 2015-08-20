template = (locals) =>
    return "
        <div class=\"counter-wrapper\">
            <div class=\"click-counter\">0<div>Кликов</div></div>
            <div class=\"expense-counter\">0<span>руб.</span><div>Расход</div></div>
        </div>
        <table>
            <thead>
                <tr>
                    <th>Название #{if locals.type is 'offers' then 'товара' else 'категории'}</th>
                    <th class=\"text-center\" width=\"170px\">Количество кликов</th>
                    <th class=\"text-center\" width=\"170px\">Расход, р</th>
                </tr>
            </thead>
            <tbody></tbody>
        </table>
    "


module.exports = template
