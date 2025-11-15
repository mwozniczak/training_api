from math import ceil

from ..models import PaginatedObject

def paginate(items, page, items_per_page):
    count = len(items)
    total_pages = ceil(count/items_per_page) - 1

    page_start = page*items_per_page
    page_end = min(count, page_start + items_per_page)
    items = items[page_start:page_end]
    return PaginatedObject(
        items=items,
        current_page=page,
        total_pages=total_pages
    )