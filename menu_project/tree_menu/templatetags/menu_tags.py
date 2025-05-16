from django import template
from django.urls import resolve
from tree_menu.models import MenuItem
from collections import defaultdict

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    path = request.path
    current_url_name = resolve(path).url_name if path else None

    items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')
    tree = defaultdict(list)
    for item in items:
        tree[item.parent_id].append(item)

    def build_tree(parent_id=None):
        nodes = []
        for item in tree[parent_id]:
            url = item.get_url()
            is_active = url == path or item.named_url == current_url_name
            children = build_tree(item.id)
            show_children = is_active or any(c['is_active'] or c['show_children'] for c in children)
            nodes.append({
                'item': item,
                'url': url,
                'is_active': is_active,
                'children': children,
                'show_children': show_children
            })
        return nodes

    return {'menu_tree': build_tree(), 'menu_name': menu_name}
