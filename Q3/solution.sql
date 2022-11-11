select result_1.owner_id, result_1.owner_name, count( distinct category_article_mapping.category_id)
from 
    (select owner.owner_id, owner.owner_name, article.article_id, 
    from owner 
    inner join article on article.owner_id = owner.owner_id)
    result_1
inner join category_article_mapping on result_1.article_id = category_article_mapping.article_id



